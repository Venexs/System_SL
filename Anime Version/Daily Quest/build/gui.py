
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from datetime import datetime, timedelta, date
import threading
import time
import sys
import random
import json
import csv
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

subprocess.Popen(['python', 'sfx.py'])

window = Tk()

window.geometry("477x856")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)


def update_timer(end_time):
    remaining_time = end_time - datetime.now()

    if remaining_time.days < 0:
        window.quit()

    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    timer_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer, text=timer_text)

    window.after(1000, update_timer, end_time)

with open("Files/Data/Daily_Quest.json", 'r') as daily_quest_file:
    daily_quest_data=json.load(daily_quest_file)
    # ? =======================================================
    # ? Players
    pl_push=daily_quest_data["Player"]["Push"]
    pl_sit=daily_quest_data["Player"]["Sit"]
    pl_sqat=daily_quest_data["Player"]["Squat"]
    pl_run=daily_quest_data["Player"]["Run"]

    pl_int=daily_quest_data["Player"]["Int_type"]
    pl_slp=daily_quest_data["Player"]["Sleep"]
    # ? =======================================================
    # ? Final
    fl_push=daily_quest_data["Final"]["Push"]
    fl_sit=daily_quest_data["Final"]["Sit"]
    fl_sqat=daily_quest_data["Final"]["Squat"]
    fl_run=daily_quest_data["Final"]["Run"]

    fl_int=daily_quest_data["Final"]["Int_type"]
    fl_slp=daily_quest_data["Final"]["Sleep"]
    # ? =======================================================

with open("Files/status.json", 'r') as rank_check_file:
    rank_check_data=json.load(rank_check_file)
    lvl=rank_check_data["status"][0]['level']

    if lvl>=1 and lvl<=10:
        rank="E"
    elif lvl>=11 and lvl<=20:
        rank="D"
    elif lvl>=21 and lvl<=30:
        rank="C"
    elif lvl>=31 and lvl<=45:
        rank="B"
    elif lvl>=46 and lvl<=65:
        rank="A"
    elif lvl>=66 and lvl<=80:
        rank="S"
    elif lvl>=81 and lvl<=90:
        rank="SS"
    elif lvl>=91 and lvl<=100:
        rank="SSS"
    elif lvl>=101:
        rank="National"

def check_comp():
    with open("Files/Data/Daily_Quest.json", 'r') as daily_quest_file:
        daily_quest_data=json.load(daily_quest_file)
        # ? =======================================================
        # ? Players
        pl_push=daily_quest_data["Player"]["Push"]
        pl_sit=daily_quest_data["Player"]["Sit"]
        pl_sqat=daily_quest_data["Player"]["Squat"]
        pl_run=daily_quest_data["Player"]["Run"]

        pl_int=daily_quest_data["Player"]["Int_type"]
        pl_slp=daily_quest_data["Player"]["Sleep"]
        # ? =======================================================
        # ? Final
        fl_push=daily_quest_data["Final"]["Push"]
        fl_sit=daily_quest_data["Final"]["Sit"]
        fl_sqat=daily_quest_data["Final"]["Squat"]
        fl_run=daily_quest_data["Final"]["Run"]

        fl_int=daily_quest_data["Final"]["Int_type"]
        fl_slp=daily_quest_data["Final"]["Sleep"]
        # ? =======================================================

    if pl_push>=fl_push and pl_run>=fl_run and pl_sqat>=fl_sqat and pl_sit>=fl_sit and pl_int>=fl_int and pl_slp>=fl_slp:
        if fl_push!=100 and fl_sit!=100 and fl_sqat!=100:
            daily_quest_data["Final"]["Push"]+=5
            daily_quest_data["Final"]["Sit"]+=5
            daily_quest_data["Final"]["Squat"]+=5
            daily_quest_data["Final"]["Run"]+=0.5
            if round(fl_int,1)!=10:
                daily_quest_data["Final"]["Int_type"]+=0.5
            else:
                daily_quest_data["Final"]["Int_type"]+=0.5

            with open("Files/Checks/Daily_time_check.csv", 'w',  newline='') as fin_daily_date_check_file:
                fw1=csv.writer(fin_daily_date_check_file)
                fw1.writerow([today_date_str,"DONE"])
        
            subprocess.Popen(['python', 'Anime Version/Daily Quest Rewards/gui.py'])
            
            window.quit()

