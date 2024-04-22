
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import json
import csv
import subprocess

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("957x555")
window.configure(bg = "#FFFFFF")

window.attributes('-alpha',0.8)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 555,
    width = 957,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    478.0,
    277.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    477.0,
    288.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    483.0,
    91.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    483.0,
    234.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    483.0,
    379.0,
    image=image_image_5
)


# ? =====================================================================
# ? =====================================================================

with open("Files/status.json", 'r') as fson:
    data=json.load(fson)
    hp=data["status"][0]['hp']
    mp=data["status"][0]['mp']
    lvl=data["status"][0]['level']
    stre=data["status"][0]['str']
    intel=data["status"][0]['int']
    agi=data["status"][0]['agi']
    vit=data["status"][0]['vit']
    per=data["status"][0]['per']
    man=data["status"][0]['man']

    tit=data["status"][1]['title']
    job=data["status"][1]['job']

    av_str_based=data["avail_eq"][0]['str_based']
    av_int_based=data["avail_eq"][0]['int_based']
# ? =====================================================================
# ? =====================================================================

# / =================================================
# / =================================================

def update_str():
    if int(av_str_based)!=0:
        global str_txt
        current_text = canvas.itemcget(str_txt, "text")
        # ? ====================================================
        current_number = int(current_text)
        new_number = current_number + 1
        # ? ====================================================
        with open("Files/status.json", 'w') as fson:
            data["status"][0]['str']+=1
            data["avail_eq"][0]['str_based']-=1
            json.dump(data, fson, indent=4)
        # ? ====================================================
        new_text = f"{new_number:03d}"
        canvas.itemconfig(str_txt, text=new_text)

        de_update_str()

def update_agi():
    if int(av_str_based)!=0:
        global agi_txt
        current_text = canvas.itemcget(agi_txt, "text")
         # ? ====================================================
        current_number = int(current_text)
        new_number = current_number + 1
        # ? ====================================================
        with open("Files/status.json", 'w') as fson:
            data["status"][0]['agi']+=1
            data["avail_eq"][0]['str_based']-=1
            json.dump(data, fson, indent=4)
        # ? ====================================================
        new_text = f"{new_number:03d}"
        canvas.itemconfig(agi_txt, text=new_text)

        de_update_str()

def update_vit():
    if int(av_str_based)!=0:
        global vit_txt
        current_text = canvas.itemcget(vit_txt, "text")
         # ? ====================================================
        current_number = int(current_text)
        new_number = current_number + 1
        # ? ====================================================
        with open("Files/status.json", 'w') as fson:
            data["status"][0]['vit']+=1
            data["avail_eq"][0]['str_based']-=1
            json.dump(data, fson, indent=4)
        # ? ====================================================
        new_text = f"{new_number:03d}"
        canvas.itemconfig(vit_txt, text=new_text)

        de_update_str()

def update_int():
    if int(av_int_based)!=0:
        global int_txt
        current_text = canvas.itemcget(int_txt, "text")
         # ? ====================================================
        current_number = int(current_text)
        new_number = current_number + 1
        # ? ====================================================
        with open("Files/status.json", 'w') as fson:
            data["status"][0]['int']+=1
            data["avail_eq"][0]['int_based']-=1
            json.dump(data, fson, indent=4)
        # ? ====================================================
        new_text = f"{new_number:03d}"
        canvas.itemconfig(int_txt, text=new_text)

        de_update_int()

def update_per():
    if int(av_int_based)!=0:
        global per_txt
        current_text = canvas.itemcget(per_txt, "text")
         # ? ====================================================
        current_number = int(current_text)
        new_number = current_number + 1 
        # ? ====================================================
        with open("Files/status.json", 'w') as fson:
            data["status"][0]['per']+=1
            data["avail_eq"][0]['int_based']-=1
            json.dump(data, fson, indent=4)
        # ? ====================================================
        new_text = f"{new_number:03d}"
        canvas.itemconfig(per_txt, text=new_text)

        de_update_int()

def update_man():
    if int(av_int_based)!=0:
        global man_txt
        current_text = canvas.itemcget(man_txt, "text")
         # ? ====================================================
        current_number = int(current_text)
        new_number = current_number + 1
        # ? ====================================================
        with open("Files/status.json", 'w') as fson:
            data["status"][0]['man']+=1
            data["avail_eq"][0]['int_based']-=1
            json.dump(data, fson, indent=4)
        # ? ====================================================
        new_text = f"{new_number:03d}"
        canvas.itemconfig(man_txt, text=new_text)

        de_update_int()

# / =================================================
# / =================================================

def de_update_str():
    global av_str_based_txt
    current_text = canvas.itemcget(av_str_based_txt, "text")
    current_number = int(current_text)
    new_number = current_number - 1
    new_text = f"{new_number:03d}"
    canvas.itemconfig(av_str_based_txt, text=new_text)

def de_update_int():
    global av_int_based_txt
    current_text = canvas.itemcget(av_int_based_txt, "text")
    current_number = int(current_text)
    new_number = current_number - 1
    new_text = f"{new_number:03d}"
    canvas.itemconfig(av_int_based_txt, text=new_text)

# / =================================================
# / =================================================


