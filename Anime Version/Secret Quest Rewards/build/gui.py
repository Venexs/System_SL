# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from datetime import datetime, timedelta, date
import subprocess
import json
import csv
import cv2
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class VideoPlayer:
    def __init__(self, canvas, video_path, x, y, frame_skip=2, resize_factor=0.8):
        self.canvas = canvas
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.x = x
        self.y = y
        self.frame_skip = frame_skip  # Number of frames to skip
        self.resize_factor = resize_factor  # Factor to resize frames
        self.image_id = self.canvas.create_image(self.x, self.y)
        self.frame_count = 0
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        
        if not ret:
            # If the video has ended, reset the capture object
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        if ret:
            self.frame_count += 1
            if self.frame_count % self.frame_skip == 0:  # Skip frames for performance
                frame = cv2.resize(frame, (0, 0), fx=self.resize_factor, fy=self.resize_factor)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.canvas.itemconfig(self.image_id, image=imgtk)
                self.canvas.imgtk = imgtk

        self.canvas.after(10, self.update_frame)

    def __del__(self):
        self.cap.release()

def start_move(event):
    global lastx, lasty
    lastx = event.x_root
    lasty = event.y_root

def move_window(event):
    global lastx, lasty
    deltax = event.x_root - lastx
    deltay = event.y_root - lasty
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry("+%s+%s" % (x, y))
    lastx = event.x_root
    lasty = event.y_root

def ex_close(win):
    win.quit()

subprocess.Popen(['python', 'sfx.py'])

window = Tk()

window.geometry("555x669")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.overrideredirect(True)
window.wm_attributes("-topmost", True)

with open("Files/Status.json", 'r') as rank_check_file:
    rank_check_data=json.load(rank_check_file)
    lvl=rank_check_data["status"][0]['level']

    if lvl>=1 and lvl<=10:
        rank="E"
    elif lvl>=11 and lvl<=20:
        rank="D"
    elif lvl>=21 and lvl<=30:
        rank="C"
    elif lvl>=31 and lvl<=45:
        rank="B"
    elif lvl>=46 and lvl<=65:
        rank="A"
    elif lvl>=66 and lvl<=80:
        rank="S"
    elif lvl>=81 and lvl<=90:
        rank="SS"
    elif lvl>=91 and lvl<=100:
        rank="SSS"
    elif lvl>=101:
        rank="National"

with open("Files/Data/Rank_Rewards.json", 'r') as final_rank_check_file:
    final_rank_check_data=json.load(final_rank_check_file)
    rew_list=final_rank_check_data[rank]

    av_str=av_int=(rew_list[0]*2)
    xp_pl=(rew_list[1]*2)
    coins=(rew_list[2]*2)

today = date.today()
today_date_str = today.strftime("%Y-%m-%d")

with open("Files/Checks/Daily_time_check.csv", 'w', newline='') as Daily_date_check_file:
    fw=csv.writer(Daily_date_check_file)
    fw.writerow([today_date_str, "False"])

with open("Files/Data/Streaks.json", "r") as streak_file:
    streak_file_data=json.load(streak_file)
    streak=streak_file_data["Streak"][0]

with open("Files/Titles/Title_list.json", "r") as list_of_titles:
    list_of_titles_data=json.load(list_of_titles)
    list_of_titles_keys=list(list_of_titles_data.keys())

    if streak>=0 and streak<=3:
        title=list_of_titles_keys[0]
    elif streak>=4 and streak<=8:
        title=list_of_titles_keys[1]
    elif streak>=9 and streak<=14:
        title=list_of_titles_keys[2]
    elif streak>=15 and streak<=20:
        title=list_of_titles_keys[3]
    elif streak>=21 and streak<=30:
        title=list_of_titles_keys[4]
    elif streak>=31 and streak<=40:
        title=list_of_titles_keys[5]
    elif streak>=41 and streak<=50:
        title=list_of_titles_keys[6]
    elif streak>=51 and streak<=70:
        title=list_of_titles_keys[7]
    elif streak>=71 and streak<=90:
        title=list_of_titles_keys[8]
    elif streak>=91:
        title=list_of_titles_keys[9]

