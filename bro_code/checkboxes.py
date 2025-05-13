# import tkinter as tk
# from PIL import Image, ImageTk

# def display():
#     if x.get() == 1:
#        print("Copy that!")
#     else:
#         print("Thanks")

# window = tk.Tk()

# x = tk.IntVar()
# y = tk.IntVar()

# checkbox = tk.Checkbutton(window, text="Python", variable=x, onvalue=1, offvalue=0,command=display)
# checkbox.pack()
# checkbox.config(font=("Arial", 20)) #changes font
# checkbox.config(bg="Pink")
# checkbox.config(fg="Brown")
# checkbox.config(activeforeground="Brown")
# checkbox.config(activebackground="Pink")
# checkbox.config(padx=25,pady=10,width=250,height=50)
# checkbox.config(anchor='w') #anchors widget to relative cardinal direction


# # image = Image.open("C:/Users/ASUS/Downloads/Python-logo-notext.svg.png")
# # photo = ImageTk.PhotoImage(image)
# # checkbox.config(image=photo)

# checkbox2 = tk.Checkbutton(window, text="Java", variable=y, onvalue=1, offvalue=0,command=display)
# checkbox2.pack()
# checkbox2.config(font=("Arial", 20)) #changes font
# checkbox2.config(bg="Pink")
# checkbox2.config(fg="Brown")
# checkbox2.config(activeforeground="Brown")
# checkbox2.config(activebackground="Pink")
# checkbox2.config(padx=25,pady=10,width=250,height=50)
# checkbox2.config(anchor='w')
#  #anchors widget to relative cardinal direction

# window.mainloop()

from tkinter import *
import tkinter as tk

def display():
    if(x.get()==1)&(y.get()==0):
        print("I like Python")
    elif(x.get()==0)&(y.get()==1):
        print("I like Java")
    elif(x.get()==1)&(y.get()==1):
        print("I like both Python & Java")
    else:
        print("I don't like either")

window = tk.Tk()

x = IntVar()
y = IntVar()

checkbox = tk.Checkbutton(window,text='Python',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()
checkbox.config(font=('Arial',20)) #changes the font
checkbox.config(fg='#00FF00') #foreground color
checkbox.config(bg='#000000') #background color
checkbox.config(activeforeground='#0000FF') #active foreground color
checkbox.config(activebackground='#000000') #active background color
# photo = PhotoImage(file='python_logo.png')
# checkbox.config(image=photo,compound='left') #sets image to photoimage
checkbox.config(padx=25,pady=10,width=250,height=50)
checkbox.config(anchor='w') #anchors widget to relative cardinal direction

checkbox2 = tk.Checkbutton(window,text='Java',variable=y,onvalue=1,offvalue=0,command=display)
#checkbox2.pack()
checkbox2.config(font=('Arial',20)) #changes the font
checkbox2.config(fg='#0000FF') #foreground color
checkbox2.config(bg='#000000') #background color
checkbox2.config(activeforeground='#0000FF') #active foreground color
checkbox2.config(activebackground='#000000') #active background color
# photo2 = PhotoImage(file='Java_logo.png')
# checkbox2.config(image=photo2,compound='left') #sets image to photoimage
checkbox2.config(padx=25,pady=10,width=250,height=50)
checkbox2.config(anchor='w')
 #anchors widget to relative cardinal direction
window.mainloop()