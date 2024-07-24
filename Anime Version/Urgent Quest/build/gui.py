
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

subprocess.Popen(['python', 'sfx.py'])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("741x239")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)

def complete():
    with open("Files\Checks\Ability_Check.json", 'r') as ability_check_file:
        ability_check_file_data=json.load(ability_check_file)
    
    with open("Files\Checks\Ability_Check.json", 'w') as fin_ability_check_file:
        ability_check_file_data["Check"][abi]=0
        json.dump(ability_check_file_data, fin_ability_check_file, indent=4)

    with open("Files/Data/Job_info.json", 'r') as stat_fson:
        stat_data=json.load(stat_fson)

    stat_data["status"][1][abi]+=1
    with open("Files/Data/Job_info.json", 'w') as final_stat_fson:
        json.dump(stat_data, final_stat_fson, indent=4)

    if abi_l in ["str",'vit','agi']:
        abi_2="str_based"
    elif abi_l in ["int",'per','man']:
        abi_2="int_based"
    
    with open("Files/status.json", 'r') as fson:
        data=json.load(fson)
        abi_l=abi.lower()
        data["status"][0][abi_l]+=1
        data["avail_eq"][0][abi_2]-=1

    with open("Files/status.json", 'w') as fin_fson:
        json.dump(data, fin_fson, indent=4)

    subprocess.Popen(['python', 'Anime Version/Status Tab/build/gui.py'])
    window.quit()

with open("Files/Temp Files/Urgent Temp.csv", 'r') as urgent_file:
    fr=csv.reader(urgent_file)
    for k in fr:
        abi=k[0]

desc1=desc2=desc3=''
segments = []
segment_length = 77

file_name=f"Files\Workout\{abi}_based.json"
with open(file_name, 'r') as workout_file:
    workout_file_data=json.load(workout_file)
    workout_file_list=list(workout_file_data.keys())

    name=random.choice(workout_file_list)

    desc_full=workout_file_data[name][0]["desc"]

    for i in range(0, len(desc_full), segment_length):
        segments.append(desc_full[i:i+segment_length])

    if len(segments) >= 1:
        desc1 = segments[0]
    if len(segments) >= 2:
        desc2 = segments[1]
    if len(segments) >= 3:
        desc3 = segments[2]
    
    both_check=False
    one_check=False
    time_check=False

    amt1=amt2=''
    amt1_val=amt2_val=''

    if "amt" in workout_file_data[name][0]:
        one_check=True
        amt1=workout_file_data[name][0]["amt"]
        amt1_val=workout_file_data[name][0]["amtval"]
        if "time" in workout_file_data[name][0]:
            both_check=True
            time_check=True
            amt2=workout_file_data[name][0]["time"]
            amt2_val=workout_file_data[name][0]["timeval"]

    if "time" in workout_file_data[name][0]:
        time_check=True
        amt2=workout_file_data[name][0]["time"]
        amt2_val=workout_file_data[name][0]["timeval"]
        if "amt" in workout_file_data[name][0]:
            one_check=True
            both_check=True
            amt1=workout_file_data[name][0]["amt"]
            amt1_val=workout_file_data[name][0]["amtval"]

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 239,
    width = 741,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    405.0,
    198.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    370.0,
    120.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    378.0,
    37.0,
    image=image_image_3
)

canvas.create_text(
    45.0,
    62.0,
    anchor="nw",
    text="Do the below mentioned exercise for as much as it is mentioned within the time-limit ",
    fill="#FFFFFF",
    font=("Montserrat Regular", 15 * -1)
)

canvas.create_text(
    45.0,
    81.0,
    anchor="nw",
    text=f"to increase the {abi} ability",
    fill="#FFFFFF",
    font=("Montserrat Regular", 15 * -1)
)

canvas.create_text(
    45.0,
    101.0,
    anchor="nw",
    text=f"[{name}]",
    fill="#FFFFFF",
    font=("Montserrat Bold", 20 * -1)
)

if one_check==True and both_check==False:
    canvas.create_text(
        45.0,
        130.0,
        anchor="nw",
        text=f"For, {amt1} {amt1_val}",
        fill="#FFFFFF",
        font=("Montserrat Regular", 13 * -1)
    )

elif time_check==True and both_check==False:
    canvas.create_text(
        45.0,
        130.0,
        anchor="nw",
        text=f"For, {amt2} {amt2_val}",
        fill="#FFFFFF",
        font=("Montserrat Regular", 13 * -1)
    )

elif both_check==True:
    canvas.create_text(
        45.0,
        130.0,
        anchor="nw",
        text=f"For, {amt1} {amt1_val}",
        fill="#FFFFFF",
        font=("Montserrat Regular", 13 * -1)
    )
    canvas.create_text(
        225.0,
        130.0,
        anchor="nw",
        text=f"And for {amt2} {amt2_val}",
        fill="#FFFFFF",
        font=("Montserrat Regular", 13 * -1)
    )

canvas.create_text(
    45.0,
    151.0,
    anchor="nw",
    text=desc1,
    fill="#FFFFFF",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    45.0,
    165.0,
    anchor="nw",
    text=desc2,
    fill="#FFFFFF",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    45.0,
    179.0,
    anchor="nw",
    text=desc3,
    fill="#FFFFFF",
    font=("Montserrat Regular", 10 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: complete(),
    relief="flat"
)
button_1.place(
    x=551.0,
    y=207.0,
    width=137.0,
    height=19.0
)
window.resizable(False, False)
window.mainloop()
