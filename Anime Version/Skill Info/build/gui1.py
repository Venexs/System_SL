
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import csv
import json
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def up():
    global screen_txt
    global av_txt
    screen_tr_txt=canvas_1.itemcget(screen_txt, "text")
    av_tr_txt=canvas_1.itemcget(av_txt, "text")
    if int(av_tr_txt)!=0:
        new=int(screen_tr_txt)+1
        be_new=f"{new:03d}"
        canvas_1.itemconfig(screen_txt, text=be_new)

        new_1=int(av_tr_txt)-1
        be_new_1=f"{new_1:03d}"
        canvas_1.itemconfig(av_txt, text=be_new_1)

def down():
    global screen_txt
    global av_txt
    screen_tr_txt=canvas_1.itemcget(screen_txt, "text")
    av_tr_txt=canvas_1.itemcget(av_txt, "text")
    if int(screen_tr_txt)!=0:
        new=int(screen_tr_txt)-1
        be_new=f"{new:03d}"
        canvas_1.itemconfig(screen_txt, text=be_new)

        new_1=int(av_tr_txt)+1
        be_new_1=f"{new_1:03d}"
        canvas_1.itemconfig(av_txt, text=be_new_1)

def confirm():
    global screen_txt
    global av_txt
    global pl_points
    screen_tr_txt=canvas_1.itemcget(screen_txt, "text")
    av_tr_txt=canvas_1.itemcget(av_txt, "text")
    got=int(screen_tr_txt)

    fin=pl_points+got
    fin_2=fin-get

    level_up=False
    if fin_2>0:
        pl_points=fin_2
        level_up=True
    else:
        pl_points=fin

    if base=='STR':
        status_data["avail_eq"][0]['str_based']=status_data["avail_eq"][0]['str_based']-int(screen_tr_txt)

    elif base=='INT':
        status_data["avail_eq"][0]['int_based']=status_data["avail_eq"][0]['int_based']-int(screen_tr_txt)

    with open("Files/status.json", 'w') as fin_status:
        json.dump(status_data, fin_status, indent=4)

    data_main[name][0]["pl_point"]=pl_points
    if level_up==True:
        data_main[name][0]["lvl"]=lvl+1

    with open("Files/Skills/Skill.json", 'w') as fin_skill:
        json.dump(data_main, fin_skill, indent=6)

    subprocess.Popen(['python', 'Anime Version/Skill Info/build/gui.py'])

    window.quit()

def goback():
    subprocess.Popen(['python', 'Anime Version/Skill Info/build/gui.py'])

    window.quit()

subprocess.Popen(['python', 'sfx.py'])

window = Tk()

window.geometry("450x163")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)

with open("Files/Temp Files/Skill Temp.csv", 'r') as csv_open:
    fr=csv.reader(csv_open)
    for k in fr:
        name=k[0]

with open("Files\Data\Skill_Up_Values.json", 'r') as fson:
    data=json.load(fson)

with open("Files/Skills/Skill.json", 'r') as fron:
    data_main=json.load(fron)
    data_main_key=list(data_main.keys())

    for k in data_main_key:
        if k==name:
            lvl=data_main[name][0]["lvl"]
            pl_points=data_main[name][0]["pl_point"]
            base=data_main[name][0]["base"]

get=data['Values'][0][str(lvl+1)]

with open("Files/status.json", 'r') as status:
    status_data=json.load(status)

    if base=='STR':
        av_data=status_data["avail_eq"][0]['str_based']
        naming="STR, AGI, VIT"

    elif base=='INT':
        av_data=status_data["avail_eq"][0]['int_based']
        naming="INT, PER, MAN"

    av_data=f"{av_data:03d}"

canvas_1 = Canvas(
    window,
    bg = "#FFFFFF",
    height = 163,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas_1.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas_1.create_image(
    225.0,
    81.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: goback(),
    relief="flat"
)
button_1.place(
    x=427.0,
    y=3.0,
    width=20.0,
    height=20.0
)

canvas_1.create_text(
    18.0,
    28.0,
    anchor="nw",
    text=f"SPEND AVAILABLE {naming} TYPE POINTS TO UPGRADE SKILL?",
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 12 * -1)
)

av_txt=canvas_1.create_text(
    398.0,
    128.0,
    anchor="nw",
    text=av_data,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 24 * -1)
)

canvas_1.create_rectangle(
    133.0,
    56.0,
    317.0,
    106.0,
    fill="#FFFFFF",
    outline="")

screen_txt=canvas_1.create_text(
    164.0,
    35.0,
    anchor="nw",
    text="000",
    fill="#000000",
    font=("Montserrat SemiBold", 60 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: down(),
    relief="flat"
)
button_2.place(
    x=82.0,
    y=63.0,
    width=38.0,
    height=38.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: up(),
    relief="flat"
)
button_3.place(
    x=329.0,
    y=63.0,
    width=38.0,
    height=38.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: confirm(),
    relief="flat"
)
button_4.place(
    x=6.0,
    y=141.0,
    width=69.0,
    height=16.0
)
window.resizable(False, False)
window.mainloop()