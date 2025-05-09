import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
image = Image.open("C:/Users/ASUS/Downloads/download.png")
photo = ImageTk.PhotoImage(image)

# label = tk.Label(window, text="Hello World", font=("Arial",30,"bold"), fg="pink", bg="Black", relief=SUNKEN, bd=10, padx= 20, pady= 20) 
# #RAISED OR SUNKEN
label = tk.Label(window, image=photo)
label.pack()

window.mainloop()

  