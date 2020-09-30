import pygame
import random

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# устанавливает ширину и высоту окна
SIZE = width, height = [300, 700]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Тип Дождь")

speed = 10
# Плотность
val = 100
# Создает пустой список
rain_list = []

# Частота появление (в range()) в рандомных координатах
for i in range(val):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    rain_list.append([x, y])

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BLACK)

    # Process each snow flake in the list
    for i in range(len(rain_list)):

        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, rain_list[i], random.randrange(1, 5))

        # Move the snow flake down one pixel
        rain_list[i][1] += speed

        # If the snow flake has moved off the bottom of the screen
        if rain_list[i][1] > height:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            rain_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, width)
            rain_list[i][0] = x

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()