def update_pushup():
    global pushup_txt
    current_text=int((((canvas.itemcget(pushup_txt, "text")).split("/"))[0])[1:])
    print(current_text)
    with open("Files/Data/Daily_Quest.json", 'w') as write_daily_quest_file:
        daily_quest_data["Player"]["Push"]+=1
        json.dump(daily_quest_data, write_daily_quest_file, indent=4)
    canvas.itemconfig(pushup_txt, text=f"[{current_text+1}/{fl_push}]")
    check_comp()

def update_situp():
    global situp_txt
    current_text=int((((canvas.itemcget(situp_txt, "text")).split("/"))[0])[1:])
    with open("Files/Data/Daily_Quest.json", 'w') as write_daily_quest_file:
        daily_quest_data["Player"]["Sit"]+=1
        json.dump(daily_quest_data, write_daily_quest_file, indent=4)
    canvas.itemconfig(situp_txt, text=f"[{current_text+1}/{fl_sit}]")
    check_comp()

def update_sqat():
    global squat_txt
    current_text=int((((canvas.itemcget(squat_txt, "text")).split("/"))[0])[1:])
    with open("Files/Data/Daily_Quest.json", 'w') as write_daily_quest_file:
        daily_quest_data["Player"]["Squat"]+=1
        json.dump(daily_quest_data, write_daily_quest_file, indent=4)
    canvas.itemconfig(squat_txt, text=f"[{current_text+1}/{fl_sqat}]")
    check_comp()

def update_run():
    global run_txt
    current_text=float((((canvas.itemcget(run_txt, "text")).split("/"))[0])[1:])
    with open("Files/Data/Daily_Quest.json", 'w') as write_daily_quest_file:
        daily_quest_data["Player"]["Run"]+=0.5
        json.dump(daily_quest_data, write_daily_quest_file, indent=4)
    canvas.itemconfig(run_txt, text=f"[{current_text+0.5}/{fl_run}]")
    check_comp()

def update_int():
    global int_txt
    current_text=int((((canvas.itemcget(int_txt, "text")).split("/"))[0])[1:])
    with open("Files/Data/Daily_Quest.json", 'w') as write_daily_quest_file:
        daily_quest_data["Player"]["Int_type"]+=0.5
        json.dump(daily_quest_data, write_daily_quest_file, indent=4)
    canvas.itemconfig(int_txt, text=f"[{current_text+0.5}/{fl_int}]")
    check_comp()

def update_sleep():
    global sleep_txt
    current_text=int((((canvas.itemcget(sleep_txt, "text")).split("/"))[0])[1:])
    with open("Files/Data/Daily_Quest.json", 'w') as write_daily_quest_file:
        daily_quest_data["Player"]["Sleep"]+=1
        json.dump(daily_quest_data, write_daily_quest_file, indent=4)
    canvas.itemconfig(sleep_txt, text=f"[{current_text+1}/{fl_slp}]")
    check_comp()

def preview():
    subprocess.Popen(['python', 'Anime Version/Daily Quest Preview/build/gui.py'])

    window.quit()

try:
    with open("Files/Checks/Daily_time_check.csv", 'r') as Daily_date_check_file:
        fr=csv.reader(Daily_date_check_file)
        for k in fr:
            date_old=k[0]
            rew_check=k[1]

except:
    full_check=False
    rew_check="False"

today = date.today()
today_date_str = today.strftime("%Y-%m-%d")

try:
    date_from_string = datetime.strptime(date_old, "%Y-%m-%d").date()
except:
    date_from_string = today - timedelta(days = 2)


if date_from_string < today:
    full_check=False
    with open("Files/Checks/Daily_time_check.csv", 'w',  newline='') as fin_daily_date_check_file:
        fw1=csv.writer(fin_daily_date_check_file)
        fw1.writerow([today_date_str,"UNDONE"])

