import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Drawing Tool")

#Added a drawing canvas
canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack()

# Run the Tkinter event loop
root.mainloop()
