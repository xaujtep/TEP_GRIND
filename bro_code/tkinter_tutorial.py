from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("420x420")
window.title("First GUI")
window.config(background="black")

image = Image.open('"C:\Users\ASUS\Pictures\Camera Roll\pic.jpg"')
icon = ImageTk.PhotoImage(image)


window.mainloop()