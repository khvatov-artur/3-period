import tkinter as tk
import math

# --- functions ---

def calculate_position(data):
    #unpack data
    center_x, center_y, radius, distance, angle, angle_speed, x, y = data

    # calculate new position of object
    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))

    # save positon so other object can use it as its center of rotation
    data[6] = x
    data[7] = y

    # calcuate oval coordinates
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2

def create_object(data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    # create oval
    return c.create_oval(x1, y1, x2, y2, outline='black',
    fill='white', width=10)

def move_object(object_id, data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    # move oval
    c.coords(object_id, x1, y1, x2, y2)

def animate():
    # move earth - angle += angle_speed
    circle2[4] += circle2[5]
    move_object(object2, circle2)

    circle3[4] += circle3[5]
    move_object(object3, circle3)
    # animate again after 100ms
    root.after(100, animate)

# --- main ---

# canvas size
WIDTH  = 600
HEIGHT = 600

# center of solar system
center_x = WIDTH//2
center_y = HEIGHT//2

# objects data
# [center of rotation x and y, radius, distance from center, current angle, angle speed, current positon x and y]
circle1   = [center_x, center_y, 200, 0, 0, 0, 0, 0]
circle2 = [center_x, center_y, 50, 250, 0, 10, 0, 0]
circle3 = [center_x, center_y, 50, 250, 0, -10, 0, 0]

# - init -
root = tk.Tk()
root.title("Laba 1")

# - canvas -
c = tk.Canvas(root, width=WIDTH, heigh=HEIGHT)
c.pack()

# create sun and earth
object1 = create_object(circle1)
object2 = create_object(circle2)
object3 = create_object(circle3)
# start animation
animate()

# - start program -
root.mainloop()