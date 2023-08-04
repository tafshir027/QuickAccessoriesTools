from tkinter import *
from tkinter import filedialog
from tkinter import font


def notepad():
    global open_status
    global selected
    selected = False
    open_status = False
    root = Tk()
    root.title("NotePad ")
    root.geometry("1000x600")

    # create  Main Frame
    my_frame = Frame(root)
    my_frame.pack(pady=5)

    # create srollbar
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    # create textBox
    my_text = Text(my_frame, width=97, height=25, font=("arial", 18), selectbackground="blue", selectforeground="#fff",
                   undo=True, yscrollcommand=text_scroll.set)
    my_text.pack()
    text_scroll.config(command=my_text.yview)

    # new file Function
    def new_file():
        my_text.delete(1.0, END)
        root.title('New File - Textpad!')
        status_bar.config(text="New File       ")

    def open_file():
        my_text.delete(1.0, END)
        text_file = filedialog.askopenfilename(initialdir="", title="open File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All files", "*.*")))

        name = text_file
        name.replace("c:/Users/", "")
        root.title(f"{name} - TextPad!")
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

    def save_as():
        text_file = filedialog.asksaveasfilename(defaultextension=".*", title="save file", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All files", "*.*")))
        if text_file:
            name = text_file
            root.title(f"{name} - TextPad!")
            text_file = open(text_file, 'w')
            text_file.write(my_text.get(1.0, END))
            text_file.close()

    # Edit Menu
    def cut_text(e):

        global selected
        if e:
            selected = root.clipboard_get()
        else:
            if my_text.selection_get():
                selected = my_text.selection_get()
                my_text.delete("sel.first", "sel.last ")
                root.clipboard_clear()
                root.clipboard_append(selected)

    def copy_text(e):
        global selected
        if e:
            selected = root.clipboard_get()
        if my_text.selection_get():
            selected = my_text.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)

    def paste_text(e):
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

    def exit():
        root.destroy()

    # create Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Add File Menu
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="file", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="open", command=open_file)
    file_menu.add_command(label="Save As", command=save_as)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit)

    # edit Menu
    edit_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut    (Ctrl+X)", command=lambda: cut_text(False))
    edit_menu.add_command(label="Copy   (Ctrl+C)", command=lambda: copy_text(False))
    edit_menu.add_command(label="paste  (Ctrl+V)", command=lambda: paste_text(False))
    file_menu.add_separator()
    edit_menu.add_command(label="Undo  (Ctrl+Z)", command=my_text.edit_undo, accelerator="(ctrl+Z)")
    edit_menu.add_command(label="Redo  (Ctrl+Y)", command=my_text.edit_redo, accelerator="(ctrl+y)")

    # About Menu
    about_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=about_menu)
    about_menu.add_command(label="Contact Us")

    # Add status Bar
    status_bar = Label(root, text="Ready  ", anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=5)

    # Edit Binding

    root.bind('control-key-x', cut_text)
    root.bind('control-key-c', copy_text)
    root.bind('control-key-v', paste_text)

    root.mainloop()

#notepad()

