
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import json
import csv
import subprocess
import random
import cv2
from PIL import Image, ImageTk
from datetime import datetime, timedelta

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("391x676")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
#window.update()

def three_val(val):
    values=f"{val:03d}:"
    new_value=''
    for k in values:
        if k!=':':
            new_value+=k
    return new_value

def sign(num):
    if num<0:
        return "-"
    elif num>0:
        return "+"
    elif num==0:
        return ""

def pos_fix(num):
    if num<0:
        num=abs(num)
        return str(num)
    elif num==0:
        return ""
    else:
        return str(num)

class VideoPlayer:
    def __init__(self, canvas, video_path, x, y, frame_skip=2, resize_factor=0.8):
        self.canvas = canvas
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.x = x
        self.y = y
        self.frame_skip = frame_skip  # Number of frames to skip
        self.resize_factor = resize_factor  # Factor to resize frames
        self.image_id = self.canvas.create_image(self.x, self.y)
        self.frame_count = 0
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        
        if not ret:
            # If the video has ended, reset the capture object
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()

        if ret:
            self.frame_count += 1
            if self.frame_count % self.frame_skip == 0:  # Skip frames for performance
                frame = cv2.resize(frame, (0, 0), fx=self.resize_factor, fy=self.resize_factor)
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

def title_chng(event):
    subprocess.Popen(['python', 'Anime Version/Equip Title/build/gui.py'])

    window.quit()

def title_color(name):
    if name=="False Ranker":
        color="#FF2F2F"
    elif name=="One Above All":
        color="#FFCF26"
    else:
        color="#FFFFFF"

    return color

def start_job(event):
    with open("Files/Data/Job_info.json", 'r') as stat_fson:
        data=json.load(stat_fson)

    canvas.itemconfig("Jobs", state="hidden")
    data["status"][0]["job_active"]='True'

    data["status"][1]["plSTR"]=int(stre)
    data["status"][1]["plINT"]=int(intel)
    data["status"][1]["plAGI"]=int(agi)
    data["status"][1]["plVIT"]=int(vit)
    data["status"][1]["plPER"]=int(per)
    data["status"][1]["plMAN"]=int(man)

    with open("Files\Temp Files\Job_Change Date.csv", 'w', newline='') as time_open_csv_file:
        fw=csv.writer(time_open_csv_file)
        current_date = datetime.now()
        # Add 10 days to the current date
        future_date = current_date + timedelta(days=1)
        # Define the desired format for the date string
        date_format = "%Y-%m-%d"
        # Convert the future date to a string
        future_date_string = future_date.strftime(date_format)
        fw.writerow([future_date_string])

    with open("Files/Data/Job_info.json", 'w') as fson:
        json.dump(data, fson, indent=4)

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
    413.0,
    image=image_image_1
)

video_path = "Files/0001-0200.mp4"
player = VideoPlayer(canvas, video_path, 478.0, 413.0)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    195.0,
    362.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    109.0,
    112.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    191.0,
    455.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    191.0,
    328.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    748.0,
    80.0,
    image=image_image_6
)

# ? =====================================================================
# ? =====================================================================

