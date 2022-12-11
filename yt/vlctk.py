import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter import Canvas
from tkinter import *
import vlc

root = tk.Tk()
root.title("Reactor Suite")

# Create a label
label = Label(root, text = "Draw!", font =("Arial Bold", 20)) 
label.pack()

def open_file():
    global video_file
    video_file = filedialog.askopenfilename(title="Select video file", filetypes=[("MP4 files", "*.mp4")])
    if video_file == '':
        messagebox.showerror("Error", "No file selected")
    else:
        play_video()


def close_window():
    root.destroy()

# Create a button
def play_video():
    instance = vlc.Instance("--no-xlib")
    media = instance.media_player_new(video_file)
    media.set_hwnd(root.winfo_id())
    media.play()

# play_button = Button(root, text="Play Video", width=20, command=play_video)
# play_button.pack()

# Create a menu
menu = Menu(root) 
root.config(menu=menu)

# file
file_menu = Menu(menu, tearoff=0) 
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=close_window)
menu.add_cascade(label='File', menu=file_menu) 

# edit
edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=edit_menu)

# options
options_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Options', menu=options_menu)

# view
view_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='View', menu=view_menu)
def new_file():
    canvas.delete("all")



# pen menu
# //////////
# //////////
# //////////

# This function is called when the user clicks the mouse
def draw(event):
  # Get the coordinates of the mouse event
  x, y = event.x, event.y

  global last_x, last_y

  # If this is the first mouse event, do not draw a line
  if last_x is None:
    last_x, last_y = x, y
    return

  # Draw a line from the previous mouse event to the current event
  canvas.create_line(last_x, last_y, x, y, fill="red")

  # Update the global variables with the current event coordinates
  last_x, last_y = x, y

# # Create a Canvas widget
# canvas = Canvas(root, width=640, height=480, highlightthickness=0)
# canvas.pack()

# # Bind the left mouse button click event to the `draw` function
# canvas.bind("<B1-Motion>", draw)

# # Create a global variable to store the coordinates of the last mouse event
# last_x, last_y = None, None

# # run tkinter window
# root.mainloop()

# # Bind the left mouse button click event to the `draw` function
# canvas.bind("<B1-Motion>", draw)

# # Create a global variable to store the coordinates of the last mouse event
# last_x, last_y = None, None

# # run tkinter window
# root.mainloop()



# This function is called when the user clicks the mouse
def release(event):
  # Get the coordinates of the mouse event
  global last_x, last_y

  # Reset the global variables so the next mouse event will draw a new line
  last_x, last_y = None, None

# This function is called when the user clicks the mouse
def draw(event):
  # Get the coordinates of the mouse event
  x, y = event.x, event.y

  global last_x, last_y

  # If this is the first mouse event, do not draw a line
  if last_x is None:
    last_x, last_y = x, y
    return

  # Draw a line from the previous mouse event to the current event
  canvas.create_line(last_x, last_y, x, y, fill="red")

  # Update the global variables with the current event coordinates
  last_x, last_y = x, y

# Create a Canvas widget
canvas = Canvas(root, width=640, height=480, highlightthickness=0)
canvas.pack()

# Bind the left mouse button click event to the `draw` function
canvas.bind("<B1-Motion>", draw)

# Bind the left mouse button release event to the `release` function
canvas.bind("<ButtonRelease-1>", release)

# Create a global variable to store the coordinates of the last mouse event
last_x, last_y = None, None

# run tkinter window
root.mainloop()