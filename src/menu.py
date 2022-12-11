import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import cv2
import numpy as np
from PIL import ImageTk

# Create the window
window = tk.Tk()
window.title('Video Player')
window.geometry('800x600')

# Create the functions
def open_file():
    global video_file
    video_file = filedialog.askopenfilename(title="Select video file", filetypes=[("MP4 files", "*.mp4")])
    if video_file == '':
        messagebox.showerror("Error", "No file selected")
    else:
        play()

def close_window():
    window.destroy()

def erase_drawing():
    canvas.delete('all')

def change_pen_size():
    size = window.simpledialog.askinteger("Pen size", "Enter pen size:",
                                   parent=window,
                                   minvalue=1, maxvalue=20)
    if size is not None:
        canvas.configure(width=size)

def zoom_in():
    canvas.scale("all", event.x, event.y, 1.1, 1.1)

def zoom_out():
    canvas.scale("all", event.x, event.y, 0.9, 0.9)

def play():
    global frame_num
    video = cv2.VideoCapture(video_file)
    while True:
        video.set(cv2.CAP_PROP_POS_MSEC, frame_num)
        success, image = video.read()
        if success:
            frame_num += 1000 // frame_rate
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, image=image, anchor=tk.NW)
            canvas.bind("<Button-1>", draw)
            window.update_idletasks()
            window.update()
        else:
            break
    video.release()

def pause():
    pass

def rewind():
    global frame_num
    frame_num -= 5000 // frame_rate

def fast_forward():
    global frame_num
    frame_num += 5000 // frame_rate

def draw(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black")

def help():
    messagebox.showinfo("Help", "Use the menu bar to change drawing settings and playback controls.")

# Create the menu bar
menubar = Menu(window)

# Create the file menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Exit", command=close_window)
menubar.add_cascade(label="File", menu=filemenu)

# Create the edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Erase", command=erase_drawing)
editmenu.add_command(label="Pen Size", command=change_pen_size)
menubar.add_cascade(label="Edit", menu=editmenu)

# Create the options menu
optionsmenu = Menu(menubar, tearoff=0)
optionsmenu.add_command(label="Zoom In", command=zoom_in)
optionsmenu.add_command(label="Zoom Out", command=zoom_out)
menubar.add_cascade(label="Options", menu=optionsmenu)

# Create the view menu
viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Play", command=play)
viewmenu.add_command(label="Pause", command=pause)
viewmenu.add_command(label="Rewind", command=rewind)
viewmenu.add_command(label="Fast Forward", command=fast_forward)
menubar.add_cascade(label="View", menu=viewmenu)

# Create the help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

# Create the main frame
main_frame = tk.Frame(window, bg='gray')
main_frame.pack()

# Create the drawing canvas
canvas = tk.Canvas(main_frame, bg='white', width=800, height=600)
canvas.pack()

# Create the video playback controls
play_button = tk.Button(main_frame, text='Play', command=play)
play_button.pack(side=tk.LEFT)

pause_button = tk.Button(main_frame, text='Pause', command=pause)
pause_button.pack(side=tk.LEFT)

rewind_button = tk.Button(main_frame, text='Rewind', command=rewind)
rewind_button.pack(side=tk.LEFT)

fast_forward_button = tk.Button(main_frame, text='Fast Forward', command=fast_forward)
fast_forward_button.pack(side=tk.LEFT)

# Create the global variables
video_file = None
frame_num = 0
frame_rate = 25

# Run the program
window.mainloop()