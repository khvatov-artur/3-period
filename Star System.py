import tkinter as tk
import math


# --- functions ---

def calculate_position(data):
    # unpack data
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
    return c.create_oval(x1, y1, x2, y2)


def move_object(object_id, data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    # move oval
    c.coords(object_id, x1, y1, x2, y2)


def animate():
    # move earth - angle += angle_speed
    mercury[4] += mercury[5]
    move_object(mrc_id, mercury)

    venus[4] += venus[5]
    move_object(ven_id, venus)

    earth[4] += earth[5]
    move_object(e_id, earth)

    # moon uses earth position as center of rotation
    moon[0] = earth[6]
    moon[1] = earth[7]

    # move move - angle += angle_speed
    moon[4] += moon[5]
    move_object(m_id, moon)

    mars[4] += mars[5]
    move_object(mrs_id, mars)

    jupyter[4] += jupyter[5]
    move_object(jup_id, jupyter)

    saturn[4] += saturn[5]
    move_object(sat_id, saturn)

    uran[4] += uran[5]
    move_object(urn_id, uran)

    neptune[4] += neptune[5]
    move_object(npt_id, neptune)

    # animate again after 100ms
    root.after(100, animate)


# --- main ---

# canvas size
WIDTH = 750
HEIGHT = 750

# center of solar system
center_x = WIDTH // 2
center_y = HEIGHT // 2

# objects data
# [center of rotation x and y, radius, distance from center, current angle, angle speed, current positon x and y]
sun = [center_x, center_y, 67, 0, 0, 0, 0, 0]
mercury = [center_x, center_y, 5, 100, 0, 21, 0, 0]
venus = [center_x, center_y, 12, 140, 0, 1, 14, 0]
earth = [center_x, center_y, 13, 180, 0, 8.6, 0, 0]
moon = [center_x, center_y, 3.4, 16, 0, 8.6, 0, 0]
mars = [center_x, center_y, 6.8, 220, 0, 5, 0, 0]
jupyter = [center_x, center_y, 20, 280, 0, 2, 0, 0]
saturn = [center_x, center_y, 18, 350, 0, 0.8, 0, 0]
uran = [center_x, center_y, 16, 410, 0, 0 / .4, 0, 0]
neptune = [center_x, center_y, 16, 450, 0, 0.1, 0, 0]

# - init -
root = tk.Tk()
root.title("Solar System")

# - canvas -
c = tk.Canvas(root, width=WIDTH, heigh=HEIGHT, bg="lightgrey")
c.pack()

# create sun and earth
s_id = create_object(sun)
e_id = create_object(earth)
m_id = create_object(moon)
mrc_id = create_object(mercury)
ven_id = create_object(venus)
mrs_id = create_object(mars)
jup_id = create_object(jupyter)
sat_id = create_object(saturn)
urn_id = create_object(uran)
npt_id = create_object(neptune)

# start animation
animate()

# - start program -
root.mainloop()
