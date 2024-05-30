
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

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH1 = OUTPUT_PATH / Path(r"assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)


window = Tk()

window.geometry("548x314")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)

name1=name2=name3=name4=name5=name6='-'
lvl1=lvl2=lvl3=lvl4=lvl5=lvl6='??'

with open("Files\Skills\Skill.json", 'r') as fson:
    c=0
    try:
        data=json.load(fson)
        data_key=list(data.keys())
        for k in data_key:
            if data[k][0]["type"]=='Active':
                if c==0:
                    name1=k
                    lvl1=data[k][0]["lvl"]
                    c+=1
                elif c==1:
                    name2=k
                    lvl2=data[k][0]["lvl"]
                    c+=1
                elif c==2:
                    name3=k
                    lvl3=data[k][0]["lvl"]
                    c+=1
                elif c==3:
                    name4=k
                    lvl4=data[k][0]["lvl"]
                    c+=1
                elif c==4:
                    name5=k
                    lvl5=data[k][0]["lvl"]
                    c+=1
                elif c==5:
                    name6=k
                    lvl6=data[k][0]["lvl"]
                    c+=1
    except:
        print()

def open_prog(name):
    if name!='-':
        with open("Files/Temp Files/Skill Temp.csv", 'w', newline='') as csv_open:
            fw=csv.writer(csv_open)
            rec=[name]
            fw.writerow(rec)

        subprocess.Popen(['python', 'Anime Version/Skill Info/build/gui.py'])

        window.quit()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 314,
    width = 548,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    603.0,
    447.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    280.0,
    435.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    196.0,
    62.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    281.0,
    279.0,
    image=image_image_4
)

canvas.create_text(
    69.0,
    268.0,
    anchor="nw",
    text=name6,
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    407.0,
    268.0,
    anchor="nw",
    text=f"Lvl.{lvl6}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_prog(name6),
    relief="flat"
)
button_1.place(
    x=481.0,
    y=267.0,
    width=24.0,
    height=24.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    281.0,
    247.0,
    image=image_image_5
)

canvas.create_text(
    69.0,
    236.0,
    anchor="nw",
    text=name5,
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    407.0,
    236.0,
    anchor="nw",
    text=f"Lvl.{lvl5}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_prog(name5),
    relief="flat"
)
button_2.place(
    x=481.0,
    y=235.0,
    width=24.0,
    height=24.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    281.0,
    215.0,
    image=image_image_6
)

canvas.create_text(
    69.0,
    204.0,
    anchor="nw",
    text=name4,
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    407.0,
    204.0,
    anchor="nw",
    text=f"Lvl.{lvl4}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_prog(name4),
    relief="flat"
)
button_3.place(
    x=481.0,
    y=203.0,
    width=24.0,
    height=24.0
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    281.0,
    183.0,
    image=image_image_7
)

canvas.create_text(
    69.0,
    172.0,
    anchor="nw",
    text=name3,
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    407.0,
    172.0,
    anchor="nw",
    text=f"Lvl.{lvl3}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_prog(name3),
    relief="flat"
)
button_4.place(
    x=481.0,
    y=171.0,
    width=24.0,
    height=24.0
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    281.0,
    151.0,
    image=image_image_8
)

canvas.create_text(
    69.0,
    140.0,
    anchor="nw",
    text=name2,
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    407.0,
    140.0,
    anchor="nw",
    text=f"Lvl.{lvl2}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_prog(name2),
    relief="flat"
)
button_5.place(
    x=481.0,
    y=139.0,
    width=24.0,
    height=24.0
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    281.0,
    119.0,
    image=image_image_9
)

canvas.create_text(
    69.0,
    108.0,
    anchor="nw",
    text=name1,
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    407.0,
    108.0,
    anchor="nw",
    text=f"Lvl.{lvl1}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_prog(name1),
    relief="flat"
)
button_6.place(
    x=481.0,
    y=107.0,
    width=24.0,
    height=24.0
)
window.resizable(False, False)
window.mainloop()