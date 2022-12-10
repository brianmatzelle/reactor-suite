import tkinter as tk 
import cv2
import threading

#creating window
window = tk.Tk()
window.title("MP4 Player with Drawing")
window.geometry("800x600")

#create frame
frame = tk.Frame(window)
frame.grid(row = 0, column = 0)

#create canvas
canvas = tk.Canvas(frame, width = 800, height = 600,background = "black")
canvas.grid(row = 0, column = 0)

#playback control variables
play_status = 0

#drawing functions
def draw_circle(x, y):
    canvas.create_oval(x-5, y-5, x+5, y+5, fill = "white")

def draw_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill = "white")

def draw_rectangle(x, y):
    canvas.create_rectangle(x-5, y-5, x+5, y+5, fill = "white")

#threading
class VideoThread(threading.Thread): 
    def __init__(self, threadID, name, counter): 
        threading.Thread.__init__(self) 
        self.threadID = threadID 
        self.name = name 
        self.counter = counter 
    def run(self): 
        print ("Starting " + self.name) 
        play_video() 
        print ("Exiting " + self.name) 

def play_video():
    global play_status
    #open video file
    video_file = cv2.VideoCapture("video.mp4")

    #video playback loop
    while video_file.isOpened():
        #capture frame-by-frame
        ret, frame = video_file.read()
        if ret == True:
            #show frame in canvas
            canvas.create_image(0, 0, image = frame, anchor = tk.NW)
            if play_status == 0:
                video_file.set(cv2.CAP_PROP_POS_FRAMES, 0)
            if play_status == 1:
                video_file.set(cv2.CAP_PROP_POS_MSEC, (video_file.get(cv2.CAP_PROP_POS_MSEC)+1000))
            if play_status == 2:
                video_file.set(cv2.CAP_PROP_POS_FRAMES, (video_file.get(cv2.CAP_PROP_POS_FRAMES)+1))
            window.update()
        else:
            break
    video_file.release()

#play and pause button
def play_pause_button():
    global play_status
    if play_status == 0:
        play_status = 1
        play_pause_btn.configure(text = "Pause")
    else:
        play_status = 0
        play_pause_btn.configure(text = "Play")

#rewind button
def rewind_button():
    global play_status
    play_status = 0
    play_pause_btn.configure(text = "Play")

#creating buttons
play_pause_btn = tk.Button(window, text = "Play", command = play_pause_button)
play_pause_btn.grid(row = 1, column = 0)

rewind_btn = tk.Button(window, text = "Rewind", command = rewind_button)
rewind_btn.grid(row = 1, column = 1)

#mouse events
def mouse_down(event):
    x = event.x
    y = event.y
    draw_circle(x, y)

def mouse_move(event):
    x = event.x
    y = event.y
    draw_line(x, y, x + 5, y + 5)

def mouse_up(event):
    x = event.x
    y = event.y
    draw_rectangle(x, y)

#binding mouse events
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<B1-Motion>", mouse_move)
canvas.bind("<ButtonRelease-1>", mouse_up)

#create and start thread
thread1 = VideoThread(1, "Thread-1", 1) 
thread1.start()

#run mainloop
window.mainloop()