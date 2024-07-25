
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import csv
import subprocess
import json
import cv2
from PIL import Image, ImageTk

subprocess.Popen(['python', 'sfx.py'])
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("555x729")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
#window.update()

class VideoPlayer:
    def __init__(self, canvas, video_path, x, y):
        self.canvas = canvas
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.x = x
        self.y = y
        self.image_id = self.canvas.create_image(self.x, self.y)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            # If the video has ended, reset the capture object
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.itemconfig(self.image_id, image=imgtk)
            self.canvas.imgtk = imgtk

        self.canvas.after(10, self.update_frame)

    def __del__(self):
        self.cap.release()

def start_move(event):
    global lastx, lasty
    lastx = event.x_root
    lasty = event.y_root

def move_window(event):
    global lastx, lasty
    deltax = event.x_root - lastx
    deltay = event.y_root - lasty
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry("+%s+%s" % (x, y))
    lastx = event.x_root
    lasty = event.y_root

def ex_close(win):
    win.quit()

def questadd():
    subprocess.Popen(['python', 'Anime Version/Quest adder/build/gui.py'])
    window.quit()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 729,
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
    404.0,
    image=image_image_1
)

video_path = "Files/0001-0200.mp4"
player = VideoPlayer(canvas, video_path, 277.0, 380.0)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    289.0,
    378.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    288.0,
    109.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    289.0,
    426.0,
    image=image_image_4
)

with open("Files/Quests/Active_Quests.json", 'r') as fson:
    main_data=json.load(fson)
    main_keys=list(main_data.keys())

name1=name2=name3=name4=name5=name6=name7=name8=name9=name10=name11=name12=name13='-'
rank1=rank2=rank3=rank4=rank5=rank6=rank7=rank8=rank9=rank10=rank11=rank12=rank13='-'
type1=type2=type3=type4=type5=type6=type7=type8=type9=type10=type11=type12=type13='-'
id1=id2=id3=id4=id5=id6=id7=id8=id9=id10=id11=id12=id13='-'

c=-1

def get_image(rank,typel):
    if rank!='-' and typel!='-':
        if rank=='D' or rank=='E':
            if typel=="Common":
                return PhotoImage(file=relative_to_assets("image_5.png"))
            
            elif typel=="Learn":
                return PhotoImage(file=relative_to_assets("image_6.png"))
            
        elif rank=='C' or rank=='B':
            if typel=="Common":
                return PhotoImage(file=relative_to_assets("image_8.png"))
            
            elif typel=="Learn":
                return PhotoImage(file=relative_to_assets("image_9.png"))
            
        elif rank=='A':
            if typel=="Common":
                return PhotoImage(file=relative_to_assets("image_11.png"))
            
            elif typel=="Learn":
                return PhotoImage(file=relative_to_assets("image_12.png"))
            
        elif rank=='S':
            if typel=="Common":
                return PhotoImage(file=relative_to_assets("image_14.png"))
            
            elif typel=="Learn":
                return PhotoImage(file=relative_to_assets("image_15.png"))
        
        elif rank=='?':
            if typel=='Unknown':
                return PhotoImage(file=relative_to_assets("image_16.png"))
    else:
        return PhotoImage(file=relative_to_assets("image_17.png"))
            
def open_quest(name,id,type):
    if name!="-":
        with open("Files/Temp Files/Quest Temp.csv", 'w', newline='') as csv_open:
                fw=csv.writer(csv_open)
                rec=[name,id]
                fw.writerow(rec)
        if type=='Learn':
            subprocess.Popen(['python', 'Anime Version/Quest Info/Learn Quest/build/gui.py'])
        
        elif type=='Common':
            subprocess.Popen(['python', 'Anime Version/Quest Info/Count Quest/build/gui.py'])

        elif type=='Unknown':
            subprocess.Popen(['python', 'Anime Version/Quest Info/Unknown Quest/build/gui.py'])

        window.quit()

# ? ==================================================================
try:
    name1=main_keys[c+1]
    rank1=main_data[main_keys[c+1]][0]["rank"]
    type1=main_data[main_keys[c+1]][0]["type"]
    id1=main_data[main_keys[c+1]][0]["ID"]
except:
    name1=rank1=type1=id1='-'

image_image_5=get_image(rank1,type1)
image_5 = canvas.create_image(
    289.0,
    196.0,
    image=image_image_5
)

