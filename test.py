from tkinter import *
from scipy import *
from PIL import *

import customtkinter as tk
tk.set_appearance_mode('dark')
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
btn = tk.CTkButton(master="",text="click me").pack()
root.geometry("300x400")
root.mainloop()