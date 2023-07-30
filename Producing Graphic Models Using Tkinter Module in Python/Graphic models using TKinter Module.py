import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Graphic Models with Tkinter")

# Function to draw a rectangle on the canvas
def draw_rectangle():
    canvas.create_rectangle(50, 50, 200, 150, fill="blue")

# Function to draw an oval on the canvas
def draw_oval():
    canvas.create_oval(250, 50, 400, 150, fill="red")

# Function to draw a line on the canvas
def draw_line():
    canvas.create_line(50, 200, 400, 200, fill="green", width=3)

# Create Canvas widget
canvas = tk.Canvas(root, width=450, height=250, bg="white")
canvas.pack()

# Create buttons to draw shapes
rectangle_button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
rectangle_button.pack(side=tk.LEFT, padx=10)

oval_button = tk.Button(root, text="Draw Oval", command=draw_oval)
oval_button.pack(side=tk.LEFT, padx=10)

line_button = tk.Button(root, text="Draw Line", command=draw_line)
line_button.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event loop
root.mainloop()
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Graphic Models with Tkinter")

# Function to draw a rectangle on the canvas
def draw_rectangle():
    canvas.create_rectangle(50, 50, 200, 150, fill="blue")

# Function to draw an oval on the canvas
def draw_oval():
    canvas.create_oval(250, 50, 400, 150, fill="red")

# Function to draw a line on the canvas
def draw_line():
    canvas.create_line(50, 200, 400, 200, fill="green", width=3)

# Create Canvas widget
canvas = tk.Canvas(root, width=450, height=250, bg="white")
canvas.pack()

# Create buttons to draw shapes
rectangle_button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
rectangle_button.pack(side=tk.LEFT, padx=10)

oval_button = tk.Button(root, text="Draw Oval", command=draw_oval)
oval_button.pack(side=tk.LEFT, padx=10)

line_button = tk.Button(root, text="Draw Line", command=draw_line)
line_button.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event loop
root.mainloop()