canvas.create_text(
    121.0,
    184.0,
    anchor="nw",
    text=name1,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name2=main_keys[c+1]
    rank2=main_data[main_keys[c+1]][0]["rank"]
    type2=main_data[main_keys[c+1]][0]["type"]
    id2=main_data[main_keys[c+1]][0]["ID"]
except:
    name2=rank2=type2=id2='-'

image_image_6=get_image(rank2,type2)
image_6 = canvas.create_image(
    289.0,
    235.0,
    image=image_image_6
)

canvas.create_text(
    119.0,
    223.0,
    anchor="nw",
    text=name2,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name3=main_keys[c+1]
    rank3=main_data[main_keys[c+1]][0]["rank"]
    type3=main_data[main_keys[c+1]][0]["type"]
    id3=main_data[main_keys[c+1]][0]["ID"]
except:
    name3=rank3=type3=id3='-'

image_image_7=get_image(rank3,type3)
image_7 = canvas.create_image(
    289.0,
    274.0,
    image=image_image_7
)

canvas.create_text(
    119.0,
    262.0,
    anchor="nw",
    text=name3,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name4=main_keys[c+1]
    rank4=main_data[main_keys[c+1]][0]["rank"]
    type4=main_data[main_keys[c+1]][0]["type"]
    id4=main_data[main_keys[c+1]][0]["ID"]
except:
    name4=rank4=type4=id4='-'

image_image_8=get_image(rank4,type4)
image_8 = canvas.create_image(
    289.0,
    313.0,
    image=image_image_8
)

canvas.create_text(
    119.0,
    301.0,
    anchor="nw",
    text=name4,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name5=main_keys[c+1]
    rank5=main_data[main_keys[c+1]][0]["rank"]
    type5=main_data[main_keys[c+1]][0]["type"]
    id5=main_data[main_keys[c+1]][0]["ID"]
except:
    name5=rank5=type5=id5='-'

image_image_9=get_image(rank5,type5)
image_9 = canvas.create_image(
    289.0,
    352.0,
    image=image_image_9
)

canvas.create_text(
    119.0,
    340.0,
    anchor="nw",
    text=name5,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name6=main_keys[c+1]
    rank6=main_data[main_keys[c+1]][0]["rank"]
    type6=main_data[main_keys[c+1]][0]["type"]
    id6=main_data[main_keys[c+1]][0]["ID"]
except:
    name6=rank6=type6=id6='-'

image_image_10=get_image(rank6,type6)
image_10 = canvas.create_image(
    289.0,
    391.0,
    image=image_image_10
)

canvas.create_text(
    119.0,
    379.0,
    anchor="nw",
    text=name6,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name7=main_keys[c+1]
    rank7=main_data[main_keys[c+1]][0]["rank"]
    type7=main_data[main_keys[c+1]][0]["type"]
    id7=main_data[main_keys[c+1]][0]["ID"]
except:
    name7=rank7=type7=id7='-'

image_image_11=get_image(rank7,type7)
image_11 = canvas.create_image(
    289.0,
    430.0,
    image=image_image_11
)

canvas.create_text(
    119.0,
    418.0,
    anchor="nw",
    text=name7,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name8=main_keys[c+1]
    rank8=main_data[main_keys[c+1]][0]["rank"]
    type8=main_data[main_keys[c+1]][0]["type"]
    id8=main_data[main_keys[c+1]][0]["ID"]
except:
    name8=rank8=type8=id8='-'

image_image_12=get_image(rank8,type8)
image_12 = canvas.create_image(
    289.0,
    469.0,
    image=image_image_12
)

canvas.create_text(
    119.0,
    457.0,
    anchor="nw",
    text=name8,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name9=main_keys[c+1]
    rank9=main_data[main_keys[c+1]][0]["rank"]
    type9=main_data[main_keys[c+1]][0]["type"]
    id9=main_data[main_keys[c+1]][0]["ID"]
except:
    name9=rank9=type9=id9='-'

image_image_13=get_image(rank9,type9)
image_13 = canvas.create_image(
    289.0,
    508.0,
    image=image_image_13
)

canvas.create_text(
    119.0,
    496.0,
    anchor="nw",
    text=name9,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name10=main_keys[c+1]
    rank10=main_data[main_keys[c+1]][0]["rank"]
    type10=main_data[main_keys[c+1]][0]["type"]
    id10=main_data[main_keys[c+1]][0]["ID"]
except:
    name10=rank10=type10=id10='-'

image_image_14=get_image(rank10,type10)
image_14 = canvas.create_image(
    289.0,
    547.0,
    image=image_image_14
)

canvas.create_text(
    119.0,
    535.0,
    anchor="nw",
    text=name10,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name11=main_keys[c+1]
    rank11=main_data[main_keys[c+1]][0]["rank"]
    type11=main_data[main_keys[c+1]][0]["type"]
    id11=main_data[main_keys[c+1]][0]["ID"]
except:
    name11=rank11=type11=id11='-'

image_image_15=get_image(rank11,type11)
image_15 = canvas.create_image(
    289.0,
    586.0,
    image=image_image_15
)

canvas.create_text(
    119.0,
    574.0,
    anchor="nw",
    text=name11,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name12=main_keys[c+1]
    rank12=main_data[main_keys[c+1]][0]["rank"]
    type12=main_data[main_keys[c+1]][0]["type"]
    id12=main_data[main_keys[c+1]][0]["ID"]
except:
    name12=rank12=type12=id12='-'

image_image_16=get_image(rank12,type12)
image_16 = canvas.create_image(
    289.0,
    625.0,
    image=image_image_16
)

canvas.create_text(
    119.0,
    613.0,
    anchor="nw",
    text=name12,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

# ? ==================================================================
c+=1
try:
    name13=main_keys[c+1]
    rank13=main_data[main_keys[c+1]][0]["rank"]
    type13=main_data[main_keys[c+1]][0]["type"]
    id13=main_data[main_keys[c+1]][0]["ID"]
except:
    name12=rank12=type12=id12='-'

image_image_17=get_image(rank13,type13)
image_17 = canvas.create_image(
    289.0,
    664.0,
    image=image_image_17
)

canvas.create_text(
    119.0,
    652.0,
    anchor="nw",
    text=name13,
    fill="#FFFFFF",
    font=("Montserrat", 18 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name1, id1, type1),
    relief="flat"
)
button_1.place(
    x=465.0,
    y=184.0,
    width=24.0,
    height=24.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name2, id2, type2),
    relief="flat"
)
button_2.place(
    x=465.0,
    y=223.0,
    width=24.0,
    height=24.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name3, id3, type3),
    relief="flat"
)
button_3.place(
    x=465.0,
    y=262.0,
    width=24.0,
    height=24.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name4, id4, type4),
    relief="flat"
)
button_4.place(
    x=465.0,
    y=301.0,
    width=24.0,
    height=24.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name5, id5, type5),
    relief="flat"
)
button_5.place(
    x=465.0,
    y=340.0,
    width=24.0,
    height=24.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name6, id6, type6),
    relief="flat"
)
button_6.place(
    x=465.0,
    y=379.0,
    width=24.0,
    height=24.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name7, id7, type7),
    relief="flat"
)
button_7.place(
    x=465.0,
    y=418.0,
    width=24.0,
    height=24.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name8, id8, type8),
    relief="flat"
)
button_8.place(
    x=465.0,
    y=457.0,
    width=24.0,
    height=24.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name9, id9, type9),
    relief="flat"
)
button_9.place(
    x=465.0,
    y=496.0,
    width=24.0,
    height=24.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name10, id10, type10),
    relief="flat"
)
button_10.place(
    x=465.0,
    y=535.0,
    width=24.0,
    height=24.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name11, id11, type11),
    relief="flat"
)
button_11.place(
    x=465.0,
    y=574.0,
    width=24.0,
    height=24.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name12, id12, type12),
    relief="flat"
)
button_12.place(
    x=465.0,
    y=613.0,
    width=24.0,
    height=24.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_quest(name13, id13, type13),
    relief="flat"
)
button_13.place(
    x=465.0,
    y=652.0,
    width=24.0,
    height=24.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: questadd(),
    relief="flat"
)
button_14.place(
    x=472.0,
    y=129.0,
    width=30.0,
    height=30.0
)

image_0=canvas.create_rectangle(
    0.0,
    0.0,
    570.0,
    35.0,
    fill="#212121",
    outline="")

canvas.tag_bind(image_0, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_0, "<B1-Motion>", move_window)

button_image_0 = PhotoImage(
    file=relative_to_assets("button_0.png"))
button_0 = Button(
    image=button_image_0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ex_close(window),
    relief="flat"
)
button_0.place(
    x=520.0,
    y=3.0,
    width=28.0,
    height=28.0
)

window.resizable(False, False)
window.mainloop()
