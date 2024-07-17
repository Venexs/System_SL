
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import cv2
from PIL import Image, ImageTk
import subprocess
import json

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

subprocess.Popen(['python', 'sfx.py'])

window.geometry("568x109")
window.configure(bg = "#FFFFFF")
window.attributes('-alpha',0.8)
window.wm_attributes("-topmost", True)
window.overrideredirect(True)

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

with open("Files/status.json", 'r') as fson:
    data=json.load(fson)
    data["status"][0]['level']+=1
    data["status"][0]['str']+=1
    data["status"][0]['agi']+=1
    data["status"][0]['vit']+=1
    data["status"][0]['int']+=1
    data["status"][0]['per']+=1
    data["status"][0]['hp']+=10
    data["status"][0]['mp']+=10

with open("Files/status.json", 'w') as fson:
    json.dump(data, fson, indent=4)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 109,
    width = 568,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    341.0,
    364.0,
    image=image_image_1
)

video_path = "Files/0001-0200.mp4"
player = VideoPlayer(canvas, video_path, 430.0, 263.0)

canvas.create_text(
    140.0,
    35.0,
    anchor="nw",
    text="Leveled Up!",
    fill="#FFFFFF",
    font=("Montserrat Medium", 48 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    285.0,
    68.0,
    image=image_image_2
)

image_0=canvas.create_rectangle(
    0.0,
    0.0,
    596.0,
    28.0,
    fill="#2E2E2E",
    outline="")

canvas.tag_bind(image_0, "<ButtonPress-1>", start_move)
canvas.tag_bind(image_0, "<B1-Motion>", move_window)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ex_close(window),
    relief="flat"
)
button_1.place(
    x=538.0,
    y=3.0,
    width=23.0,
    height=23.0
)
window.resizable(False, False)
window.mainloop()