with open("Files/status.json", 'r') as fson:
    data=json.load(fson)
    name=data["status"][0]['name'].upper()
    # ? =================================================
    hp=data["status"][0]['hp']
    mp=data["status"][0]['mp']
    lvl=data["status"][0]['level']
    old_lvl=f"{lvl:02d}"
    # ? =================================================
    stre=data["status"][0]['str']
    stre=three_val(stre)

    intel=data["status"][0]['int']
    intel=three_val(intel)

    agi=data["status"][0]['agi']
    agi=three_val(agi)

    vit=data["status"][0]['vit']
    vit=three_val(vit)

    per=data["status"][0]['per']
    per=three_val(per)

    man=data["status"][0]['man']
    man=three_val(man)
    # ? =================================================
    tit=data["status"][1]['title']
    job=data["status"][1]['job'].upper()
    # ? =================================================
    xp_str=data["status"][0]['XP']
    coins=data["status"][0]['coins']
    # ? =================================================
    av_str_based=data["avail_eq"][0]['str_based']
    av_str_based=three_val(av_str_based)
    av_int_based=data["avail_eq"][0]['int_based']
    av_int_based=three_val(av_int_based)
    # ? =================================================
    str_buff=data["equipment"][0]["STR"]
    str_buff=sign(str_buff)+pos_fix(str_buff)

    agi_buff=data["equipment"][0]["AGI"]
    agi_buff=sign(agi_buff)+pos_fix(agi_buff)

    vit_buff=data["equipment"][0]["VIT"]
    vit_buff=sign(vit_buff)+pos_fix(vit_buff)

    int_buff=data["equipment"][0]["INT"]
    int_buff=sign(int_buff)+pos_fix(int_buff)

    per_buff=data["equipment"][0]["PER"]
    per_buff=sign(per_buff)+pos_fix(per_buff)

    man_buff=data["equipment"][0]["MAN"]
    man_buff=sign(man_buff)+pos_fix(man_buff)
    # ? =================================================

# ? =====================================================================
# ? =====================================================================

if lvl!=0:
    fin_chk=False
    with open("Files/Data/Level_Up_Values.json", 'r') as fron2:
        data_2=json.load(fron2)
        xp_chl=data_2["XP Check"][str(lvl+1)]
        if xp_str>=xp_chl:
            fin_chk=True

    if fin_chk==True:
        data["status"][0]['level']+=1
        with open("Files/status.json", 'w') as up_fson:
            json.dump(data, up_fson, indent=4)
        subprocess.Popen(['python', 'Anime Version/Leveled up NO ADD/build/gui.py'])
        subprocess.Popen(['python', 'Anime Version/Status Tab/build/gui.py'])
        window.quit()

with open("Files/Data/Level_Up_Values.json", 'r') as fron:
    data_1=json.load(fron)
    xp_end=data_1["XP Check"][str(lvl)]

    fin_xp=xp_end-xp_str

# ? =====================================================================
# ? =====================================================================

# / =================================================
# / =================================================

def update_str():
    if int(av_str_based)!=0:
        with open("Files\Checks\Ability_Check.json", 'r') as ability_check_file:
            ability_check_file_data=json.load(ability_check_file)
            val=ability_check_file_data["Check"]["STR"]
        if val<3:
            with open("Files/Data/Job_info.json", 'r') as stat_fson:
                stat_data=json.load(stat_fson)
            global str_txt
            current_text = canvas.itemcget(str_txt, "text")
            # ? ====================================================
            current_number = int(current_text)
            new_number = current_number + 1
            # ? ====================================================
            with open("Files/status.json", 'w') as fson:
                data["status"][0]['str']+=1
                data["avail_eq"][0]['str_based']-=1
                json.dump(data, fson, indent=4)
            # ? ====================================================
            stat_data["status"][1]["STR"]+=1
            with open("Files/Data/Job_info.json", 'w') as final_stat_fson:
                json.dump(stat_data, final_stat_fson, indent=4)
            # ? ====================================================
            new_text = f"{new_number:03d}"
            canvas.itemconfig(str_txt, text=new_text)
            with open("Files\Checks\Ability_Check.json", 'w') as fin_ability_check_file:
                ability_check_file_data["Check"]["STR"]+=1
                json.dump(ability_check_file_data, fin_ability_check_file, indent=4)
            de_update_str()
        else:
            with open("Files/Temp Files/Urgent Temp.csv", 'w', newline='') as urgent_file:
                fr=csv.writer(urgent_file)
                fr.writerow(["STR"])
            subprocess.Popen(['python', 'Anime Version/Urgent Quest/build/gui.py'])
            window.quit()

