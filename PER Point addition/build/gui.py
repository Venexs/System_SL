
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\System\PER Point addition\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("881x243")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 243,
    width = 881,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    516.0,
    277.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    440.0,
    131.99999999999991,
    image=image_image_2
)

canvas.create_text(
    329.0,
    36.0,
    anchor="nw",
    text="NOTIFICATION",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    219.0,
    84.0,
    anchor="nw",
    text="To increase your PER skill, Take the test on this",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    293.0,
    108.0,
    anchor="nw",
    text="page and enter your score here",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
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
    x=315.0,
    y=190.0,
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
    x=484.0,
    y=190.0,
    width=82.0,
    height=28.0
)

canvas.create_rectangle(
    118.0,
    227.0,
    762.0,
    232.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    313.0,
    70.0,
    567.0,
    75.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    116.0,
    31.0,
    762.0,
    36.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    441.0,
    160.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=273.0,
    y=139.0,
    width=336.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
