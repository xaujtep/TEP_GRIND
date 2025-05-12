import tkinter as tk

def submit():
    username = entry.get()
    print("Hello" + username)
window = tk.Tk()

def delete():
    entry.delete(0, tk.END )

def back_space():
    entry.delete(len(entry.get())-1, tk.END)

submit = tk.Button(window, text="Submit", command=submit)
submit.pack(side= "right")

delete = tk.Button(window, text="Delete", command=delete)
delete.pack(side= "right")

back_space = tk.Button(window, text="Backsapce", command=back_space)
back_space.pack(side= "right")

entry = tk.Entry()
entry.config(font=("Ink free", 45))
entry.config(bg="#47cc7f")
# # entry.insert(0, "TF")
# entry.config(state="disabled") ACTIVE OR DISABLE
entry.config(width=10)
# entry.config(show="*") PASSWORD   
entry.pack()
window.mainloop()