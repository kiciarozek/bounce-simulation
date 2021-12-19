import pygame
from math import sqrt
pygame.init()

screen = pygame.display.set_mode([1000, 950])

display_surface = pygame.display.set_mode((1000,950))

x = 250
y = 875

h0 = y
hmax = h0
hstop = 0.1

freefall = True

rho = 0.75
t = 1
tau = 0.1
t_last = 0
dt = 0.05
g = 9.81
v = 0

vmax = sqrt(2 * hmax * g)

try:
    font = pygame.font.Font('RobotoMono-Regular.ttf', 32)
except:
    font = pygame.font.Font(None,40)

ziemia = font.render('Earth', True,(0,0,0),(0,150,0) )
ziemiaRect = ziemia.get_rect()
ziemiaRect.center = (1000-100,30)

mars = font.render('Mars', True,(200,200,200),(0,0,0) )
marsRect = mars.get_rect()
marsRect.center = (1000-100,90)

ksiezyc = font.render('Moon', True,(200,200,200),(0,0,0) )
ksiezycRect = ksiezyc.get_rect()
ksiezycRect.center = (1000-100,150)

inputtext = "1"

text = font.render("Speed:", True,(200,200,200),(0,0,0) )
textRect = text.get_rect()
textRect.center = (1000-100,210)

inputbox = font.render(inputtext, True,(200,200,200),(0,0,0) )
inputboxRect = inputbox.get_rect()
inputboxRect.center = (1000-100,270)

inputactive = False

running = True
while running:

    # if bouncing is taking too long end it
    if hmax > hstop:
        # is ball in air?
        if freefall:
            # set the new height based off some science stuff
            hnew = y + v * dt - 0.5 * g * dt * dt
            # is ball touching ground, if not stop it
            if y < 0:
                t = t_last + 2 * sqrt(2 * hmax / g)
                freefall = False
                t_last = t + tau
                y = 0
            # if it is in air
            else:
                t = t + dt
                v = v - g * dt
                y = hnew
        # if it is touching ground
        else:
            t = t + tau
            vmax = vmax * rho
            v = vmax
            freefall = True
            y = 0
        hmax = 0.5 * vmax * vmax / g


    screen.fill((255, 255, 255))

    circle = pygame.draw.circle(screen, (0, 0, 255), (x, 875 - y), 75)

    display_surface.blit(ziemia, ziemiaRect)
    display_surface.blit(mars, marsRect)
    display_surface.blit(ksiezyc, ksiezycRect)

    display_surface.blit(inputbox, inputboxRect)
    display_surface.blit(text, textRect)

    inputbox = font.render(inputtext, True, (200, 200, 200), (0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        if circle.collidepoint(pygame.mouse.get_pos()):
            hmax = y
            mx , my = pygame.mouse.get_pos()
            y = 875 - my
            x = mx
            hstop = 0.1
            freefall = True
            rho = 0.75
            t = 1
            tau = 0.1
            t_last = 0
            v = 0
            if hmax > 0:
                vmax = sqrt(2 * hmax * g)
            else:
                vmax = 0

        elif ziemiaRect.collidepoint(pygame.mouse.get_pos()):
            ziemia = font.render('Ziemia', True, (0, 0, 0), (0, 150, 0))
            mars = font.render('Mars', True, (200, 200, 200), (0, 0, 0))
            ksiezyc = font.render('Kśiężyc', True, (200, 200, 200), (0, 0, 0))
            g = 9.81
            freefall = False

        elif marsRect.collidepoint(pygame.mouse.get_pos()):
            ziemia = font.render('Ziemia', True, (200, 200, 200), (0, 0, 0))
            mars = font.render('Mars', True, (0, 0, 0), (0, 150, 0))
            ksiezyc = font.render('Kśiężyc', True, (200, 200, 200), (0, 0, 0))
            g = 3.72
            freefall = False

        elif ksiezycRect.collidepoint(pygame.mouse.get_pos()):
            ziemia = font.render('Ziemia', True, (200, 200, 200), (0, 0, 0))
            mars = font.render('Mars', True, (200, 200, 200), (0, 0, 0))
            ksiezyc = font.render('Kśiężyc', True, (0, 0, 0), (0, 150, 0))
            g = 1.62
            freefall = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inputboxRect.collidepoint(pygame.mouse.get_pos()):
                inputactive = True
                inputtext = ""
        elif event.type == pygame.KEYDOWN and inputactive:

            if event.key == pygame.K_RETURN:
                inputactive = False
                dt = float(inputtext) * 0.05
            elif event.key == pygame.K_BACKSPACE:
                inputtext = inputtext[:-1]
            else:
                inputtext += event.unicode

    if inputactive:
        inputbox = font.render(inputtext, True, (0, 0, 0), (0, 150, 0))

    pygame.display.flip()

pygame.quit()
