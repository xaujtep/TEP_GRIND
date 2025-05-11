import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)
    label.config(text=count)

window = tk.Tk()
button = tk.Button(window, text="Click me")
button.config(command=click) #performs call back of function
button.config(font=("Arial", 15, "bold"))
button.config(bg="Black")
button.config(fg="White")
button.config(activebackground="Blue")
button.config(activeforeground="White")

# image = Image.open("C:/Users/ASUS/Downloads/download.png")
# # button.config(image= image) 
# photo = ImageTk.PhotoImage(image)
label = tk.Label(window, text=count)
label.config(font=("Monospace", 45, "bold"))
label.pack()

button.pack()
window.mainloop()