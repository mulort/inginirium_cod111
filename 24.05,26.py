'''
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

win.fill((255, 255, 255))
pygame.draw.rect(win, (255, 255, 0), (50, 50, 100, 100))
pygame.draw.circle(win, (0, 255, 255), (50, 100), 20)

pygame.draw.polygon(win, (0, 0, 0), [(0, 100), (100, 50), (100, 150)], False)
pygame.draw.line(win, (0, 255, 255), (0, 0), (100, 100), 5)
pygame.draw.lines(win, (0, 0, 0), True, ((200, 200), (300, 150), (300, 250)), 10)

pygame.display.update()


win.fill((255, 255, 255))
    pygame.display.update()

win.fill((255, 255, 255))
pygame.draw.rect(win, (255,255, 0), (50, 50, 100, 100))
pygame.display.update()


import pygame
pygame.init()
x = int(input())
y = int(input())
win = pygame.display.set_mode((x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((0, 0, 0))
    pygame.draw.line(win, (255, 255, 255), (0, 0), (x, y), 5)
    pygame.draw.line(win, (255, 255, 255), (x, 0), (0, y), 5)
    pygame.display.update()'''