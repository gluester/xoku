import pygame
from pygame.locals import *
from roku import Roku
tvIP = input("Please provide your TVs IP address (settings > network): ")
roku = Roku(tvIP)

pygame.init()
pygame.display.set_caption("Roku Controller")
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock
try:
    # sets all the controller stuff
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]; joystick = pygame.joystick.Joystick(0); joystick.init()
except:
    print("No controller")
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                roku.left()
            elif event.key == pygame.K_UP:
                roku.up()
            elif event.key == pygame.K_DOWN:
                roku.down()
            elif event.key == pygame.K_RIGHT:
                roku.right()
            elif event.key == pygame.K_ESCAPE:
                roku.back()
            elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                roku.select()
            elif event.key == pygame.K_HOME or event.key == pygame.K_BACKSPACE:
                roku.home()
        if event.type == JOYBUTTONDOWN:
            print(event)
            if event.button == 0:
                roku.select()
            if event.button == 10:
                roku.home()
            if event.button == 6 or event.button == 7:
                roku.info()
            if event.button == 1:
                roku.back()
        if event.type == JOYHATMOTION:
            print(event)
            if event.value == (0, -1):
                roku.down()
            if event.value == (0, 1):
                roku.up()
            if event.value == (1, 0):
                roku.right()
            if event.value == (-1, 0):
                roku.left()
