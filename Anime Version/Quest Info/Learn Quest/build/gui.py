
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import json
import csv
import subprocess
import cv2
from PIL import Image, ImageTk

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def make_window_transparent(window):
    # This function makes the window background transparent
    window.wm_attributes('-transparentcolor', "#0c679b")

window = Tk()

window.geometry("897x555")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
make_window_transparent(window)

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

with open("Files/Temp Files/Quest Temp.csv", 'r') as csv_open:
    fr=csv.reader(csv_open)
    for k in fr:
        name=k[0]

objdesc1=objdesc2=''
desc1=desc2=''
segments = []
other_seg=[]
segment_length = 70

with open("Files/Quests/Active_Quests.json", 'r') as fson:
    data=json.load(fson)
    for k in data:
        if k==name:
            obj=objval='-'
            rank=data[k][0]["rank"]

            check=True
            try:
                skill=data[k][0]["skill"]
                level=data[k][0]["level"]
            except:
                check=False
                obj_desc=data[k][0]["obj_desc"]
                for i in range(0, len(obj_desc), segment_length):
                    other_seg.append(obj_desc[i:i+segment_length])

                if len(other_seg) >= 1:
                    objdesc1 = other_seg[0]
                if len(other_seg) >= 2:
                    objdesc2 = "-"+other_seg[1]

            try:
                obj=data[k][0]["amt"]
                objval=data[k][0]["amtval"]
            except:
                obj=data[k][0]["time"]
                objval=data[k][0]["timeval"]

            desc_full=data[k][0]["desc"]

            for i in range(0, len(desc_full), segment_length):
                segments.append(desc_full[i:i+segment_length])

            if len(segments) >= 1:
                desc1 = segments[0]
            if len(segments) >= 2:
                desc2 = "-"+segments[1]

            rewards=data[k][0]["Rewards"]

def preview(nameob,quantity):
    if nameob!='-' and quantity!=0:
        with open("Files/Temp Files/Preview Item Temp.csv", 'w', newline='') as new_csv_open:
            fw=csv.writer(new_csv_open)
            rec=[nameob, quantity]
            fw.writerow(rec)
        subprocess.Popen(['python', 'Anime Version/Preview Item/build/gui.py'])

def reward():
    rol=list(dicts.keys())
    for k in rol:
        if k=="LVLADD":
            with open("Files/Status.json", 'r') as fson:
                    data_status=json.load(fson)
            
            for k in range(dicts[k]):                
                data_status["status"][0]['level']+=1
                data_status["status"][0]['str']+=1
                data_status["status"][0]['agi']+=1
                data_status["status"][0]['vit']+=1
                data_status["status"][0]['int']+=1
                data_status["status"][0]['per']+=1
                data_status["status"][0]['hp']+=10
                data_status["status"][0]['mp']+=10
                
            if rank=="E":
                data_status["status"][0]['XP']+=10
            elif rank=="D":
                data_status["status"][0]['XP']+=20
            elif rank=="C":
                data_status["status"][0]['XP']+=40
            elif rank=="B":
                data_status["status"][0]['XP']+=80
            elif rank=="A":
                data_status["status"][0]['XP']+=150
            elif rank=="S":
                data_status["status"][0]['XP']+=200

            with open("Files/status.json", 'w') as fson:
                json.dump(data_status, fson, indent=4)
            subprocess.Popen(['python', 'Anime Version/Leveled up NO ADD/build/gui.py'])

        elif k=="STRav":
            for k in range(dicts[k]):
                with open("Files/Status.json", 'r') as fson:
                    data_status_2=json.load(fson)
                    
                    data_status_2["avail_eq"][0]['str_based']+=1

                with open("Files/status.json", 'w') as fson:
                    json.dump(data_status_2, fson, indent=4)

        elif k=="INTav":
            for k in range(dicts[k]):
                with open("Files/Status.json", 'r') as fson:
                    data_status_3=json.load(fson)
                    
                    data_status_3["avail_eq"][0]['int_based']+=1

                with open("Files/status.json", 'w') as fson:
                    json.dump(data_status_3, fson, indent=4)

        else:
            check=False
            with open("Files/Data/Inventory_list.json", 'r') as fson:
                data_inv=json.load(fson)
                item=data_inv[k]
                name_of_item=k
            
            with open("Files/Inventory.json", 'r') as fson:
                data_fininv=json.load(fson)
                key_data=list(data_fininv.keys())

                for k in key_data:
                    if name_of_item==k:
                        check=True
            
            if check==True:
                data_fininv[name_of_item][0]["qty"]+=1

            elif check==False:
                data_fininv[name_of_item]=item

            with open("Files/Inventory.json", 'w') as finaladdon:
                json.dump(data_fininv, finaladdon, indent=6)

    with open("Files/Quests/Active_Quests.json", 'r') as fols:
        quests=json.load(fols)

    del quests[name]

    with open("Files/Quests/Active_Quests.json", 'w') as folas:
        json.dump(quests, folas, indent=6)

    subprocess.Popen(['python', 'Anime Version/Quest Complete/build/gui.py'])
    subprocess.Popen(['python', 'Anime Version/Quests/build/gui.py'])

    window.quit()

