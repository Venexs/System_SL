
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import json
import csv
import cv2
from PIL import Image, ImageTk
import random

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("481x417")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
#window.update()

class VideoPlayer:
    def __init__(self, canvas, video_path, x, y):
        self.canvas = canvas
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.x = x
        self.y = y
        self.image_id = self.canvas.create_image(self.x, self.y)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            # If the video has ended, reset the capture object
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        if ret:
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

ft=13

def fin():
    try:
        with open("Files/Quests/Active_Quests.json", 'r') as active_quests_file:
            activ_quests=json.load(active_quests_file)
            name_of_activ_quests=list(activ_quests.keys())
            activ_quests_vals=0
            for k in name_of_activ_quests:
                activ_quests_vals+=1
    except:
        name_of_activ_quests=[]
    
    if activ_quests_vals<13 and activ_quests_vals!=13:
        quest_name='-'+entry_1.get()
        quest_type=(entry_2.get()).upper()
        quest_obj=entry_3.get()
        quest_amt=entry_4.get()
        quest_amt_type=entry_5.get()
        rank=(entry_6.get()).upper()

        if rank not in ["E", "D", "C", "B", "A", "S"]:
            rank='E'

        if quest_type not in ["STR", "INT"]:
            quest_type="STR"

        if quest_type=='STR':
            rew3="STRav"
        elif quest_type=='INT':
            rew3="INTav"

        id_val=random.randrange(1,999999)

        with open("Files\Quests\Quest_Desc.json", 'r') as quest_desc_file:
            quest_desc=json.load(quest_desc_file)
            if rank in ["E", "D"]:
                desc_list=quest_desc["Easy"]
                findesc=random.choice(desc_list)
            elif rank in ["C", "B"]:
                desc_list=quest_desc["Intermediate"]
                findesc=random.choice(desc_list)
            elif rank in ["A", "S"]:
                desc_list=quest_desc["Hard"]
                findesc=random.choice(desc_list)

        # ? Rewards
        amt={
            "S":250000, 
            "A":130000,
            "B":80000,
            "C":5000,
            "D":500,
            "E":300
            }
        
        coinval=amt[rank]
        rew1=f"Coin Bag {coinval}"
        with open("Files\Data\Inventory_List.json", 'r') as rewards_name_file:
            reward_names=json.load(rewards_name_file)
            reward_names_list=list(reward_names.keys())

            final_rewards_list=[]
            for k in reward_names_list:
                if rank==reward_names[k][0]["rank"]:
                    final_rewards_list.append(k)
            
            rew2=random.choice(final_rewards_list)

        rew_dict={rew1:1, rew2:1}
        if rank in ["S"]:
            rew_dict["LVLADD"]=8
            rew_dict[rew3]=10
        elif rank in ["A"]:
            rew_dict["LVLADD"]=5
            rew_dict[rew3]=8
        elif rank in ["B"]:
            rew_dict["LVLADD"]=2
            rew_dict[rew3]=6


        detail=[{
            "desc":findesc,
            "amt":quest_amt,
            "amtval":quest_amt_type,
            "type":"Learn",
            "obj_desc":"Quest given by Player. No descriptino Availabke",
            "rank":rank,
            "ID": id_val,
            "Rewards":rew_dict,
            "skill":quest_obj
        }]

        activ_quests[quest_name]=detail

        with open("Files/Quests/Active_Quests.json", 'w') as fin_active_quest_file:
            json.dump(activ_quests, fin_active_quest_file, indent=6)

    else:
        subprocess.Popen(['python', 'Anime Version/Quests Filled/build/gui.py'])

    window.quit()

    subprocess.Popen(['python', 'Anime Version/Quests/build/gui.py'])

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 417,
    width = 481,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    552.0,
    326.0,
    image=image_image_1
)

video_path = "Files/0001-0200.mp4"
player = VideoPlayer(canvas, video_path, 277.0, 278.0)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    240.0,
    228.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    162.0,
    71.0,
    image=image_image_3
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat', ft)
)
entry_1.place(
    x=30.0,
    y=116.0,
    width=369.0,
    height=20.0
)

canvas.create_text(
    30.0,
    98.0,
    anchor="nw",
    text="Enter Quest Name:",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat', ft)
)
entry_2.place(
    x=30.0,
    y=166.0,
    width=71.0,
    height=20.0
)

canvas.create_text(
    30.0,
    148.0,
    anchor="nw",
    text="Enter Quest Type (STR or INT): ",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat', ft)
)
entry_3.place(
    x=30.0,
    y=216.0,
    width=171.0,
    height=20.0
)

canvas.create_text(
    30.0,
    198.0,
    anchor="nw",
    text="Quest Objective:",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat', ft)
)
entry_4.place(
    x=30.0,
    y=266.0,
    width=71.0,
    height=20.0
)

canvas.create_text(
    30.0,
    248.0,
    anchor="nw",
    text="Quest Amount:",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat', ft)
)
entry_5.place(
    x=182.0,
    y=266.0,
    width=71.0,
    height=20.0
)

canvas.create_text(
    182.0,
    248.0,
    anchor="nw",
    text="Quest Amount Type:",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    197.0,
    311.0,
    image=image_image_4
)

entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat', ft)
)
entry_6.place(
    x=28.0,
    y=348.0,
    width=71.0,
    height=20.0
)

canvas.create_text(
    28.0,
    330.0,
    anchor="nw",
    text="Quest Rank (E,D,C,B,A Or S) : ",
    fill="#FFFFFF",
    font=("Montserrat Medium", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fin(),
    relief="flat"
)
button_1.place(
    x=350.0,
    y=381.0,
    width=109.0,
    height=22.0
)

image_0=canvas.create_rectangle(
    0.0,
    0.0,
    486.0,
    33.0,
    fill="#262626",
    outline="")

canvas.tag_bind(image_0, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_0, "<B1-Motion>", move_window)

button_image_0 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_0 = Button(
    image=button_image_0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ex_close(window),
    relief="flat"
)
button_0.place(
    x=453.0,
    y=2.0,
    width=28.0,
    height=28.0
)

window.resizable(False, False)
window.mainloop()
