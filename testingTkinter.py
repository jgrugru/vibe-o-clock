from tkinter import *

root = Tk()

# topFrame = Frame(root)
# topFrame.pack()

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text="Button 1", fg="black")
# button2 = Button(topFrame, text="Button 2", fg="red")
# button3 = Button(topFrame, text="Button 3", fg="yellow")
# button4 = Button(bottomFrame, text="Button 4", fg="green")

# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)


# one = tkinter.Label(root, text="one", bg="red", fg="white")
# one.pack()
# two = tkinter.Label(root, text="two", bg="blue", fg="green")
# two.pack(fill=tkinter.X)
# three = tkinter.Label(root, text="three", bg="purple", fg="white")
# three.pack(side=tkinter.LEFT, fill=tkinter.Y)

label_1 = Label(root, text='Name')
label_2 = Label(root, text='Password')
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) #takes N, E, S, W options for sticky
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

checkbox = Checkbutton(root, text="Keep me logged in")
checkbox.grid(columnspan=2)


# part 6
# def printName(event):
#     print("Hello, I like cheese. <|)")
    
# button_1 = Button(root, text="Print text")#, command=printName)
# button_1.bind("<Button-1>", printName)
# button_1.pack()


# def left_click(event):
#     print("left click")

# def right_click(event):
#     print("right click")

# def middle_click(event):
#     print("middle click")

# frame = Frame(root, width=300, height=250)
# frame.bind("<Button-1>", left_click)
# frame.bind("<Button-2>", middle_click)
# frame.bind("<Button-3>", right_click)
# frame.pack()
root.mainloop()