def abandon():
    with open("Files/Quests/Active_Quests.json", 'r') as fols:
        quests=json.load(fols)

    del quests[name]

    with open("Files/Quests/Active_Quests.json", 'r') as fols:
        json.dump(quests, fols, indent=6)

    subprocess.Popen(['python', 'Anime Version/Quests/build/gui.py'])

    window.quit()

def return_quest():
    subprocess.Popen(['python', 'Anime Version/Quests/build/gui.py'])

    window.quit()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 555,
    width = 897,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    277.0,
    image=image_image_1
)

video_path = "Files/0001-0200.mp4"
player = VideoPlayer(canvas, video_path, 478.0, 277.0)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    448.0,
    284.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    448.023681640625,
    117.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    512.6856384277344,
    226.34335327148438,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    235.40396118164062,
    252.2617950439453,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    235.023681640625,
    252.0,
    image=image_image_6
)

canvas.create_text(
    325.023681640625,
    218.0,
    anchor="nw",
    text=name,
    fill="#FFFFFF",
    font=("Montserrat Regular", 16 * -1)
)

if check==True:
    canvas.create_text(
        329.023681640625,
        300.0,
        anchor="nw",
        text=f"Learn [{skill}] and become [{level}] at it.",
        fill="#FFFFFF",
        font=("Montserrat Regular", 11 * -1)
    )

else:
    canvas.create_text(
        329.023681640625,
        300.0,
        anchor="nw",
        text=objdesc1,
        fill="#FFFFFF",
        font=("Montserrat Regular", 11 * -1)
    )

    canvas.create_text(
        329.023681640625,
        313.0,
        anchor="nw",
        text=objdesc2,
        fill="#FFFFFF",
        font=("Montserrat Regular", 11 * -1)
    )

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    447.023681640625,
    309.0,
    image=image_image_7
)

canvas.create_text(
    329.023681640625,
    246.0,
    anchor="nw",
    text="Quest Difficulty:",
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 12 * -1)
)

canvas.create_text(
    395.0,
    283.0,
    anchor="nw",
    text=f"Do for {obj} {objval}",
    fill="#FFFFFF",
    font=("Montserrat Regular", 12 * -1)
)

canvas.create_text(
    329,
    283.0,
    anchor="nw",
    text="Objective:",
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 12 * -1)
)

canvas.create_text(
    329.023681640625,
    264.0,
    anchor="nw",
    text=f"{rank}-Rank",
    fill="#FFFFFF",
    font=("Montserrat Regular", 12 * -1)
)

canvas.create_text(
    327.023681640625,
    332.0,
    anchor="nw",
    text=desc1,
    fill="#FFFFFF",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    327.023681640625,
    344.0,
    anchor="nw",
    text=desc2,
    fill="#FFFFFF",
    font=("Montserrat Regular", 10 * -1)
)

# ? ===============================================================================

name1=name2=name3=name4='-'
qt1=qt2=qt3=qt4=0
dicts={}

try:
    c=0
    reward_key=list(rewards.keys())
    for k in reward_key:
        if c==0:
            if k=="LVLADD":
                name1="Level Increase"
                o_name1=k
                qt1=data[name][0]["Rewards"]["LVLADD"]
                c+=1
            elif k=="STRav":
                name1="Addition of STR, AGI, VIT, Available Points"
                o_name1=k
                qt1=data[name][0]["Rewards"]["STRav"]
                c+=1
            elif k=="INTav":
                name1="Addition of INT, PER, MAN, Available Points"
                o_name1=k
                qt1=data[name][0]["Rewards"]["INTav"]
                c+=1
            else:
                name1=k
                o_name1=k
                qt1=data[name][0]["Rewards"][k]
                c+=1
            
            dicts[o_name1]=qt1

        elif c==1:
            if k=="LVLADD":
                name2="Level Increase"
                o_name2=k
                qt2=rewards=data[name][0]["Rewards"]["LVLADD"]
                c+=1
            elif k=="STRav":
                name2="Addition of STR, AGI, VIT, Available Points"
                o_name2=k
                qt2=rewards=data[name][0]["Rewards"]["STRav"]
                c+=1
            elif k=="INTav":
                name2="Addition of INT, PER, MAN, Available Points"
                o_name2=k
                qt2=rewards=data[name][0]["Rewards"]["INTav"]
                c+=1
            else:
                name2=k
                o_name2=k
                qt2=data[name][0]["Rewards"][k]
                c+=1

            dicts[o_name2]=qt2

        elif c==2:
            if k=="LVLADD":
                name3="Level Increase"
                o_name3=k
                qt3=rewards=data[name][0]["Rewards"]["LVLADD"]
                c+=1
            elif k=="STRav":
                name3="Addition of STR, AGI, VIT, Available Points"
                o_name3=k
                qt3=rewards=data[name][0]["Rewards"]["STRav"]
                c+=1
            elif k=="INTav":
                name3="Addition of INT, PER, MAN, Available Points"
                o_name3=k
                qt3=rewards=data[name][0]["Rewards"]["INTav"]
                c+=1
            else:
                name3=k
                o_name3=k
                qt3=data[name][0]["Rewards"][k]
                c+=1

            dicts[o_name3]=qt3

        elif c==3:
            if k=="LVLADD":
                name4="Level Increase"
                o_name4=k
                qt4=rewards=data[name][0]["Rewards"]["LVLADD"]
                c+=1
            elif k=="STRav":
                name4="Addition of STR, AGI, VIT, Available Points"
                o_name4=k
                qt4=rewards=data[name][0]["Rewards"]["STRav"]
                c+=1
            elif k=="INTav":
                name4="Addition of INT, PER, MAN, Available Points"
                o_name4=k
                qt4=rewards=data[name][0]["Rewards"]["INTav"]
                c+=1
            else:
                name4=k
                o_name4=k
                qt4=data[name][0]["Rewards"][k]
                c+=1

            dicts[o_name4]=qt4

