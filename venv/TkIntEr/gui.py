from tkinter import *
root=Tk()

myLabel1=Label(root, text='This is the begining')
myLabel2=Label(root,text="THis is middle")
myLabel3=Label(root,text="this is the end")

myLabel1.grid(row=0, column=1)
myLabel2.grid(row=0, column=2)
myLabel3.grid(row=1, column=2)

root.mainloop()