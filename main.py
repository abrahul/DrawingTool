import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Drawing Tool")

#Added a drawing canvas
canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack()

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill="black", width=5)
    last_x, last_y = event.x, event.y

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# Run the Tkinter event loop
root.mainloop()
