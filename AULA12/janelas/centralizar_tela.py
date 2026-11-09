import tkinter as tk


root=tk.Tk()
width=600
height=300


screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenwidth()
x=(screen_width/2) - (width/2)
y=(screen_height/2) - (height/2)


root.geometry(f"{width}x{height}+{x}+{y}")
root.mainloop()