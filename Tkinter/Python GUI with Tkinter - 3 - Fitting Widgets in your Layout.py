from tkinter import *


root = Tk()
one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="two", bg="red", fg="white")
two.pack(fill=X)
three = Label(root, text="three", bg="green", fg="white")
three.pack(side=LEFT, fill=Y)



root.mainloop()