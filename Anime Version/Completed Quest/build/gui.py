
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import winsound
import subprocess
subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("957x555")
window.configure(bg = "#FFFFFF")


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

canvas.create_rectangle(
    65.97630000671052,
    40.0,
    82.0,
    506.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    851.9762473400588,
    30.0,
    868.0,
    497.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    483.0,
    282.9999999999999,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    326.0,
    132.0,
    image=image_image_3
)

canvas.create_text(
    358.0,
    108.0,
    anchor="nw",
    text="NOTIFICATION",
    fill="#FFFFFF",
    font=("Inter SemiBold", 40 * -1)
)

canvas.create_text(
    212.0,
    232.0,
    anchor="nw",
    text="You have already completed todays STR based Quest",
    fill="#FFFFFF",
    font=("Inter", 21 * -1)
)
window.resizable(False, False)
window.mainloop()
