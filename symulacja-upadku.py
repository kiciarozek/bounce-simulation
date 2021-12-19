import pygame
from math import sqrt
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 950])

# ball position
x = 250
y = 875
# starting height
h0 = y
# max height
hmax = h0
# when to stop bouncing
hstop = 0.1

# Is ball in air?
freefall = True

rho = 0.75
t = 1
tau = 0.1
t_last = 0
# speed of simulation
dt = 0.025
# gravitation {earth = 9.81}
g = 9.81
# velocity
v = 0

vmax = sqrt(2 * hmax * g)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if bouncing is taking too long end it
    if hmax > hstop:
        # is ball in air?
        if freefall:
            # set the new height based off some science stuff
            hnew = y + v * dt - 0.5 * g * dt * dt
            # is ball touching ground
            if y < 0:
                # do some calculations and set freefall as False
                t = t_last + 2 * sqrt(2 * hmax / g)
                freefall = False
                t_last = t + tau
                # make sure ball is on ground
                y = 0
            # if it is in air
            else:
                t = t + dt
                # make velocity higher based off gravitation and time
                v = v - g * dt
                y = hnew
        # if it is touching ground
        else:
            # do some science stuff, boooring
            t = t + tau
            vmax = vmax * rho
            v = vmax
            freefall = True
            y = 0
        # make sure ball won't reach too high
        hmax = 0.5 * vmax * vmax / g


    # Fill the background with white
    screen.fill((255, 255, 255))

    # draw a circle
    pygame.draw.circle(screen, (0, 0, 255), (x, 875 - y), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
