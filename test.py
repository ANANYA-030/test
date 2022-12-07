from tkinter import *
#from PIL import ImageTk,Image
from tkVideoPlayer import TkinterVideo


window=Tk()
window.geometry("650x548")
window.title("Anime streaming application")
window.config(background="black")

canvas= Canvas(window,height=548,width=650)
'''
def resizer(e):
  global bg1,resized_bg,new_bg
  bg1=Image.open('galaxy.png')
  resized_bg=bg1.resize((e.width,e.height),Image.ANTIALIAS)
  new_bg=ImageTk.PhotoImage(resized_bg)
  canvas.create_image(0,0,image=new_bg,anchor='nw')
'''
def click():
  welcomeText.destroy()
  button.destroy()
  animePage()

def spyPlay():
  videoplayer= TkinterVideo(master=canvas,scaled=True)
  videoplayer.load(r"spyxfamily-1.Mkv")
  videoplayer.pack(expand=True,fill="both")
  videoplayer.play()
  

def animePage(): 
  def animePlay():
    canvas.delete("all")
    canvas.create_image(0,0,image=background_photo,anchor='nw')
    canvas.create_text(160,40,text="SPY X FAMILY",font=("Helvetica",35,'bold'),fill='red')
    canvas.create_text(140,120,text=" Genres:Action,Comedy\n Status:Completed\n Ep total:12",font=("Helvetica",20),fill='Pink')
    canvas.create_text(70,220,text="EPISODES",font=("Helvetica",20,'bold'),fill='orange')
    ep_btn=Button(canvas,text="EPISODE 1",bg="#28F608",borderwidth=3,command=spyPlay)
    ep_btn_window=canvas.create_window(50,250,window=ep_btn)
    '''
    frame = Frame(canvas)
    frame.place(x=20,y=240)
    List=["Adele.mp4","Faded.mp4"]
    for i in range(1,4):
      Button(frame,text="EPISODE"+str(i),bg="green",borderwidth=3,command=count(List[i-1])).pack()
     '''
    window.mainloop()

  #background_photo=ImageTk.PhotoImage(file='galaxy.png')
  background_photo=PhotoImage(file='galaxy.png')
  spy1=PhotoImage(file='spy.png')
  # canvas= Canvas(window,height=548,width=650)
  canvas.pack(fill='both',expand = True)
  canvas.create_image(0,0,image=background_photo,anchor='nw')
  canvas.create_text(320,40,text="ANIME-STREAMING",font=("Helvetica",35),fill='white')
  canvas.create_image(100,160,image=spy1)
  spy_btn=Button(window,text="PLAY",bg="#28F608",borderwidth=3,command=animePlay)
  spy_btn_window=canvas.create_window(100,250,window=spy_btn)
  window.mainloop()  
  
'''
sImage=Image.open('play.jpg')
re2=sImage.resize((150,150))
re2.save("play.png")
'''

startImage=PhotoImage(file='image2.png')
welcomeText=Label (window,text="Welcome to Anime Streaming application",
                 font=('Arial',23,'bold'),
                 fg="#335BFF",
                 bg='black',
                 relief=RAISED,
                 bd=15,
                 padx=15,
                 pady=10,
                 image=startImage,
                 compound='bottom'
                 )
welcomeText.pack()

button= Button(window,text='Click to Continue...',
              command=click,
              font=("Comic Sans",18),
              bg="#335BFF",
              #bg="#00FF00",
              fg="black",
              )                
button.pack()

#window.bind('<Configure>',resizer)
window.mainloop()

