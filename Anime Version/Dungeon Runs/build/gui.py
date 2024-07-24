
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import json
import csv
import subprocess
import random
import cv2
from PIL import Image, ImageTk
from datetime import datetime, timedelta

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("804x369")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.overrideredirect(True)
window.wm_attributes("-topmost", True)

waves={}
XP_val=0
mob=1
rank='X'
rew_rank='X'

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

def rank_get(rank,amt1,amt1_check):
    if rank=='D':
        if amt1_check=="amt":
            if amt1==50:
                amt1+=10
            elif amt1==15:
                amt1+=5
            elif amt1==2:
                amt1+=1
            elif amt1==30:
                amt1+=15
            elif amt1==1:
                amt1+=1
        elif amt1_check=="time":
            if amt1==45:
                amt1+=15
            elif amt1==60:
                amt1+=60
            elif amt1==1:
                amt1+=1
    elif rank=='C':
        if amt1_check=="amt":
            if amt1==50:
                amt1+=20
            elif amt1==15:
                amt1+=15
            elif amt1==2:
                amt1+=2
            elif amt1==30:
                amt1+=30
            elif amt1==1:
                amt1+=2
        elif amt1_check=="time":
            if amt1==45:
                amt1+=30
            elif amt1==60:
                amt1+=120
            elif amt1==1:
                amt1+=2
    elif rank=='B':
        if amt1_check=="amt":
            if amt1==50:
                amt1+=30
            elif amt1==15:
                amt1+=35
            elif amt1==2:
                amt1+=3
            elif amt1==30:
                amt1+=60
            elif amt1==1:
                amt1+=3
        elif amt1_check=="time":
            if amt1==45:
                amt1+=45
            elif amt1==60:
                amt1+=240
            elif amt1==1:
                amt1+=4
    elif rank=='A':
        if amt1_check=="amt":
            if amt1==50:
                amt1+=100
            elif amt1==15:
                amt1+=50
            elif amt1==2:
                amt1+=5
            elif amt1==30:
                amt1+=70
            elif amt1==1:
                amt1+=4
        elif amt1_check=="time":
            if amt1==45:
                amt1+=65
            elif amt1==60:
                amt1+=360
            elif amt1==1:
                amt1+=6
    elif rank=='S':
        if amt1_check=="amt":
            if amt1==50:
                amt1+=150
            elif amt1==15:
                amt1+=85
            elif amt1==2:
                amt1+=8
            elif amt1==30:
                amt1+=90
            elif amt1==1:
                amt1+=5
        elif amt1_check=="time":
            if amt1==45:
                amt1+=75
            elif amt1==60:
                amt1+=540
            elif amt1==1:
                amt1+=9

    return amt1

