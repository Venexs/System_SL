
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"INT Daily Quest Rewards\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("555x957")
window.configure(bg = "#FFFFFF")


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
    215.0,
    266.0,
    anchor="nw",
    text="You got rewards.",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    189.0,
    577.0,
    anchor="nw",
    text="Accept these rewards?",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    175.0,
    156.0,
    anchor="nw",
    text="QUEST REWARDS",
    fill="#FFFFFF",
    font=("Inter Medium", 26 * -1)
)

canvas.create_rectangle(
    172.0,
    184.0,
    398.0,
    187.00000006601084,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    131.0,
    367.0,
    442.0,
    395.0,
    fill="#272727",
    outline="")

canvas.create_text(
    140.0,
    370.0,
    anchor="nw",
    text="1: Intelligence Points +1",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
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
    x=105.0,
    y=672.0,
    width=81.0,
    height=34.5
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
    x=387.0,
    y=672.0,
    width=81.0,
    height=34.5
)
window.resizable(False, False)
window.mainloop()
