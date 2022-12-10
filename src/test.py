import tkinter
import pygame
from PIL import Image, ImageTk
from pygame import *

# window size
window_width = 800
window_height = 600

# Setup the window
root = tkinter.Tk()
root.title("MP4 Player")
root.geometry('%dx%d+%d+%d' % (window_width, window_height, 0, 0))

# Create the canvas for drawing on the video
canvas = tkinter.Canvas(root, width=window_width, height=window_height, cursor="cross")
canvas.pack()

# Initialize pygame
pygame.init()

# Load the mp4 file
movie = pygame.movie.Movie("video.mp4")

# Get the size of the video
movie_width = movie.get_size()[0]
movie_height = movie.get_size()[1]

# Scale the video to the window size
scale_x = window_width / movie_width
scale_y = window_height / movie_height

# Create the video surface
video_surface = pygame.Surface((movie_width, movie_height))

# Create the drawing surface
draw_surface = pygame.Surface((movie_width, movie_height))

# Initialize the pen size and color
pen_size = 1
pen_color = (0, 0, 0)

# Create the menu bar
menu_bar = tkinter.Menu(root)

# File menu
file_menu = tkinter.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tkinter.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_drawing)
edit_menu.add_command(label="Clear", command=clear_drawing)
edit_menu.add_command(label="Pen Size", command=change_pen_size)
edit_menu.add_command(label="Pen Color", command=change_pen_color)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Options menu
options_menu = tkinter.Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Zoom in", command=zoom_in)
options_menu.add_command(label="Zoom out", command=zoom_out)
menu_bar.add_cascade(label="Options", menu=options_menu)

# Help menu
help_menu = tkinter.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=open_help_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Set the menu bar
root.config(menu=menu_bar)

# Play the video
movie.play()

while True:
    # Get the current movie frame
    movie_frame = movie.get_current_frame()

    # Convert the frame to a PIL image
    frame_image = Image.fromstring("RGB", (movie_width, movie_height), movie_frame)

    # Convert the PIL image to a Tkinter image
    frame_image_tk = ImageTk.PhotoImage(frame_image)

    # Draw the Tkinter image on the canvas
    canvas.create_image(0, 0, image=frame_image_tk, anchor="nw")

    # Get the user input
    for event in pygame.event.get():
        # Check for quit
        if event.type == pygame.QUIT:
            pygame.quit()
            root.quit()
            exit()

        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            # Spacebar for pause/play
            if event.key == pygame.K_SPACE:
                if movie.get_busy():
                    movie.pause()
                else:
                    movie.play()

            # Left arrow for rewind 5 seconds
            elif event.key == pygame.K_LEFT:
                movie.rewind()

            # Right arrow for fast forward 5 seconds
            elif event.key == pygame.K_RIGHT:
                movie.forward()

        # Check for mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Draw on the video
            draw_on_video(mouse_pos)

        # Check for scroll wheel events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                # Scroll up for zoom in
                zoom_in()
            elif event.button == 5:
                # Scroll down for zoom out
                zoom_out()

    # Update the video surface
    video_surface.blit(frame_image_tk, (0, 0))

    # Draw the drawing surface on the video surface
    video_surface.blit(draw_surface, (0, 0))

    # Flip the display
    pygame.display.flip()

# Cleanup
pygame.quit()
root.quit()