def update_agi():
    if int(av_str_based)!=0:
        with open("Files\Checks\Ability_Check.json", 'r') as ability_check_file:
            ability_check_file_data=json.load(ability_check_file)
            val=ability_check_file_data["Check"]["AGI"]
        if val<3:
            with open("Files/Data/Job_info.json", 'r') as stat_fson:
                stat_data=json.load(stat_fson)
            global agi_txt
            current_text = canvas.itemcget(agi_txt, "text")
            # ? ====================================================
            current_number = int(current_text)
            new_number = current_number + 1
            # ? ====================================================
            with open("Files/status.json", 'w') as fson:
                data["status"][0]['agi']+=1
                data["avail_eq"][0]['str_based']-=1
                json.dump(data, fson, indent=4)
            # ? ====================================================
            stat_data["status"][1]["AGI"]+=1
            with open("Files/Data/Job_info.json", 'w') as final_stat_fson:
                json.dump(stat_data, final_stat_fson, indent=4)
            # ? ====================================================
            new_text = f"{new_number:03d}"
            canvas.itemconfig(agi_txt, text=new_text)
            with open("Files\Checks\Ability_Check.json", 'w') as fin_ability_check_file:
                ability_check_file_data["Check"]["AGI"]+=1
                json.dump(ability_check_file_data, fin_ability_check_file, indent=4)
            de_update_str()
        else:
            with open("Files/Temp Files/Urgent Temp.csv", 'w', newline='') as urgent_file:
                fr=csv.writer(urgent_file)
                fr.writerow(["AGI"])
            subprocess.Popen(['python', 'Anime Version/Urgent Quest/build/gui.py'])
            window.quit()

def update_vit():
    if int(av_str_based)!=0:
        with open("Files\Checks\Ability_Check.json", 'r') as ability_check_file:
            ability_check_file_data=json.load(ability_check_file)
            val=ability_check_file_data["Check"]["VIT"]
        if val<3:
            with open("Files/Data/Job_info.json", 'r') as stat_fson:
                stat_data=json.load(stat_fson)
            global vit_txt
            current_text = canvas.itemcget(vit_txt, "text")
            # ? ====================================================
            current_number = int(current_text)
            new_number = current_number + 1
            # ? ====================================================
            with open("Files/status.json", 'w') as fson:
                data["status"][0]['vit']+=1
                data["avail_eq"][0]['str_based']-=1
                json.dump(data, fson, indent=4)
            # ? ====================================================
            stat_data["status"][1]["VIT"]+=1
            with open("Files/Data/Job_info.json", 'w') as final_stat_fson:
                json.dump(stat_data, final_stat_fson, indent=4)
            # ? ====================================================
            new_text = f"{new_number:03d}"
            canvas.itemconfig(vit_txt, text=new_text)
            with open("Files\Checks\Ability_Check.json", 'w') as fin_ability_check_file:
                ability_check_file_data["Check"]["VIT"]+=1
                json.dump(ability_check_file_data, fin_ability_check_file, indent=4)
            de_update_str()
        else:
            with open("Files/Temp Files/Urgent Temp.csv", 'w', newline='') as urgent_file:
                fr=csv.writer(urgent_file)
                fr.writerow(["VIT"])
            subprocess.Popen(['python', 'Anime Version/Urgent Quest/build/gui.py'])
            window.quit()

