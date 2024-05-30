
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

subprocess.Popen(['python', 'sfx.py'])

window = Tk()

window.geometry("391x676")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 676,
    width = 391,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    478.0,
    350.0,
    image=image_image_1
)

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
    197.0,
    363.0,
    image=image_image_5
)

canvas.create_text(
    25.0,
    136.0,
    anchor="nw",
    text="MAIN SKILLS TAB",
    fill="#FF7325",
    font=("Exo Bold", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (subprocess.Popen(['python', 'Help/build/gui9.py']), window.quit()),
    relief="flat"
)
button_1.place(
    x=329.0,
    y=605.0,
    width=30.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (subprocess.Popen(['python', 'Help/build/gui7.py']), window.quit()),
    relief="flat"
)
button_2.place(
    x=31.0,
    y=605.0,
    width=30.0,
    height=30.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    195.0,
    302.0,
    image=image_image_6
)
window.resizable(False, False)
window.mainloop()