except:
    print()

canvas.create_text(
    168.023681640625,
    347.0,
    anchor="nw",
    text="REWARDS:",
    fill="#10DF4A",
    font=("Montserrat SemiBold", 14 * -1)
)

canvas.create_text(
    181.023681640625,
    364.0,
    anchor="nw",
    text=f"-{name1}",
    fill="#FFFFFF",
    font=("Montserrat Light", 12 * -1)
)

canvas.create_text(
    181.023681640625,
    380.0,
    anchor="nw",
    text=f"-{name2}",
    fill="#FFFFFF",
    font=("Montserrat Light", 12 * -1)
)

canvas.create_text(
    181.023681640625,
    396.0,
    anchor="nw",
    text=f"-{name3}",
    fill="#FFFFFF",
    font=("Montserrat Light", 12 * -1)
)

canvas.create_text(
    181.023681640625,
    412.0,
    anchor="nw",
    text=f"-{name4}",
    fill="#FFFFFF",
    font=("Montserrat Light", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: return_quest(),
    relief="flat"
)
button_1.place(
    x=785.023681640625,
    y=62.0,
    width=40.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: preview(o_name1,qt1),
    relief="flat"
)
button_2.place(
    x=168.023681640625,
    y=366.0,
    width=13.0,
    height=13.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: preview(o_name2,qt2),
    relief="flat"
)
button_3.place(
    x=168.023681640625,
    y=382.0,
    width=13.0,
    height=13.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: preview(o_name3,qt3),
    relief="flat"
)
button_4.place(
    x=168.023681640625,
    y=397.0,
    width=13.0,
    height=13.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: preview(o_name4,qt4),
    relief="flat"
)
button_5.place(
    x=168.023681640625,
    y=413.0,
    width=13.0,
    height=12.999969482421875
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    136.023681640625,
    481.0,
    image=image_image_8
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: abandon(),
    relief="flat"
)
button_6.place(
    x=587.023681640625,
    y=378.0,
    width=120.0,
    height=16.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: reward(),
    relief="flat"
)
button_7.place(
    x=587.023681640625,
    y=398.0,
    width=120.0,
    height=16.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    240.0,
    24.0,
    fill="#0c679b",
    outline="")

canvas.create_rectangle(
    0.0,
    525.0,
    925.0,
    555.0,
    fill="#0c679b",
    outline="")

image_image_40 = PhotoImage(
    file=relative_to_assets("Side1.png"))
image_40 = canvas.create_image(
    20.0,
    270.0,
    image=image_image_40
)

image_image_50 = PhotoImage(
    file=relative_to_assets("Side2.png"))
image_50 = canvas.create_image(
    880.0,
    294.0,
    image=image_image_50
)

canvas.create_rectangle(
    240.0,
    0.0,
    957.0,
    36.0,
    fill="#0c679b",
    outline="")

image_image_60 = PhotoImage(
    file=relative_to_assets("Bar1.png"))
image_60 = canvas.create_image(
    478.0,
    21.0,
    image=image_image_60
)

canvas.tag_bind(image_60, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_60, "<B1-Motion>", move_window)

image_image_70 = PhotoImage(
    file=relative_to_assets("Bar2.png"))
image_70 = canvas.create_image(
    480.0,
    530.0,
    image=image_image_70
)

window.resizable(False, False)
window.mainloop()