def update_int():
    if int(av_int_based)!=0:
        with open("Files\Checks\Ability_Check.json", 'r') as ability_check_file:
            ability_check_file_data=json.load(ability_check_file)
            val=ability_check_file_data["Check"]["INT"]
        if val<3:
            with open("Files/Data/Job_info.json", 'r') as stat_fson:
                stat_data=json.load(stat_fson)
            global int_txt
            current_text = canvas.itemcget(int_txt, "text")
            # ? ====================================================
            current_number = int(current_text)
            new_number = current_number + 1
            # ? ====================================================
            with open("Files/status.json", 'w') as fson:
                data["status"][0]['int']+=1
                data["avail_eq"][0]['int_based']-=1
                json.dump(data, fson, indent=4)
            # ? ====================================================
            stat_data["status"][1]["INT"]+=1
            with open("Files/Data/Job_info.json", 'w') as final_stat_fson:
                json.dump(stat_data, final_stat_fson, indent=4)
            # ? ====================================================
            new_text = f"{new_number:03d}"
            canvas.itemconfig(int_txt, text=new_text)
            with open("Files\Checks\Ability_Check.json", 'w') as fin_ability_check_file:
                ability_check_file_data["Check"]["INT"]+=1
                json.dump(ability_check_file_data, fin_ability_check_file, indent=4)
            de_update_int()
        else:
            with open("Files/Temp Files/Urgent Temp.csv", 'w', newline='') as urgent_file:
                fr=csv.writer(urgent_file)
                fr.writerow(["INT"])
            subprocess.Popen(['python', 'Anime Version/Urgent Quest/build/gui.py'])
            window.quit()

def update_per():
    if int(av_int_based)!=0:
        with open("Files\Checks\Ability_Check.json", 'r') as ability_check_file:
            ability_check_file_data=json.load(ability_check_file)
            val=ability_check_file_data["Check"]["PER"]
        if val<3:
            with open("Files/Data/Job_info.json", 'r') as stat_fson:
                stat_data=json.load(stat_fson)
            global per_txt
            current_text = canvas.itemcget(per_txt, "text")
            # ? ====================================================
            current_number = int(current_text)
            new_number = current_number + 1 
            # ? ====================================================
            with open("Files/status.json", 'w') as fson:
                data["status"][0]['per']+=1
                data["avail_eq"][0]['int_based']-=1
                json.dump(data, fson, indent=4)
            # ? ====================================================
            stat_data["status"][1]["PER"]+=1
            with open("Files/Data/Job_info.json", 'w') as final_stat_fson:
                json.dump(stat_data, final_stat_fson, indent=4)
            # ? ====================================================
            new_text = f"{new_number:03d}"
            canvas.itemconfig(per_txt, text=new_text)
            with open("Files\Checks\Ability_Check.json", 'w') as fin_ability_check_file:
                ability_check_file_data["Check"]["PER"]+=1
                json.dump(ability_check_file_data, fin_ability_check_file, indent=4)
            de_update_int()
        else:
            with open("Files/Temp Files/Urgent Temp.csv", 'w', newline='') as urgent_file:
                fr=csv.writer(urgent_file)
                fr.writerow(["PER"])
            subprocess.Popen(['python', 'Anime Version/Urgent Quest/build/gui.py'])
            window.quit()

def update_man():
    if int(av_int_based)!=0:
        with open("Files\Checks\Ability_Check.json", 'r') as ability_check_file:
            ability_check_file_data=json.load(ability_check_file)
            val=ability_check_file_data["Check"]["MAN"]
        if val<3:
            with open("Files/Data/Job_info.json", 'r') as stat_fson:
                stat_data=json.load(stat_fson)
            global man_txt
            current_text = canvas.itemcget(man_txt, "text")
            # ? ====================================================
            current_number = int(current_text)
            new_number = current_number + 1
            # ? ====================================================
            with open("Files/status.json", 'w') as fson:
                data["status"][0]['man']+=1
                data["avail_eq"][0]['int_based']-=1
                json.dump(data, fson, indent=4)
            # ? ====================================================
            stat_data["status"][1]["MAN"]+=1
            with open("Files/Data/Job_info.json", 'w') as final_stat_fson:
                json.dump(stat_data, final_stat_fson, indent=4)
            # ? ====================================================
            new_text = f"{new_number:03d}"
            canvas.itemconfig(man_txt, text=new_text)
            with open("Files\Checks\Ability_Check.json", 'w') as fin_ability_check_file:
                ability_check_file_data["Check"]["MAN"]+=1
                json.dump(ability_check_file_data, fin_ability_check_file, indent=4)
            de_update_int()
        else:
            with open("Files/Temp Files/Urgent Temp.csv", 'w', newline='') as urgent_file:
                fr=csv.writer(urgent_file)
                fr.writerow(["MAN"])
            subprocess.Popen(['python', 'Anime Version/Urgent Quest/build/gui.py'])
            window.quit()

