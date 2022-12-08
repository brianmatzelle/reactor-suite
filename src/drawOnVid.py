# Import necessary libraries
import cv2
from ffpyplayer.player import MediaPlayer
import time

# Open the video file using OpenCV's VideoCapture function
path = "data/input.mp4"
video = cv2.VideoCapture(path)
player = MediaPlayer(path)

# Check if the video was successfully opened
if not video.isOpened():
    print("Error opening video file!")

# Define a color for the drawing
color = (0, 0, 255)

# Create a variable to track the current position of the mouse
mouse_pos = (0, 0)

# Create a variable to track whether the mouse is currently pressed
mouse_pressed = False

# Create a variable to store the points of the drawing
points = []


# Define a mouse callback function that will be called whenever the mouse is clicked or moved
def mouse_callback(event, x, y, flags, param):
    global mouse_pos, mouse_pressed

    # If the left mouse button is pressed, set the mouse_pressed variable to True
    # and store the current position of the mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pos = (x, y)
        mouse_pressed = True

    # If the left mouse button is released, set the mouse_pressed variable to False
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False

    # If the mouse is moved while the left button is pressed, add the current position
    # of the mouse to the points list and update the mouse_pos variable
    elif event == cv2.EVENT_MOUSEMOVE and mouse_pressed:
        points.append(mouse_pos)
        mouse_pos = (x, y)

# Set the update rate for the drawing, in seconds
update_rate = 0.01

# Create a timer to track the time since the last update
last_update = time.time()

# Loop through the video frame by frame
while video.isOpened():
    # Read the current frame of the video
    success, frame = video.read()
    audio_frame, val = player.get_frame()

    # If there are no more frames in the video, break out of the loop
    if not success:
        break

    # Check if the update rate has been reached
    current_time = time.time()
    elapsed_time = current_time - last_update
    if elapsed_time >= update_rate:
        # If the update rate has been reached, update the drawing and reset the timer
        for i in range(1, len(points)):
            cv2.line(frame, points[i - 1], points[i], color, thickness=5)
        last_update = current_time

    # Show the frame with the drawing on it
    cv2.imshow("Frame", frame)

    # Set the mouse callback function for the frame
    cv2.setMouseCallback("Frame", mouse_callback)

    # Use a long delay in the waitKey function to keep the video playing at the correct speed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Clean up
video.release()
cv2.destroyAllWindows()
