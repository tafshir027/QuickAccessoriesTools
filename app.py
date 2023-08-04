import tkinter
from tkinter import *

import pytz

from TodoList import *
from Calculator_App import calculator
from notePad_App import notepad
from TodoList import todo_list
from weather_app import *
from weather_app import *
import os
import time
import wave
import threading
import pyaudio
import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv
from PIL import Image, ImageTk
from tkinter import colorchooser
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import PIL.ImageGrab as ImageGrab


window = Tk()
window.title("Quick accessories Tools")
window.geometry('1280x720+20+10')
window.resizable(False, False)
window.config(bg="#1B202A")


# Title Label

AppTitle = Label(window, text=" 'Quick accessories Tools' ", font=("arial", 20), padx=1280, pady=15, fg='#fff',
                 bg="#242e41")
AppTitle.pack()


# Digital Clock
def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)


clock = Label(window, font=("Arial", 23), background="#1B202A", foreground="white")
clock.place(x=30, y=650)
get_time()


# Paint window
def paint():
    top = Toplevel()
    top.state("zoomed")
    top.title('Paint Application')
    top.config(bg='#f0f0f0')
    top.minsize(1350, 650)

    global  pen_color


    pen_color = "red"
    eraser_color = "white"


    def canvasColor():
        global eraser_color

        color = colorchooser.askcolor()
        canvas.configure(bg=color[1])
        eraser_color = color[1]

    def save():
        file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
        x = top.winfo_rootx() + canvas.winfo_x()
        y = top.winfo_rooty() + canvas.winfo_y()

        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()

        ImageGrab.grab().crop((x, y, x1, y1)).save(file_name)
        messagebox.showinfo("paint Notification", "Image is Saved " + str(file_name))

    def erase():
        global pen_color
        pen_color = eraser_color

    def clear():
        canvas.delete("all")

    def paint(event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)

        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color, width=pen_size.get())

    # Canvas
    canvas = Canvas(top, bg="white", bd=5, relief=GROOVE, height=700, width=1480)
    canvas.place(x=10, y=100)

    canvas.bind("<B1-Motion>", paint)

    def select_color(col):
        global pen_color
        pen_color = col

    # Frame
    color_frame = LabelFrame(top, text="color", relief=RIDGE, bg="#fff", width=490, height=80,
                             font=("arial", 15, "bold"))
    color_frame.place(x=10, y=10)

    tools_frame = LabelFrame(top, text="Tools", relief=RIDGE, bg="#fff", width=320, height=80,
                             font=("arial", 15, "bold"))
    tools_frame.place(x=450, y=10)

    pen_frame = LabelFrame(top, text="Pen Size", relief=RIDGE, bg="#fff", width=294, height=60,
                           font=("arial", 15, "bold"))
    pen_frame.place(x=730, y=10)

    # Color
    colors = ['#FF0000', '#008000', '#FFC0CB', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#A52A2A', '#FFFFFF',
              '#000000', '#808080', '#87CEEB']

    # Button
    i = j = 0
    for color in colors:
        Button(color_frame, bd=3, bg=color, relief=RIDGE, width=3, command= lambda col=color: select_color(col)).grid(
            row=j, column=i, padx=1)
        i = i + 1

    # tools button
    canvas_color_b1 = Button(tools_frame, command=canvasColor, text="Canvas", bg="#2F323C", fg="#fff",
                             font=("arial", 12))
    canvas_color_b1.grid(row=0, column=0, padx=3)

    save_b1 = Button(tools_frame, command=save, text="Save", bg="#2F323C", fg="#fff", font=("arial", 12))
    save_b1.grid(row=0, column=1, padx=3)

    erase_b1 = Button(tools_frame , text="Erase", bg="#2F323C", fg="#fff", font=("arial", 12), command=erase)
    erase_b1.grid(row=0, column=2, padx=3)

    clear_b1 = Button(tools_frame, command=clear, text="Clear", bg="#2F323C", fg="#fff", font=("arial", 12))
    clear_b1.grid(row=0, column=3, padx=3)

    # Pen and eraser size
    pen_size = Scale(pen_frame, orient=HORIZONTAL, from_=0, to=50, length=170)
    pen_size.set(1)
    pen_size.grid(row=0, column=0)

    top.mainloop()