def get():
    dupli_title=False
    try:
        with open("Files/Titles/Titles.json", 'r') as title_import:
            title_import_data=json.load(title_import)
            title_import_data_list=list(title_import_data.keys())
            for k in title_import_data_list:
                if k==title:
                    dupli_title=True
    except:
        dupli_title=False

    if dupli_title==True:
        subprocess.Popen(['python', 'Anime Version/Title Exists/build/gui.py'])

    else:
        try:
            with open("Files/Titles/Titles.json", 'r') as title_import:
                title_import_data=json.load(title_import)
        except:
            title_import_data={}
        
        title_import_data[title]=list_of_titles_data[title]
        
        with open("Files/Titles/Titles.json", 'w') as final_title_import:
            json.dump(title_import_data, final_title_import, indent=4)

    with open("Files/Status.json", 'w') as status_import:
        rank_check_data["status"][0]['coins']+=coins
        rank_check_data["avail_eq"][0]['str_based']+=av_str
        rank_check_data["avail_eq"][0]['int_based']+=av_int
        rank_check_data["status"][0]['XP']+=xp_pl
        json.dump(rank_check_data, status_import, indent=4)

    with open("Files/Checks/Daily_time_check.csv", 'w', newline='') as Daily_date_check_file:
        fw=csv.writer(Daily_date_check_file)
        fw.writerow([today_date_str, "True"])

    subprocess.Popen(['python', 'Anime Version/Status Tab/build/gui.py'])
    window.quit()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 669,
    width = 555,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    277.0,
    478.0,
    image=image_image_1
)

video_path = "Files/0001-0200.mp4"
player = VideoPlayer(canvas, video_path, 277.0, 380.0)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    287.0,
    364.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    286.0,
    175.0,
    image=image_image_3
)

canvas.create_text(
    125.0,
    232.0,
    anchor="nw",
    text="You’ve got rewards! Congratulations",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_rectangle(
    105.0,
    291.0,
    468.0,
    317.0,
    fill="#272727",
    outline="")

canvas.create_text(
    105.0,
    293.0,
    anchor="nw",
    text=f" 1. +{av_str} STR Type Ability Points",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_rectangle(
    105.0,
    333.0,
    468.0,
    359.0,
    fill="#272727",
    outline="")

canvas.create_text(
    105.0,
    335.0,
    anchor="nw",
    text=f" 2. +{av_int} INT Type Ability Points",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_rectangle(
    105.0,
    375.0,
    468.0,
    401.0,
    fill="#272727",
    outline="")

canvas.create_text(
    105.0,
    377.0,
    anchor="nw",
    text=f" 3. +{xp_pl} XP",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_rectangle(
    105.0,
    417.0,
    468.0,
    443.0,
    fill="#272727",
    outline="")

canvas.create_text(
    105.0,
    419.0,
    anchor="nw",
    text=f" 4. {coins} Gold Coins",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_rectangle(
    105.0,
    459.0,
    468.0,
    485.0,
    fill="#FFF859",
    outline="")

canvas.create_rectangle(
    106.0,
    460.0,
    467.0,
    484.0,
    fill="#272727",
    outline="")

canvas.create_text(
    105.0,
    459.0,
    anchor="nw",
    text=f" 5. New Title: [{title}]",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    184.0,
    522.0,
    anchor="nw",
    text="Accept these rewards?",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=133.0,
    y=571.0,
    width=82.0,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=358.0,
    y=571.0,
    width=82.0,
    height=28.0
)

image_0=canvas.create_rectangle(
    0.0,
    0.0,
    570.0,
    35.0,
    fill="#212121",
    outline="")

canvas.tag_bind(image_0, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_0, "<B1-Motion>", move_window)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_0.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ex_close(window),
    relief="flat"
)
button_8.place(
    x=520.0,
    y=3.0,
    width=28.0,
    height=28.0
)

window.resizable(False, False)
window.mainloop()
