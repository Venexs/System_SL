
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\System\Penalty Check\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("730x385")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 385,
    width = 730,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    591.0,
    363.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    363.0,
    201.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    363.0,
    65.0,
    image=image_image_3
)

canvas.create_text(
    53.0,
    101.0,
    anchor="nw",
    text="Please Enter paths to a specific program that distracts you such as a Video Game  ",
    fill="#FFFFFF",
    font=("MontserratRoman Regular", 12 * -1)
)

canvas.create_text(
    68.0,
    118.0,
    anchor="nw",
    text="D:\Games\Warframe\Downloaded\Public\Warframe.x64.exe",
    fill="#74D5FF",
    font=("MontserratRoman Bold", 10 * -1)
)

canvas.create_text(
    53.0,
    118.0,
    anchor="nw",
    text="Ex: ",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 10 * -1)
)

canvas.create_text(
    53.0,
    135.0,
    anchor="nw",
    text="Path 1:",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 13 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    298.5,
    165.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=53.0,
    y=155.0,
    width=491.0,
    height=18.0
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
    x=554.0,
    y=153.0,
    width=25.0,
    height=25.0
)

canvas.create_text(
    53.0,
    187.0,
    anchor="nw",
    text="Path 2:",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 13 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    298.5,
    217.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=53.0,
    y=207.0,
    width=491.0,
    height=18.0
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
    x=554.0,
    y=205.0,
    width=25.0,
    height=25.0
)

canvas.create_text(
    53.0,
    239.0,
    anchor="nw",
    text="Enter the time you usually use the distracting programs: (Ex: 18:30)",
    fill="#FFFFFF",
    font=("MontserratRoman Regular", 13 * -1)
)

canvas.create_text(
    64.0,
    256.0,
    anchor="nw",
    text="HH",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 13 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    75.5,
    284.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=53.0,
    y=274.0,
    width=45.0,
    height=18.0
)

canvas.create_text(
    107.0,
    274.0,
    anchor="nw",
    text=":",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 13 * -1)
)

canvas.create_text(
    129.0,
    256.0,
    anchor="nw",
    text="MM",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 13 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    140.5,
    284.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=118.0,
    y=274.0,
    width=45.0,
    height=18.0
)

canvas.create_text(
    53.0,
    323.0,
    anchor="nw",
    text="DO NOT INSERT PATHS TO IMPORTANT/CRUCIAL PROGRAMS!",
    fill="#FF0000",
    font=("MontserratRoman Bold", 10 * -1)
)

canvas.create_text(
    53.0,
    337.0,
    anchor="nw",
    text="NOT RECOMMENDED TO ADD GOOGLE CHROME OR OTHER WEB BROWSERS IN HERE!",
    fill="#FF0000",
    font=("MontserratRoman Bold", 10 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=579.0,
    y=321.0,
    width=75.0,
    height=16.0
)
window.resizable(False, False)
window.mainloop()
