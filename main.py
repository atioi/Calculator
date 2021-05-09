import tkinter.font
from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

nr_btn_font = tkinter.font.Font(size=15)

result = 0


def btn_click(number):
    e.delete(0, END)
    e.insert(0, str(number))


def clear():
    e.delete(0, END)
    global result
    result = 0


def add():
    global result
    result += int(e.get())
    e.delete(0, END)
    e.insert(0, '+')


def show_result():
    global result
    result += int(e.get())
    e.delete(0, END)
    e.insert(0, str(result))
    result = 0


button_0 = Button(root, text="0", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, font=nr_btn_font, command=lambda: btn_click(9))

button_equal = Button(root, text="+", padx=95, pady=20, font=nr_btn_font, command=add)
button_sum = Button(root, text="=", padx=40, pady=20, font=nr_btn_font, command=show_result)
button_clear = Button(root, text="C", padx=95, pady=20, font=nr_btn_font, command=lambda: clear())

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=4, column=1, columnspan=2)
button_sum.grid(row=5, column=0)

root.mainloop()
