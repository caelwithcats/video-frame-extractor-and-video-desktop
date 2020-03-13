import tkinter as tk
from tkinter import filedialog
from tkinter import *
import cv2
import os
## PUBLIC VARIBLES
folder = "./Pictures/frames"

class Application(tk.Frame):
   def __init__(self,master=None):

       super().__init__(master)
       self.master = master
       self.pack()
       self.create_widgets()
       print("Current working directory is %s" % os.getcwd())

   def create_widgets(self):

       self.info_text = tk.Label(self)
       self.info_text["text"] = "Choose a .mp4 .avi .ogg or .flv file to set as your video background"
       self.info_text.pack(side="top")

       self.close_btn = tk.Button(self, text="Close", command=self.master.destroy)
       self.close_btn.pack(side="bottom")

       self.browse_btn = tk.Button(self, text="Browse...", command=self.browse_click)
       self.browse_btn.pack(side="bottom")

   def browse_click(self):

       print("Browse button clicked")
       self.filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Select a video",filetypes = (("mp4 file","*.mp4"),("all files","*.*")))
       print(self.filename)



       # print(folder)
       try:
          if not os.path.exists(os.path.dirname(folder)):
             os.mkdir(folder)

       except OSError as err:
          print(err)

       self.createFrames()

# -------------------------------------------------------------------------------------------------------------
   async def createFrames(self):

       video_capture = cv2.VideoCapture(self.filename)
       success,bitmap = video_capture.read();
       count = 0

       while success:
            print("-------------------------Video frame extractor------------------------------")
            path = "./Pictures/frames/videoframe-%d.png" % count
            cv2.imwrite(path,bitmap)
            success,bitmap = video_capture.read()
            print('Frame: %d:' % count,success)
            count += 1
       if not success:
           print("Not enough memory to complete the task. Or the video could be invalid")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
