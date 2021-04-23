from _ast import Lambda
from tkinter import*

root=Tk()

#defining title of the project
root.title(" Mero Calculator ")

entry=Entry(root, width=60, borderwidth=6)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

#function
def button_click(number):
    current=entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number=entry.get()
    global f_num
    global math
    math="add"
    f_num=float(first_number)
    entry.delete(0,END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math="subtract"
    f_num = float(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiply"
    f_num=float(first_number)
    entry.delete(0,END)

def button_divide():
    first_number=entry.get()
    global f_num
    global math
    math="divide"
    f_num=float(first_number)
    entry.delete(0,END)

def button_mod():
    first_number=entry.get()
    global f_num
    global math
    math="mod"
    f_num=float(first_number)
    entry.delete(0,END)

def button_square():
    first_number=entry.get()
    global f_num
    global math
    math="square"
    f_num=float(first_number)
    entry.delete(0,END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)

    if math == "add":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtract":
        entry.insert(0,f_num - float(second_number))
    elif math == "multipliply":
        entry.insert(0,f_num  * float(second_number))
    elif math == "divide":
        entry.insert(0, f_num / float(second_number))
    elif math == "mod":
        entry.insert(0,f_num %  float(second_number))
    elif math =="square":
        entry.insert(0, f_num ** float(second_number))


#Defining the buttons (size,font,color)
button_1 = Button(root, text="1", padx=35, pady=15, command=lambda : button_click(1),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_2 = Button(root, text="2", padx=35, pady=15, command=lambda : button_click(2),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_3 = Button(root, text="3", padx=35, pady=15, command=lambda : button_click(3),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_4 = Button(root, text="4", padx=35, pady=15, command=lambda : button_click(4),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_5 = Button(root, text="5", padx=35, pady=15, command=lambda : button_click(5),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_6 = Button(root, text="6", padx=35, pady=15, command=lambda : button_click(6),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_7 = Button(root, text="7", padx=35, pady=15, command=lambda : button_click(7),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_8 = Button(root, text="8",padx=35, pady=15, command=lambda : button_click(8),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_9 = Button(root, text="9", padx=35, pady=15, command=lambda : button_click(9),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_0 = Button(root, text="0", padx=35, pady=15, command=lambda : button_click(0),fg="white", bg="#000000",font=('Helvetica',16,'bold'))
button_00 = Button(root, text="00", padx=30, pady=15, command=lambda: button_click("00"),fg="white",bg="#000000",font=('Helvetica',16,'bold'))
button_point = Button(root, text=".", padx=37, pady=15, command=lambda : button_click("."),fg="white",bg="#000000",font=('Helvetica',16,'bold'))
button_add = Button(root, text="+", padx=35, pady=15, command=button_add,fg="white", bg="#2270BD",font=('Helvetica',16,'bold'))
button_subtract = Button(root, text="-", padx=38, pady=15, command=button_subtract,fg="white", bg="#2270BD",font=('Helvetica',16,'bold'))
button_multiply = Button(root, text="×", padx=35, pady=15, command=button_multiply,fg="white", bg="#2270BD",font=('Helvetica',16,'bold'))
button_divide = Button(root, text="÷", padx=35, pady=15, command=button_divide,fg="white", bg="#2270BD",font=('Helvetica',16,'bold'))
button_clear = Button(root, text="C",padx=35, pady=15, command=button_clear,fg="white", bg="#EB8A28",font=('Helvetica',16,'bold'))
button_square  = Button(root, text="^", padx=36, pady=15, command=button_square,fg="white", bg="#2270BD",font=('Helvetica',16,'bold'))
button_mod  = Button(root, text="MOD", padx=19, pady=15, command=button_mod,fg="white", bg="#2270BD",font=('Helvetica',16,'bold'))
button_equal = Button(root, text="=", padx=35, pady=15, command=button_equal,fg="white", bg="#2270BD",font=('Helvetica',16,'bold'))

#Placing button on screen

button_0.grid(row=5, column=0)
button_00.grid(row=5,column=1)
button_point.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4,column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_square.grid(row=2, column=3)

button_mod.grid(row=1,column=3)
button_clear.grid(row=1, column=0)
button_divide.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)

root.mainloop()