# Recorder window
def record():
    top = Toplevel()
    top.geometry("400x500+20+0")
    top.title('Recorder')
    top.config(bg='#1B202A')
    title = Label(top, text="Sound Recorder", fg="#fff", bg="#242e41", font=("Arial", 15), pady=10, padx=400).pack()

    def recordStart():
        freq = 44100
        dur = int(duration.get())
        recording = sound.rec(dur * freq,
                              samplerate=freq,
                              channels=2)

        try:
            temp = int(duration.get())
        except:
            print("please enter the right value")

        while temp > 0:
            top.update()
            time.sleep(1)
            temp -= 1

            if (temp == 0):
                messagebox.showinfo("Time countdown", "Time's up")

            Label(top, text=f"{str(temp)}", font=("arial", 20), fg="#fff", bg="#1B202A").place(x=160, y=390)
        sound.wait()
        write("recording.wav", freq, recording)

    global xv, start, stop
    xv = PhotoImage(file="resources/img/recorder.png")
    iconL = Button(top, image=xv, bg="#242e41", fg="#242e41", borderwidth=0).pack(pady=20)
    duration = StringVar()
    entry_time = Entry(top, textvariable=duration, font=("arial", 15))
    entry_time.pack(pady=20)
    start = PhotoImage(file="resources/img/plays.png")
    starts = Button(top, image=start, border=0, borderwidth=0, bg="#242e41", command=recordStart).place(x=160, y=290)


# weather APP
global sr


def weather():
    top = Toplevel()
    top.title("Weather App")
    top.config(bg="#1B202A")
    top.geometry("900x500+300+200")
    top.resizable(False, False)

    def getWeather():
        city = e1.get()

        geolocator = Nominatim(user_agent="geoapiExercise")
        location = geolocator.geocode(city)

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        global cur_time, name1, clock1
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        cur_time = local_time.strftime("%I:%M %p")
        CL.config(text=cur_time)
        N.config(text="Current Weather")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=31180e2323f84f887d21c5a305cac2cc"
        jeson_data = requests.get(api).json()
        condition = jeson_data['weather'][0]['main']
        description = jeson_data['weather'][0]['description']
        temp = int(jeson_data['main']['temp'] - 273.15)
        pressure = jeson_data['main']['pressure']
        humidity = jeson_data['main']['humidity']
        wind = jeson_data['wind']['speed']

        T1.config(text=(temp, "°"))
        lf.config(text=(condition, "|", "Feels", "Like", temp, "°"))
        w.config(text=wind)
        p.config(text=pressure)
        h.config(text=humidity)
        d.config(text=description)

    srcBox = PhotoImage(file="resources/img/src.png")
    # time
    N = Label(top, text="Current Weather", font=("arial", 15, "bold"), bg="#1B202A", fg="#fff")
    N.place(x=100, y=90)
    CL = Label(top, text="00:00 AM", font=("Helvetica", 15, "bold"), bg="#1B202A", fg="#fff")
    CL.place(x=100, y=120)

    T1 = Label(top, text="0 °", font=("arial", 30, "bold"), bg="#1B202A", fg="orange")
    T1.place(x=580, y=80)
    lf = Label(top, text="Normal | Feels Like 0 °", font=("arial", 20, "bold"), bg="#1B202A", fg="#fff")
    lf.place(x=550, y=140)

    im = Label(top, image=srcBox, border=0)
    im.place(x=100, y=20)
    e1 = Entry(top, font=("arial", 11), background="#f3f3f3", foreground="#000", width=18, borderwidth=0)
    e1.place(x=110, y=28)

    srcIcon = PhotoImage(file="resources/img/srcb.png")
    srcButton = Button(top, image=srcIcon, borderwidth="0", border="0", command=getWeather).place(x=255, y=26)

    weatherLogo = PhotoImage(file="resources/img/weather1.png")
    Label(top, image=weatherLogo, border="0", borderwidth=0).place(x=300, y=150)

    Bar = PhotoImage(file="resources/img/bar.png")
    Label(top, image=Bar, border="1", borderwidth=0).place(x=45, y=360)

    lb1 = Label(top, text="Wind", bg="#27adc8", fg="#fff", font=("arial", 20, "bold")).place(x=100, y=375)
    lb2 = Label(top, text="Humidity", bg="#27adc8", fg="#fff", font=("arial", 20, "bold")).place(x=240, y=375)
    lb3 = Label(top, text="Despription", bg="#27adc8", fg="#fff", font=("arial", 20, "bold")).place(x=420, y=375)
    lb4 = Label(top, text="Pressure", bg="#27adc8", fg="#fff", font=("arial", 20, "bold")).place(x=630, y=375)

    w = Label(top, text="00", bg="#27adc8", fg="#000", font=("arial", 10, "bold"))
    w.place(x=120, y=415)
    h = Label(top, text="00", bg="#27adc8", fg="#000", font=("arial", 10, "bold"))
    h.place(x=250, y=415)
    d = Label(top, text="00", bg="#27adc8", fg="#000", font=("arial", 10, "bold"))
    d.place(x=430, y=415)
    p = Label(top, text="00", bg="#27adc8", fg="#000", font=("arial", 10, "bold"))
    p.place(x=650, y=415)

    window.mainloop()


