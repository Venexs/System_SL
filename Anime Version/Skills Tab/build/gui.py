
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("548x314")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)

def passive():
    subprocess.Popen(['python', 'Anime Version/Skills Tab/build/gui4.py'])

    window.quit()

def active():
    subprocess.Popen(['python', 'Anime Version/Skills Tab/build/gui1.py'])

    window.quit()

def job():
    subprocess.Popen(['python', 'Anime Version/Skills Tab/build/gui3.py'])

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
    282.0,
    66.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: passive(),
    relief="flat"
)
button_1.place(
    x=52.0,
    y=110.0,
    width=459.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: active(),
    relief="flat"
)
button_2.place(
    x=52.0,
    y=164.0,
    width=459.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: job(),
    relief="flat"
)
button_3.place(
    x=52.0,
    y=218.0,
    width=459.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()