def get_act():
    global activity1
    global activity2
    global activity3
    global activity4
    
    # Activities
    str_file_name=f"Files\Workout\STR_based.json"
    with open(str_file_name, 'r') as str_quest_file_name:
        str_quest_main_names=json.load(str_quest_file_name)

    str_quest_main_names_list=list(str_quest_main_names.keys())

    act1=random.choice(str_quest_main_names_list)
    act2=random.choice(str_quest_main_names_list)

    try:
        amt1=str_quest_main_names[act1][0]["amt"]
        amtval1=str_quest_main_names[act1][0]["amtval"]
        amt1_check="amt"
    except:
        amt1=str_quest_main_names[act1][0]["time"]
        amtval1=str_quest_main_names[act1][0]["timeval"]
        amt1_check="time"
    
    try:
        amt2=str_quest_main_names[act2][0]["amt"]
        amtval2=str_quest_main_names[act2][0]["amtval"]
        amt2_check="amt"
    except:
        amt2=str_quest_main_names[act2][0]["time"]
        amtval2=str_quest_main_names[act2][0]["timeval"]
        amt2_check="time"
    
    amt1=rank_get(rank, amt1, amt1_check)
    amt2=rank_get(rank, amt2, amt2_check)

    agi_file_name=f"Files\Workout\AGI_based.json"
    with open(agi_file_name, 'r') as agi_quest_file_name:
        agi_quest_main_names=json.load(agi_quest_file_name)

    agi_quest_main_names_list=list(agi_quest_main_names.keys())

    act3=random.choice(agi_quest_main_names_list)
    act4=random.choice(agi_quest_main_names_list)

    try:
        amt3=agi_quest_main_names[act3][0]["amt"]
        amtval3=agi_quest_main_names[act3][0]["amtval"]
        amt3_check="amt"
    except:
        amt3=agi_quest_main_names[act3][0]["time"]
        amtval3=agi_quest_main_names[act3][0]["timeval"]
        amt3_check="time"
    
    try:
        amt4=agi_quest_main_names[act4][0]["amt"]
        amtval4=agi_quest_main_names[act4][0]["amtval"]
        amt4_check="amt"
    except:
        amt4=agi_quest_main_names[act4][0]["time"]
        amtval4=agi_quest_main_names[act4][0]["timeval"]
        amt4_check="time"

    amt3=rank_get(rank, amt3, amt3_check)
    amt4=rank_get(rank, amt4, amt4_check)

    full_act1_name=act1+' '+str(amt1)+' '+amtval1
    full_act2_name=act2+' '+str(amt2)+' '+amtval2
    full_act3_name=act3+' '+str(amt3)+' '+amtval3
    full_act4_name=act4+' '+str(amt4)+' '+amtval4

    canvas.itemconfig(activity1, text=full_act1_name)
    canvas.itemconfig(activity2, text=full_act2_name)
    canvas.itemconfig(activity3, text=full_act3_name)
    canvas.itemconfig(activity4, text=full_act4_name)

def get():
    global waves
    global XP_val
    global rank
    global rew_rank

    with open("Files\Data\Dungeon_Rank.csv", 'r') as rank_file:
        rank_file_reader=csv.reader(rank_file)
        for k in rank_file_reader:
            rank=k[0]
            rew_rank=rank

    if rank!="Red":
        global rank
        global mob

        if mob==3:
            if rank=='E':rank='D'
            elif rank=='D':rank='C'
            elif rank=='C':rank='B'
            elif rank=='B':rank='A'
            elif rank=='A':rank='S'
        
        # Waves
        with open("Files\Data\Dungeon_Boss_List.json", 'r') as monster_file:
            monster_file_data=json.load(monster_file)
            monster_names=list(monster_file_data.keys())

            waves={}
            monsters={}
            bosses={}
            for k in monster_names:
                if monster_file_data[k]["rank"]==rank and monster_file_data[k]["type"]=='Normal':
                    monsters[k]=monster_file_data[k]

            mob1=random.choice(list(monsters.keys()))
            mob2=random.choice(list(monsters.keys()))

            waves['1']={mob1:monster_file_data[mob1]}
            waves['2']={mob1:monster_file_data[mob2]}

            XP_val+=monster_file_data[mob1]['XP']
            XP_val+=monster_file_data[mob2]['XP']

            if rank=='E': boss_rank='D'
            elif rank=='D': boss_rank='C'
            elif rank=='C': boss_rank='B'
            elif rank=='B': boss_rank='A'
            elif rank=='A': boss_rank='S'
            elif rank=='S': boss_rank='S'

            for k in monster_names:
                if monster_file_data[k]["rank"]==boss_rank and monster_file_data[k]["type"]=='Boss':
                    bosses[k]=monster_file_data[k]

            boss=random.choice(list(bosses.keys()))

            waves['Final']={boss:monster_file_data[boss]}
            XP_val+=monster_file_data[boss]['XP']

            get_act()
            mob_fun()

def mob_fun():
    global mob

    mob_num=str(mob)
    name=list(waves[mob_num])[0]
    if waves[mob_num][name]['swarm']=='Yes':
        group="Group"
    else:
        group="Swarm"
    wave_text=f"[Wave - 0{mob_num}]"
    group_txt=f"A {group} of {name} has appeared in front of you. "
    canvas.itemconfig(waves_txt, text=wave_text)
    canvas.itemconfig(enemy, text=group_txt)
    get_act()

