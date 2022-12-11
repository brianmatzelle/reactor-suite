import vlc
import pafy
from time import sleep

# url of the video
url = "https://www.youtube.com/watch?v=H68bRnxNYFs"

# creating pafy object of the video
video = pafy.new(url)

# getting best stream
best = video.getbest()

# creating vlc media player object
media = vlc.MediaPlayer(best.url)

# start playing video
media.play()
sleep(5) # Or however long you expect it to take to open vlc
while media.is_playing():
     sleep(1)