canvas.create_text(
    395.0,
    168.0,
    anchor="nw",
    text="LEVEL",
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    391.0,
    111.0,
    anchor="nw",
    text=lvl,
    fill="#FFFFFF",
    font=("Montserrat Bold", 55 * -1)
)

av_str_based_txt=canvas.create_text(
    815.0,
    61.0,
    anchor="nw",
    text=av_str_based,
    fill="#FFFFFF",
    font=("Montserrat Bold", 24 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("Av1.png"))
image_7 = canvas.create_image(
    748.0,
    150.0,
    image=image_image_7
)

av_int_based_txt=canvas.create_text(
    815.0,
    130.0,
    anchor="nw",
    text=av_int_based,
    fill="#FFFFFF",
    font=("Montserrat Bold", 24 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("Av2.png"))
image_8 = canvas.create_image(
    748.0,
    80.0,
    image=image_image_8
)

# ? ==========================================================
# ? STR Ability points
# ? ==========================================================

str_txt=canvas.create_text(
    366.0,
    311.0,
    anchor="nw",
    text=stre,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    409.0,
    314.0,
    anchor="nw",
    text="(+20)",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

# ? ==========================================================
# ? INT Ability points
# ? ==========================================================

int_txt=canvas.create_text(
    366.0,
    365.0,
    anchor="nw",
    text=intel,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    409.0,
    368.0,
    anchor="nw",
    text="(+20)",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

# ? ==========================================================
# ? AGI Ability points
# ? ==========================================================

agi_txt=canvas.create_text(
    366.0,
    417.0,
    anchor="nw",
    text=agi,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    410.0,
    420.0,
    anchor="nw",
    text="(+20)",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

# ? ==========================================================
# ? VIT Ability points
# ? ==========================================================

vit_txt=canvas.create_text(
    603.0,
    311.0,
    anchor="nw",
    text=vit,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    640.0,
    314.0,
    anchor="nw",
    text="(+20)",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

# ? ==========================================================
# ? PER Ability points
# ? ==========================================================

per_txt=canvas.create_text(
    609.0,
    363.0,
    anchor="nw",
    text=per,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    653.0,
    366.0,
    anchor="nw",
    text="(+20)",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

# ? ==========================================================
# ? MAN Ability points
# ? ==========================================================

man_txt=canvas.create_text(
    612.0,
    419.0,
    anchor="nw",
    text=man,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

# ? ==========================================================
# ? JOB and TITLE
# ? ==========================================================

canvas.create_text(
    501.0,
    140.0,
    anchor="nw",
    text="JOB:",
    fill="#FFFFFF",
    font=("Montserrat Regular", 14 * -1)
)

canvas.create_text(
    546.0,
    137.0,
    anchor="nw",
    text=job,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 18 * -1)
)

canvas.create_text(
    501.0,
    169.0,
    anchor="nw",
    text="TITLE:",
    fill="#FFFFFF",
    font=("Montserrat Regular", 14 * -1)
)

canvas.create_text(
    546.0,
    166.0,
    anchor="nw",
    text=tit,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 18 * -1)
)

# ! ==========================================================

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    332.0,
    325.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    330.0,
    379.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    331.0,
    433.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    562.0,
    325.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    567.0,
    376.0,
    image=image_image_13
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    571.0,
    432.0,
    image=image_image_16
)

# ? ==========================================================
# ? HP and MP points
# ? ==========================================================


image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    297.0,
    232.0,
    image=image_image_14
)

canvas.create_text(
    317.0,
    223.0,
    anchor="nw",
    text=f"{hp}/",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

canvas.create_text(
    366.0,
    228.0,
    anchor="nw",
    text=f"{hp}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 12 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    575.0,
    232.0,
    image=image_image_15
)

canvas.create_text(
    595.0,
    223.0,
    anchor="nw",
    text=f"{mp}/",
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

canvas.create_text(
    644.0,
    228.0,
    anchor="nw",
    text=f"{mp}",
    fill="#FFFFFF",
    font=("Montserrat Medium", 12 * -1)
)

# ? ==========================================================
# ? Ability Add Up Button
# ? ==========================================================

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_str,
    relief="flat"
)
button_1.place(
    x=456.0,
    y=314.0,
    width=20.954654693603516,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_int,
    relief="flat"
)
button_2.place(
    x=457.0,
    y=368.0,
    width=20.954654693603516,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_agi,
    relief="flat"
)
button_3.place(
    x=457.0,
    y=420.0,
    width=20.954654693603516,
    height=20.0
)

# ? ==========================================================
# ? Ability Level Up Button
# ? ==========================================================

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=277.0,
    y=315.0,
    width=20.0,
    height=20.000003814697266
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=279.0,
    y=370.0,
    width=20.0,
    height=20.000001907348633
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=278.0,
    y=423.0,
    width=20.0,
    height=20.000001907348633
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=509.0,
    y=368.0,
    width=20.0,
    height=20.000001907348633
)
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=690.0,
    y=313.0,
    width=20.954654693603516,
    height=20.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=695.0,
    y=365.0,
    width=20.954654693603516,
    height=20.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=685.0,
    y=421.0,
    width=20.954654693603516,
    height=20.0
)
window.resizable(False, False)
window.mainloop()