def next():
    global mob
    global XP_val
    global rank
    global rew_rank

    mob+=1

    if mob==4:
        with open("Files/Status.json", 'r') as status_read_file:
            status_read_data=json.load(status_read_file)

        if rew_rank=='E':
            coin=100
            avp=1
        elif rew_rank=='D':
            coin=500
            avp=2
        elif rew_rank=='C':
            coin=1000
            avp=3
        elif rew_rank=='B':
            coin=5000
            avp=4
        elif rew_rank=='A':
            coin=10000
            avp=5
        elif rew_rank=='S':
            coin=20000
            avp=6

        status_read_data["status"][0]['XP']+=XP_val
        status_read_data["avail_eq"][0]['coins']+=coin
        status_read_data["avail_eq"][0]['str_based']+=avp
        status_read_data["avail_eq"][0]['int_based']+=avp

        with open("Files/status.json", 'w') as fson:
            json.dump(status_read_data, fson, indent=4)

        subprocess.Popen(['python', 'Anime Version/Dungeon Rewards/build/gui.py'])
        window.quit()

    else:
        subprocess.Popen(['python', 'sfx_glitch.py'])
        mob_fun()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 369,
    width = 804,
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
player = VideoPlayer(canvas, video_path, 478.0, 213.0)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    400.0,
    195.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    162.0,
    71.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ex_close(window),
    relief="flat"
)
button_1.place(
    x=614.0,
    y=327.0,
    width=127.0,
    height=22.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: next(),
    relief="flat"
)
button_2.place(
    x=591.0,
    y=296.0,
    width=150.0,
    height=22.0
)

canvas.create_text(
    28.0,
    98.0,
    anchor="nw",
    text=f"{rank}-Rank Dungeon",
    fill="#FFFFFF",
    font=("Montserrat Bold", 13 * -1)
)

waves_txt=canvas.create_text(
    52.0,
    132.0,
    anchor="nw",
    text="[Wave - XX]",
    fill="#FFFFFF",
    font=("Montserrat Medium", 14 * -1)
)

enemy=canvas.create_text(
    52.0,
    162.0,
    anchor="nw",
    text="A [group] of [Normal Enemy-1] has appeared in front of you. ",
    fill="#FFFFFF",
    font=("Montserrat Medium", 14 * -1)
)

canvas.create_text(
    52.0,
    182.0,
    anchor="nw",
    text="Do the activities below to generate enough [STR/AGI] to defeat them",
    fill="#FFFFFF",
    font=("Montserrat Medium", 14 * -1)
)

activity1=canvas.create_text(
    72.0,
    214.0,
    anchor="nw",
    text="-Activity 0",
    fill="#FFFFFF",
    font=("Montserrat Regular", 14 * -1)
)

activity2=canvas.create_text(
    72.0,
    234.0,
    anchor="nw",
    text="-Activity 1",
    fill="#FFFFFF",
    font=("Montserrat Regular", 14 * -1)
)

activity3=canvas.create_text(
    72.0,
    254.0,
    anchor="nw",
    text="-Activity 2",
    fill="#FFFFFF",
    font=("Montserrat Regular", 14 * -1)
)

activity4=canvas.create_text(
    72.0,
    274.0,
    anchor="nw",
    text="-Activity 3",
    fill="#FFFFFF",
    font=("Montserrat Regular", 14 * -1)
)

canvas.create_text(
    584.0,
    63.0,
    anchor="nw",
    text="Time Left:",
    fill="#FFFFFF",
    font=("Montserrat Regular", 12 * -1)
)

canvas.create_text(
    584.0,
    75.0,
    anchor="nw",
    text="00:00:00",
    fill="#FFFFFF",
    font=("Montserrat Bold", 32 * -1)
)

image_0=canvas.create_rectangle(
    0.0,
    0.0,
    804.0,
    33.0,
    fill="#262626",
    outline="")

canvas.tag_bind(image_0, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_0, "<B1-Motion>", move_window)
get()
window.resizable(False, False)
window.mainloop()
