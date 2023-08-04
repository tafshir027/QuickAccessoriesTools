from tkinter import *


def calculator():
    root = Tk()
    root.title("Calculator")
    root.geometry("325x450")
    root.config(bg="#1B202A")
    e1 = Entry(root, width="25",text="0", bg="#1B202A", fg="#fff", borderwidth="10", font="20",highlightcolor="#2F323C",highlightthickness="3")

    e1.grid(padx=10, pady=20)

    #function
    def button_work(number):
        current = e1.get()
        e1.delete(0,END)
        e1.insert(0,str(current)+str(number))

    def clear():
        e1.delete(0,END)
    def exit():
        root.destroy()
    def addition():
        first_number = e1.get()
        global f_number
        global math
        math = "Addition"
        f_number = int(first_number)
        e1.delete(0,END)

    def subtraction():
        first_number = e1.get()
        global f_number
        global math
        math = "subtraction"
        f_number = int(first_number)
        e1.delete(0,END)

    def multiplication():
        first_number = e1.get()
        global f_number
        global math
        math = "multiplication"
        f_number = int(first_number)
        e1.delete(0,END)

    def division():
        first_number = e1.get()
        global f_number
        global math
        math = "division"
        f_number = int(first_number)
        e1.delete(0,END)

    def module():
        first_number = e1.get()
        global f_number
        global math
        math = "module"
        f_number = int(first_number)
        e1.delete(0,END)

    def buttonEqual():
        secondNumber = e1.get()
        e1.delete(0,END)

        if math =="Addition":
            e1.insert(0,f_number + int(secondNumber))
        if math =="subtraction":
            e1.insert(0,f_number - int(secondNumber))
        if math =="multiplication":
            e1.insert(0,f_number * int(secondNumber))
        if math =="division":
            e1.insert(0,f_number / int(secondNumber))

        if math =="module":
            e1.insert(0,f_number % int(secondNumber))
    # Button Group
    seven = Button(root, text=7, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(7))
    seven.place(x="10",y="100")

    eight = Button(root, text=8, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(8))
    eight.place(x="90",y="100")

    nine = Button(root, text=9, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(9))
    nine.place(x="170",y="100")

    mul = Button(root, text="*", bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=multiplication)
    mul.place(x="250",y="100")

    four = Button(root, text=4, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(4))
    four.place(x="10",y="160")

    five = Button(root, text=5, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(5))
    five.place(x="90",y="160")

    six = Button(root, text=6, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(6))
    six.place(x="170",y="160")

    sub = Button(root, text="-", bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=subtraction)
    sub.place(x="250",y="160")

    one = Button(root, text=1, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(1))
    one.place(x="10",y="220")

    two = Button(root, text=2, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(2))
    two.place(x="90",y="220")

    three = Button(root, text=3, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(3))
    three.place(x="170",y="220")

    div = Button(root, text="/", bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=division)
    div.place(x="250",y="220")

    ac = Button(root, text="AC", bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=clear)
    ac.place(x="10",y="280")

    zero = Button(root, text=0, bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=lambda: button_work(0))
    zero.place(x="90",y="280")

    mod = Button(root, text="%", bg="#2F323C",fg="#fff", width="5", pady="5", font="15", command=module)
    mod.place(x="170",y="280")

    plus = Button(root, text="+", bg="#2F323C", fg="#fff", width="5", pady="5", font="15", command=addition)
    plus.place(x="250",y="280")


    equal = Button(root, text="=", bg="#C7B4E7",fg="#000", width="12", pady="5", font="15", command=buttonEqual)
    equal.place(x="10",y="340")

    exi = Button(root, text="Exit", bg="orange",fg="#000", width="12", pady="5", font="15", command=exit)
    exi.place(x="173",y="340")
    root.mainloop()


#calculator()