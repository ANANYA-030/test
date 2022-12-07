from tkinter import *
from tkVideoPlayer import TkinterVideo
import time
from ffpyplayer.player import MediaPlayer
window=Tk()


'''
videoplayer.load(r"Faded.mp4")
videoplayer.pack(expand=True,fill="both")
player=MediaPlayer("Faded.mp4")
val=''
play_value=True
# videoplayer.play()
'''
  videoplayer=TkinterVideo(master=window,scaled=True)
  videoplayer.load(r"spyxfamily-1.Mkv")
  videoplayer.pack(expand=True,fill="both")
  videoplayer.play()
  return True;
  player=MediaPlayer("spyxfamily-1.Mkv") 

window.mainloop()
'''
val=''
while val!='eof':
  frame,val=player.get_frame()
  if val!='eof' and frame is not None and videoplayer.play:
    img,t=frame
window.mainloop()
'''
'''
window=Tk()
print("inside")
bvPlayer("Faded.mp4", dim = (854, 480), videoOptions = True)
'''
# print("inside 2")
# videoplayer.load(r"Faded.mp4")
# videoplayer.pack(expand=True,fill="both")
# videoplayer.play()
# print("inside 3")
# window.mainloop()
