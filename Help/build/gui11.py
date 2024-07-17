
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import webbrowser
import json
import cv2
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame11")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

subprocess.Popen(['python', 'sfx.py'])

window = Tk()

window.geometry("391x676")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.overrideredirect(True)
window.wm_attributes("-topmost", True)

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

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 676,
    width = 391,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def name():
    name_txt=entry_1.get()
    with open("Files/status.json", 'r') as first_fson:
        data=json.load(first_fson)
        data["status"][0]['name']=name_txt
    
    with open("Files/status.json", 'w') as fson:
        json.dump(data, fson, indent=4)

    subprocess.Popen(['python', 'Anime Version/Penalty Check/build/gui.py'])
    window.quit()

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    478.0,
    350.0,
    image=image_image_1
)

video_path = "Files/0001-0200.mp4"
player = VideoPlayer(canvas, video_path, 478.0, 350.0)

canvas.create_rectangle(
    14.0,
    56.0,
    378.0,
    655.0,
    fill="#262626",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    196.0000047683714,
    352.00001883506775,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    196.0,
    99.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    748.0,
    80.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    201.0,
    172.0,
    image=image_image_5
)

canvas.create_text(
    54.0,
    245.0,
    anchor="nw",
    text="SELECT YOUR PREFERRED THEME",
    fill="#FFFFFF",
    font=("Exo Bold", 18 * -1)
)

canvas.create_text(
    52.0,
    483.0,
    anchor="nw",
    text="CONSIDER SUPPORTING ME HERE!",
    fill="#FFFFFF",
    font=("Exo Bold", 18 * -1)
)

canvas.create_text(
    24.0,
    129.0,
    anchor="nw",
    text="ENTER INFORMATION",
    fill="#FF7325",
    font=("Exo Bold", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: name(),
    relief="flat"
)
button_1.place(
    x=31.0,
    y=605.0,
    width=30.0,
    height=30.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    195.0,
    216.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=26.0,
    y=202.0,
    width=338.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: name(),
    relief="flat"
)
button_2.place(
    x=32.0,
    y=276.0,
    width=140.0,
    height=159.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=219.0,
    y=276.0,
    width=140.0,
    height=159.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(),
    relief="flat"
)
button_4.place(
    x=25.0,
    y=510.0,
    width=166.0,
    height=51.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://discord.gg/dYCqGZkJAe"),
    relief="flat"
)
button_5.place(
    x=198.0,
    y=510.0,
    width=166.0,
    height=51.0
)

image_0=canvas.create_rectangle(
    0.0,
    0.0,
    391.0,
    35.0,
    fill="#212121",
    outline="")

canvas.tag_bind(image_0, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_0, "<B1-Motion>", move_window)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ex_close(window),
    relief="flat"
)
button_8.place(
    x=358.0,
    y=3.0,
    width=28.0,
    height=28.0
)
window.resizable(False, False)
window.mainloop()
