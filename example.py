import os, sys
import random
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

size = width, height = 700, 600
speed = [1, 1]
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0 , 0
black = 0, 0, 0
cellwidth = 20
cellheight = 20
margin = 2
totalRows = 20
totalColumns = 25

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

grid = []

class Cell(object):
    def __init__(self):
        self.mine = False

for row in range(totalRows):
    grid.append([])
    for column in range(totalColumns):
        cell = Cell()
        grid[row].append(cell)

locs = [(row, col) for row in range(totalRows) for col in range(totalColumns)]
random.shuffle(locs)
for row, col in locs[:10]:
    grid[row][col].mine = True
    print("Mine added: ", row, col)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (cellwidth + margin)
            row = pos[1] // (cellheight + margin)
            if event.button == 1:
                print("You pressed the left mouse button at:", pos, ":", column, row)
                grid[row][column].mine = True
            elif event.button == 3:
                print("You pressed the right mouse button at:", pos, ":", column, row)
                grid[row][column].mine = False

    screen.fill(black)
    for row in range(totalRows):
        for column in range(totalColumns):
            cellColor = white
            if grid[row][column].mine == True:
                cellColor = red
            cellX = (margin + cellwidth) * column + margin
            cellY = (margin + cellheight) * row + margin
            cell = pygame.Rect([cellX, cellY, cellwidth, cellheight])
            
            pygame.draw.rect(screen, cellColor, cell)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
