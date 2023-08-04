import pickle
from tkinter import *
from tkinter import filedialog

def todo_list():
    root = Tk()
    root.title("Todo App")
    root.geometry("330x400")
    root.resizable(False, False)
    root.config(bg="#1B202A")

    my_frame = Frame(root)
    my_frame.pack(pady=10)

    my_list = Listbox(
        my_frame,
        font=16,
        width=23,
        height=7,
        bg="#1B202A",

        highlightthickness=0,
        fg="#fff",
        activestyle="none"

    )
    my_list.pack(side=LEFT, fill=BOTH)

    stuff = ["Play the field", "Make a program", "write a code", "Buy a laptop"]
    for item in stuff:
        my_list.insert(END, item)

    my_scroll = Scrollbar(my_frame, bg="#1B202A")
    my_scroll.pack(side=RIGHT, fill=BOTH)
    my_list.config(yscrollcommand=my_scroll.set)
    my_scroll.config(command=my_list.yview)

    e1 = Entry(root, width=30, borderwidth=3, font=("arial", 12))
    e1.pack(pady=30)

    def delete_task():
        my_list.delete(ANCHOR)

    def add_task():
        my_list.insert(END, e1.get())
        e1.delete(0, END)

    def cross_task():
        my_list.itemconfig(
            my_list.curselection(),

            fg="#30394A")
        my_list.select_clear(0, END)

    def uncross_task():
        my_list.itemconfig(
            my_list.curselection(),

            fg="")
        my_list.select_clear(0, END)


    delete_button = Button(root, text="Delete items", bg="#2F323C", fg="#fff", width="13", pady="5",
                           font=("arial", 11), command=delete_task)
    delete_button.place(x=28, y=270)

    add_button = Button(root, text="Add items", bg="#2F323C", fg="#fff", width="13", pady="5",
                        font=("arial", 11), command=add_task)
    add_button.place(x=177, y=270)

    cross = Button(root, text="Cross of items", bg="#2F323C", fg="#fff", width="13", pady="5",
                   font=("arial", 11), command=cross_task)
    cross.place(x=28, y=320)

    uncross = Button(root, text="Uncross of items", bg="#2F323C", fg="#fff", width="13", pady="5",
                     font=("arial", 11), command=uncross_task)
    uncross.place(x=177, y=320)

    def save_list():
        file_name = filedialog.asksaveasfilename(
            title="save file",
            filetypes=(("dat files",".dat"),("all files","*.*"))
        )
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'
        stuff = my_list.get(0,END)
        output = open(file_name,'wb')
        pickle.dump(stuff,output)
    def open_list():
        file_name = filedialog.askopenfilename(
            title="open file",
            filetypes=(("dat files", ".dat"), ("all files", "*.*"))
        )
        if file_name:
            my_list.delete(0,END)
            input_file = open(file_name,'rb')
            stuff = pickle.load(input_file)

            for item in stuff:
                my_list.insert(END,item)

    def clear_list():
        my_list.delete(0, END)

    def exit():
        root.destroy()

    # create menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # add menu items
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="open list", command=open_list)
    file_menu.add_command(label="Save list", command=save_list)
    file_menu.add_separator()
    file_menu.add_command(label="clear list", command=clear_list)
    file_menu.add_command(label="exit", command=exit)

    root.mainloop()
#todo_list()