# / =================================================
# / =================================================

def de_update_str():
    global av_str_based_txt
    current_text = canvas.itemcget(av_str_based_txt, "text")
    current_number = int(current_text)
    new_number = current_number - 1
    new_text = f"{new_number:03d}"
    canvas.itemconfig(av_str_based_txt, text=new_text)

def de_update_int():
    global av_int_based_txt
    current_text = canvas.itemcget(av_int_based_txt, "text")
    current_number = int(current_text)
    new_number = current_number - 1
    new_text = f"{new_number:03d}"
    canvas.itemconfig(av_int_based_txt, text=new_text)

# / =================================================
# / =================================================
str_txt=canvas.create_text(
    63.0,
    390.0,
    anchor="nw",
    text=stre,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    106.0,
    393.0,
    anchor="nw",
    text=f"({str_buff})",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

int_txt=canvas.create_text(
    61.0,
    444.0,
    anchor="nw",
    text=intel,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    104.0,
    447.0,
    anchor="nw",
    text=f"({int_buff})",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

agi_txt=canvas.create_text(
    61.0,
    496.0,
    anchor="nw",
    text=agi,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    104.0,
    499.0,
    anchor="nw",
    text=f"({agi_buff})",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

vit_txt=canvas.create_text(
    241.0,
    390.0,
    anchor="nw",
    text=vit,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    282.0,
    393.0,
    anchor="nw",
    text=f"({vit_buff})",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

per_txt=canvas.create_text(
    248.0,
    442.0,
    anchor="nw",
    text=per,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    289.0,
    445.0,
    anchor="nw",
    text=f"({per_buff})",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

man_txt=canvas.create_text(
    254.0,
    498.0,
    anchor="nw",
    text=man,
    fill="#FFFFFF",
    font=("Montserrat SemiBold", 20 * -1)
)

canvas.create_text(
    296.0,
    500.0,
    anchor="nw",
    text=f"({man_buff})",
    fill="#34FF48",
    font=("Montserrat Regular", 15 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    45.0,
    402.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    43.0,
    456.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    44.0,
    508.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    225.0,
    402.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    229.0,
    454.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    232.0,
    510.0,
    image=image_image_12
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_str(),
    relief="flat"
)
button_1.place(
    x=147.0,
    y=393.0,
    width=20.954654693603516,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_int(),
    relief="flat"
)
button_2.place(
    x=148.0,
    y=447.0,
    width=20.954654693603516,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_agi(),
    relief="flat"
)
button_3.place(
    x=148.0,
    y=499.0,
    width=20.954654693603516,
    height=20.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_vit(),
    relief="flat"
)
button_4.place(
    x=323.0,
    y=390.0,
    width=20.954654693603516,
    height=20.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_per(),
    relief="flat"
)
button_5.place(
    x=329.0,
    y=442.0,
    width=20.954654693603516,
    height=20.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_man(),
    relief="flat"
)
button_6.place(
    x=336.0,
    y=498.0,
    width=20.954654693603516,
    height=20.0
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    53.0,
    310.0,
    image=image_image_13
)

canvas.create_text(
    72.0,
    300.0,
    anchor="nw",
    text=hp,
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    279.0,
    310.0,
    image=image_image_14
)

canvas.create_text(
    298.0,
    300.0,
    anchor="nw",
    text=mp,
    fill="#FFFFFF",
    font=("Montserrat Medium", 18 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    136.0,
    342.0,
    image=image_image_15
)

canvas.create_text(
    239.0,
    328.0,
    anchor="nw",
    text=fin_xp,
    fill="#FFFFFF",
    font=("Montserrat Medium", 16 * -1)
)

canvas.create_text(
    281.0,
    220.0,
    anchor="nw",
    text="LEVEL",
    fill="#FFFFFF",
    font=("Montserrat Regular", 24 * -1)
)

canvas.create_text(
    287.0,
    159.0,
    anchor="nw",
    text=old_lvl,
    fill="#FFFFFF",
    font=("Montserrat Bold", 60 * -1)
)

canvas.create_text(
    14.0,
    194.0,
    anchor="nw",
    text="JOB:",
    fill="#FFFFFF",
    font=("Montserrat Bold", 20 * -1)
)

canvas.create_text(
    14.0,
    228.0,
    anchor="nw",
    text="TITLE:",
    fill="#FFFFFF",
    font=("Montserrat Bold", 20 * -1)
)

canvas.create_text(
    66.0,
    195.0,
    anchor="nw",
    text=job.upper(),
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    81.0,
    229.0,
    anchor="nw",
    text=tit.upper(),
    fill=title_color(tit),
    font=("Montserrat Regular", 18 * -1)
)

canvas.create_text(
    14.0,
    161.0,
    anchor="nw",
    text="NAME:",
    fill="#FFFFFF",
    font=("Montserrat Bold", 20 * -1)
)

canvas.create_text(
    88.0,
    162.0,
    anchor="nw",
    text=name,
    fill="#FFFFFF",
    font=("Montserrat Regular", 18 * -1)
)

av_int_based_txt=canvas.create_text(
    324.0,
    610.0,
    anchor="nw",
    text=av_int_based,
    fill="#FFFFFF",
    font=("Montserrat Bold", 24 * -1)
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    256.0,
    625.0,
    image=image_image_16
)

av_str_based_txt=canvas.create_text(
    324.0,
    555.0,
    anchor="nw",
    text=av_str_based,
    fill="#FFFFFF",
    font=("Montserrat Bold", 24 * -1)
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    263.0,
    574.0,
    image=image_image_17
)

canvas.create_text(
    10.0,
    569.0,
    anchor="nw",
    text="COINS:",
    fill="#FFFFFF",
    font=("Montserrat Medium", 16 * -1)
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    91.0,
    604.0,
    image=image_image_18
)

canvas.create_text(
    44.0,
    593.0,
    anchor="nw",
    text=coins,
    fill="#FFFFFF",
    font=("Montserrat Regular", 20 * -1)
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    259.0,
    242.0,
    image=image_image_19
)

canvas.tag_bind(image_19, "<ButtonPress-1>", title_chng)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_20 = canvas.create_image(
    259.0,
    208.0,
    image=image_image_20,
    tags='Job',
    state='hidden'
)

canvas.tag_bind(image_20, "<ButtonPress-1>", start_job)

image_0=canvas.create_rectangle(
    0.0,
    0.0,
    391.0,
    35.0,
    fill="#212121",
    outline="")

canvas.tag_bind(image_0, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_0, "<B1-Motion>", move_window)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ex_close(window),
    relief="flat"
)
button_8.place(
    x=358.0,
    y=3.0,
    width=28.0,
    height=28.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: subprocess.Popen(['python', 'Anime Version/Statistics/build/gui.py']),
    relief="flat"
)
button_9.place(
    x=233.0,
    y=60.0,
    width=145.0,
    height=23.0
)

with open("Files/Data/Job_info.json", 'r') as stat_fson:
    stat_data=json.load(stat_fson)

if stat_data["status"][0]["job_active"]=='False' and lvl>=40:
    canvas.itemconfig("Job", state="normal")
else:
    canvas.itemconfig("Job", state="hiddn")

window.resizable(False, False)
window.mainloop()
