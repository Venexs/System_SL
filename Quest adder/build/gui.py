
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import subprocess
subprocess.Popen(['python', 'sfx.py'])
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Projects\System\Quest adder\build\assets\frame0")


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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    286.9999999999999,
    483.9999999999999,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    277.0,
    493.0,
    image=image_image_3
)

canvas.create_text(
    199.0,
    116.0,
    anchor="nw",
    text="Quest Adder",
    fill="#FFFFFF",
    font=("Inter Medium", 26 * -1)
)

# ! ============================================
# ! MAIN QUEST INFO
# ! ============================================

# ? ===========================================
# ? NAME OF QUEST
# ? ===========================================

canvas.create_text(
    64.0,
    173.0,
    anchor="nw",
    text="Name of Quest:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    281.5,
    211.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=64.0,
    y=197.0,
    width=435.0,
    height=26.0
)

# ? ===========================================
# ? Quest Description
# ? ===========================================

canvas.create_text(
    64.0,
    227.0,
    anchor="nw",
    text="Quest Description:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    281.5,
    263.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=64.0,
    y=249.0,
    width=435.0,
    height=26.0
)

# ? ===========================================
# ? Quest Type
# ? ===========================================

canvas.create_text(
    64.0,
    285.0,
    anchor="nw",
    text="Type of Quest:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    178.0,
    321.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=64.0,
    y=307.0,
    width=228.0,
    height=26.0
)

# ! ============================================
# ! INCLUSIVE
# ! ============================================

canvas.create_text(
    56.0,
    350.0,
    anchor="nw",
    text="If Inclusive:",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

# ? ===========================================
# ? Which Daily Quest Exc
# ? ===========================================

canvas.create_text(
    65.0,
    373.0,
    anchor="nw",
    text="Which Daily Quest Exc:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

# ? Rules

canvas.create_text(
    376.0,
    354.0,
    anchor="nw",
    text="(Use Run,Squat,Sit,Push)",
    fill="#FF0000",
    font=("Inter", 12 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    179.0,
    409.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=65.0,
    y=395.0,
    width=228.0,
    height=26.0
)

# ? ===========================================
# ? Daily Quest Value to reach
# ? ===========================================

canvas.create_text(
    308.0,
    373.0,
    anchor="nw",
    text="Value to reach:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    372.0,
    409.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=308.0,
    y=395.0,
    width=128.0,
    height=26.0
)

# ! Time Limit

# ? ===========================================
# ? Time Limit (IF)
# ? ===========================================

canvas.create_text(
    65.0,
    430.0,
    anchor="nw",
    text="Time Limit? (Y/N)",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    85.5,
    468.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=65.0,
    y=454.0,
    width=41.0,
    height=26.0
)

# ? ===========================================
# ? For Time Limit (IF)
# ? ===========================================

canvas.create_text(
    232.0,
    430.0,
    anchor="nw",
    text="If so, Enter Hour, Minute, Seconds:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

# ! Hour

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    271.0,
    468.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=234.0,
    y=454.0,
    width=74.0,
    height=26.0
)

# ! Minute

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    372.0,
    468.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=335.0,
    y=454.0,
    width=74.0,
    height=26.0
)

# ! Seconds

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    482.0,
    468.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=445.0,
    y=454.0,
    width=74.0,
    height=26.0
)

# ! ============================================
# ! EXCLUSIVE
# ! ============================================

canvas.create_text(
    56.0,
    493.0,
    anchor="nw",
    text="If Exclusive:",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

# ? ===========================================
# ? Name of skill to Master
# ? ===========================================

canvas.create_text(
    61.0,
    515.0,
    anchor="nw",
    text="Skill to Master",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    175.0,
    553.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=61.0,
    y=539.0,
    width=228.0,
    height=26.0
)

# ? ===========================================
# ? Skill Reach (IF)
# ? ===========================================

canvas.create_text(
    304.0,
    517.0,
    anchor="nw",
    text="Any Reach value (Y/N)",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    340.0,
    553.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=304.0,
    y=539.0,
    width=72.0,
    height=26.0
)

# ? ===========================================
# ? Skill Reach Value
# ? ===========================================

canvas.create_text(
    304.0,
    569.0,
    anchor="nw",
    text="If Yes, enter value:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    340.0,
    605.0,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=304.0,
    y=591.0,
    width=72.0,
    height=26.0
)

# ? ===========================================
# ? For Time Limit (If)
# ? ===========================================

canvas.create_text(
    61.0,
    626.0,
    anchor="nw",
    text="Time Limit? (Y/N):",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    81.5,
    664.0,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=61.0,
    y=650.0,
    width=41.0,
    height=26.0
)

# ? ===========================================
# ? Time Limit
# ? ===========================================

canvas.create_text(
    230.0,
    626.0,
    anchor="nw",
    text="If so, Enter Hour, Minute, Seconds:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

# ! Hour

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    267.0,
    664.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=230.0,
    y=650.0,
    width=74.0,
    height=26.0
)

# ! Minute

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    368.0,
    664.0,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=331.0,
    y=650.0,
    width=74.0,
    height=26.0
)

# ! Seconds

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    478.0,
    664.0,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=441.0,
    y=650.0,
    width=74.0,
    height=26.0
)

# ! ===========================================
# ! REWARDS
# ! ===========================================

canvas.create_text(
    56.0,
    689.0,
    anchor="nw",
    text="Reward:",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

# ? ===========================================
# ? ITEM (Y/N)
# ? ===========================================

canvas.create_text(
    61.0,
    711.0,
    anchor="nw",
    text="Item (Y/N):",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    81.5,
    749.0,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=61.0,
    y=735.0,
    width=41.0,
    height=26.0
)

# ? ===========================================
# ? ITEM NAME
# ? ===========================================

canvas.create_text(
    159.0,
    711.0,
    anchor="nw",
    text="Item Name:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    254.0,
    749.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=160.0,
    y=735.0,
    width=188.0,
    height=26.0
)

# ? ===========================================
# ? ITEM Description
# ? ===========================================

canvas.create_text(
    362.0,
    708.0,
    anchor="nw",
    text="Item Description:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_19 = canvas.create_image(
    434.0,
    788.0,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=362.0,
    y=735.0,
    width=144.0,
    height=104.0
)

# ? ===========================================
# ? ABILITY BOOSTER (NAME)
# ? ===========================================

# ! IT DOES NOT MATTER IF THERE'S AN ITEM OR NOT

canvas.create_text(
    59.0,
    774.0,
    anchor="nw",
    text="Ability Booster:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

canvas.create_text(
    56.0,
    835.0,
    anchor="nw",
    text="(Use AGI,VIT,INT,PER,STR)",
    fill="#FF0000",
    font=("Inter", 12 * -1)
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_20 = canvas.create_image(
    117.5,
    810.0,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=59.0,
    y=796.0,
    width=117.0,
    height=26.0
)

# ? ===========================================
# ? ABILITY BOOSTER (VALUE)
# ? ===========================================

canvas.create_text(
    198.0,
    774.0,
    anchor="nw",
    text="Boost Value:",
    fill="#FFFFFF",
    font=("Inter", 18 * -1)
)

entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_21 = canvas.create_image(
    217.0,
    810.0,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_21.place(
    x=198.0,
    y=796.0,
    width=38.0,
    height=26.0
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
    x=411.0,
    y=904.0,
    width=128.0,
    height=34.0
)
window.resizable(False, False)
window.mainloop()
