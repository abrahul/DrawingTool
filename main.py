import tkinter as tk
from tkinter.colorchooser import askcolor

# Create the main window
root = tk.Tk()
root.title("Simple Drawing Tool")

# Added a drawing canvas
canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack()

# Global color variable (default is black)
color = "black"

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill=color, width=5)  # <-- FIXED: Use the selected color
    last_x, last_y = event.x, event.y

def choose_color():
    global color
    chosen_color = askcolor(color=color)[1]
    if chosen_color:  # Ensure a color was selected
        color = chosen_color

# Button to choose color
tk.Button(root, text="Choose Color", command=choose_color).pack(side="left")

# Bind mouse events
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# Run the Tkinter event loop
root.mainloop()