# option
cal = Button(window, text='Calculator', bg="#2F323C", width='15', height='2', fg="#fff", font=("arial", 13),
             command=calculator)
TextEditor = Button(window, text='Text Editor', width='15', height='2', bg="#2F323C", fg="#fff", font=("arial", 13),
                    command=notepad)
ToDo = Button(window, text='To-do-list', width='15', height='2', bg="#2F323C", fg="#fff", font=("arial", 13),
              command=todo_list)

paint = Button(window, text='Paint', bg="#2F323C", width='15', height='2', fg="#fff", font=("arial", 13), command=paint)
weather = Button(window, text='Weather', bg="#2F323C", width='15', height='2', fg="#fff", font=("arial", 13),
                 command=weather)
Recorder = Button(window, text='Recorder', bg="#2F323C", width='15', height='2', fg="#fff", font=("arial", 13),
                  command=record)

cal.place(x=562, y=340)
TextEditor.place(x=770, y=340)
ToDo.place(x=970, y=340)

paint.place(x=560, y=577)
weather.place(x=770, y=577)
Recorder.place(x=970, y=577)

cal = PhotoImage(file="resources/img/calc.png")
cal_lebel = Label(image=cal, border="0")
cal_lebel.place(x=570, y=190)

note = PhotoImage(file="resources/img/note.png")
note_lebel = Label(image=note, border="0")
note_lebel.place(x=780, y=190)

todo = PhotoImage(file="resources/img/todo.png")
todo_lebel = Label(image=todo, border="0")
todo_lebel.place(x=975, y=190)

paint = PhotoImage(file="resources/img/paint.png")
paint_lebel = Label(image=paint, border="0")
paint_lebel.place(x=570, y=417)

weather = PhotoImage(file="resources/img/weather.png")
weather_lebel = Label(image=weather, border="0")
weather_lebel.place(x=780, y=417)

record = PhotoImage(file="resources/img/recorder.png")
record_lebel = Label(image=record, border="0")
record_lebel.place(x=975, y=417)

backGround = PhotoImage(file="resources/img/bk.png")
bk = Label(image=backGround, border=0)
bk.place(x=140, y=150)

backGround1 = PhotoImage(file="resources/img/bk1.png")
bk1 = Label(image=backGround1, border=0)
bk1.place(x=140, y=400)

window.mainloop()
