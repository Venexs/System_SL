
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import csv
import subprocess
import winsound

subprocess.Popen(['python', 'sfx.py'])
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\System\Inventory Addition\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("555x957")
window.configure(bg = "#FFFFFF")

def close():
   #win.destroy()
   subprocess.Popen(['python', 'Inventory/build/gui.py'])
   window.quit()

def get_record():
    global entry_1
    global entry_2
    global entry_3
    global entry_4
    global entry_5
    
    name=entry_1.get()
    qty=entry_2.get()
    rank=entry_3.get()
    cat=entry_4.get()
    desc=entry_5.get()

    fin=open('Files/Inventory.csv', 'a', newline='')
    fw=csv.writer(fin)
    rec=[name,qty,rank,cat,desc]
    fw.writerow(rec)

    fin.close()

    close()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 957,
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

canvas.create_rectangle(
    0.0,
    866.9999999999999,
    539.0,
    883.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    87.0,
    520.9990367889404,
    103.98248827329371,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    286.9999999999999,
    483.9999999999999,
    image=image_image_2
)

canvas.create_text(
    201.0,
    166.0,
    anchor="nw",
    text="Add Items to your inventory",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    195.0,
    216.0,
    anchor="nw",
    text="The Ranks and other details\n",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    144.0,
    231.0,
    anchor="nw",
    text=" of these Items have to be truthfully entered",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    193.0,
    245.0,
    anchor="nw",
    text="Or, a Penalty may be applied",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    203.0,
    687.0,
    anchor="nw",
    text="Add to Inventory?",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    172.0,
    129.0,
    anchor="nw",
    text="Inventory Addition",
    fill="#FFFFFF",
    font=("Inter Medium", 26 * -1)
)

canvas.create_rectangle(
    170.0,
    157.0,
    399.0,
    160.0000000660591,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    38.0,
    264.0,
    519.0,
    267.00000014149407,
    fill="#FFFFFF",
    outline="")

# ============================================================

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    276.5,
    333.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=121.0,
    y=319.0,
    width=311.0,
    height=26.0
)

canvas.create_text(
    120.0,
    294.0,
    anchor="nw",
    text="Name of Item:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

# ============================================================

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    277.5,
    399.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=122.0,
    y=385.0,
    width=311.0,
    height=26.0
)

canvas.create_text(
    122.0,
    363.0,
    anchor="nw",
    text="Quantity:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

# ============================================================

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    277.5,
    465.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=122.0,
    y=451.0,
    width=311.0,
    height=26.0
)

canvas.create_text(
    122.0,
    429.0,
    anchor="nw",
    text="Rank:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

# ============================================================

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    277.5,
    537.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=122.0,
    y=523.0,
    width=311.0,
    height=26.0
)

canvas.create_text(
    122.0,
    495.0,
    anchor="nw",
    text="Category:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    286.5,
    614.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=74.0,
    y=600.0,
    width=425.0,
    height=26.0
)

canvas.create_text(
    74.0,
    573.0,
    anchor="nw",
    text="Description (Brief):",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_record,
    relief="flat"
)
button_1.place(
    x=98.0,
    y=749.0,
    width=81.0,
    height=34.5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=close,
    relief="flat"
)
button_2.place(
    x=380.0,
    y=749.0,
    width=81.0,
    height=34.5
)
window.resizable(False, False)
window.mainloop()