elif date_from_string==today:
    if pl_push>=fl_push and pl_run>=fl_run and pl_sqat>=fl_sqat and pl_sit>=fl_sit and pl_int>=fl_int and pl_slp>=fl_slp:
        full_check=True

if full_check==False:

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 856,
        width = 477,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        277.0,
        428.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        244.0,
        445.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        241.0,
        154.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        244.0,
        246.0,
        image=image_image_4
    )

    timer=canvas.create_text(
        128.0,
        700.0,
        anchor="nw",
        text="00:00:00",
        fill="#FFFFFF",
        font=("Montserrat Bold", 48 * -1)
    )

    canvas.create_text(
        91.0,
        194.0,
        anchor="nw",
        text="[Daily Quest: Player Training has arrived]",
        fill="#FFFFFF",
        font=("Montserrat Regular", 15 * -1)
    )

    canvas.create_text(
        86.0,
        296.0,
        anchor="nw",
        text="Push-ups",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    canvas.create_text(
        86.0,
        336.0,
        anchor="nw",
        text="Sit-ups",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    canvas.create_text(
        86.0,
        375.0,
        anchor="nw",
        text="Squats",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    canvas.create_text(
        86.0,
        415.0,
        anchor="nw",
        text="Running",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    canvas.create_text(
        86.0,
        472.0,
        anchor="nw",
        text="Chapter Reading",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    canvas.create_text(
        86.0,
        511.0,
        anchor="nw",
        text="Proper Last Night Sleep",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    pushup_txt=canvas.create_text(
        315.0,
        298.0,
        anchor="nw",
        text=f"[{pl_push}/{fl_push}]",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    situp_txt=canvas.create_text(
        315.0,
        336.0,
        anchor="nw",
        text=f"[{pl_sit}/{fl_sit}]",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    squat_txt=canvas.create_text(
        315.0,
        374.0,
        anchor="nw",
        text=f"[{pl_sqat}/{fl_sqat}]",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    run_txt=canvas.create_text(
        313.0,
        415.0,
        anchor="nw",
        text=f"[{pl_run}/{fl_run}km]",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    int_txt=canvas.create_text(
        333.0,
        472.0,
        anchor="nw",
        text=f"[{pl_int}/{fl_int}]",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    sleep_txt=canvas.create_text(
        334.0,
        511.0,
        anchor="nw",
        text=f"[{pl_slp}/{fl_slp}]",
        fill="#FFFFFF",
        font=("Montserrat Regular", 14 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        242.0,
        415.0,
        image=image_image_5
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_pushup(),
        relief="flat"
    )
    button_1.place(
        x=380.0,
        y=296.0,
        width=20.0,
        height=20.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_situp(),
        relief="flat"
    )
    button_2.place(
        x=380.0,
        y=336.0,
        width=20.0,
        height=20.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_sqat(),
        relief="flat"
    )
    button_3.place(
        x=380.0,
        y=373.0,
        width=20.0,
        height=20.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_run(),
        relief="flat"
    )
    button_4.place(
        x=380.0,
        y=415.0,
        width=20.0,
        height=20.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_int(),
        relief="flat"
    )
    button_5.place(
        x=380.0,
        y=472.0,
        width=20.0,
        height=20.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_sleep(),
        relief="flat"
    )
    button_6.place(
        x=382.0,
        y=510.0,
        width=20.0,
        height=20.0
    )

    canvas.create_text(
        96.0,
        562.0,
        anchor="nw",
        text="Preview Rewards",
        fill="#FFFFFF",
        font=("Montserrat Light", 13 * -1)
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: preview(),
        relief="flat"
    )
    button_7.place(
        x=73.0,
        y=559.0,
        width=20.0,
        height=20.0
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        244.0,
        650.0,
        image=image_image_6
    )
    end_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    update_timer(end_time)

else:
    if rew_check=="True":
        subprocess.Popen(['python', 'Anime Version/Quest Complete/build/gui.py'])
        window.quit()
    else:
        subprocess.Popen(['python', 'Anime Version/Daily Quest Rewards/gui.py'])
        window.quit()

window.resizable(False, False)
window.mainloop()
