from tkinter import *
from datetime import datetime

class VibeOClock(Frame):
    def __init__(self, Master=None):
        super().__init__(Master)
        self.master = Master
        self.timeLabel = Label(self, text="", bg="black", fg="white", font=("Courier", 44))
        self.timeLabel.pack(side=BOTTOM)
        self.alarmButton = Button(self, text="Vibe Alarm", fg="green", command=self.set_vibe_time)
        self.alarmButton.pack(side=TOP)
        self.pack()
        self.update_time_label()

    def update_time_label(self):
        currentTime = datetime.now().strftime("%H:%M:%S")
        self.timeLabel.configure(text=currentTime)
        self.master.after(1000, self.update_time_label)

    def set_vibe_time(self):
        print("testing vibe time")
        self.alarmButton.configure(text=datetime.now().strftime("%H:%M"))

root = Tk()
myVibeOClock = VibeOClock(Master=root)
myVibeOClock.mainloop()

# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()