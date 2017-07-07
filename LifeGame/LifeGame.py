import pygame as pg,random,time,csv
from pygame.locals import *

scrRect = pg.Rect(0, 0, 800, 640)
cellSize = 1<<3
row = scrRect.height // cellSize
col = scrRect.width // cellSize
dead, alive = 0, 1
RAND_LIFE =.2
sleep_time=.0

class LifeGame:
    def __init__(self):
        pg.init()
        screen = pg.display.set_mode(scrRect.size)
        self.field = [[dead for x in range(col)] for y in range(row)]
        self.generation = 0
        self.run = False
        self.cursor = [col / 2, row / 2]
        self.clear()
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            self.update()
            self.draw(screen)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:pg.quit();exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:pg.quit();exit()
                    elif event.key == pg.K_LEFT:
                        self.cursor[0] -= 1
                        if self.cursor[0] < 0: self.cursor[0] = 0
                    elif event.key == pg.K_RIGHT:
                        self.cursor[0] += 1
                        if self.cursor[0] > col-1: self.cursor[0] = col - 1
                    elif event.key == pg.K_UP:
                        self.cursor[1] -= 1
                        if self.cursor[1] < 0: self.cursor[1] = 0
                    elif event.key == pg.K_DOWN:
                        self.cursor[1] += 1
                        if self.cursor[1] > row-1: self.cursor[1] = row - 1
                    elif event.key == pg.K_SPACE:
                        x, y = map(int,self.cursor)
                        if self.field[y][x] == dead:self.field[y][x] = alive
                        elif self.field[y][x] == alive:self.field[y][x] = dead
                    elif event.key == pg.K_s:self.run = not self.run
                    elif event.key == pg.K_n:self.step()
                    elif event.key == K_c:self.clear()
                    elif event.key == K_r:self.rand()
                    elif event.key == K_h:
                        t=open(input('save as:')+'.csv','w+')
                        f=csv.writer(t)
                        f.writerows(self.field)
                        t.close()
                    elif event.key == K_o:
                        t = open(input('open:')+'.csv', 'r')
                        f = csv.reader(t);yy=0
                        for rows in list(f)[::2]:
                            for xx,columns in enumerate(rows):self.field[yy][xx]=int(columns)
                            yy+=1
                        t.close()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    px, py = event.pos
                    x, y = px // cellSize, py // cellSize
                    self.cursor = [x, y]
                    if self.field[y][x] == dead:self.field[y][x] = alive
                    elif self.field[y][x] == alive:self.field[y][x] = dead
    def clear(self):
        self.generation = 0
        for y in range(row):
            for x in range(col):self.field[y][x] = dead
    def rand(self):
        for y in range(row):
            for x in range(col):
                if random.random() < RAND_LIFE:self.field[y][x] = alive
    def update(self):
        if self.run:self.step();time.sleep(sleep_time)
    def step(self):
        next_field = [[False for x in range(col)] for y in range(row)]
        for y in range(row):
            for x in range(col):
                num_alive_cells = self.around(x, y)
                if num_alive_cells == 2:next_field[y][x] = self.field[y][x]
                elif num_alive_cells == 3:next_field[y][x] = alive
                else:next_field[y][x] = dead
        self.field = next_field
        self.generation += 1
    def draw(self, screen):
        for y in range(row):
            for x in range(col):
                if self.field[y][x] == alive:pg.draw.rect(screen, (0xff, 0xff, 0xff), Rect(x * cellSize, y * cellSize, cellSize, cellSize))
                elif self.field[y][x] == dead:pg.draw.rect(screen, (0x00, 0x00, 0x00), Rect(x * cellSize, y * cellSize, cellSize, cellSize))
                if cellSize>1<<2:pg.draw.rect(screen, (0x32,0x32,0x32), Rect(x * cellSize, y * cellSize, cellSize, cellSize), 1)
        pg.draw.rect(screen, (0x00,0x00,0xff), Rect(self.cursor[0] * cellSize, self.cursor[1] * cellSize, cellSize, cellSize), 1)
        pg.display.set_caption(u"Conway's Game of Life"+' '*25+"generation:%d space : birth/kill s : start/stop n : next r : random"% self.generation)
    def around(self, x, y):
        return sum([self.field[~-y][~-x],
                    self.field[~-y][x],
                    self.field[~-y][-~x%col],
                    self.field[y][~-x],
                    self.field[y][-~x%col],
                    self.field[-~y%row][~-x],
                    self.field[-~y%row][x],
                    self.field[-~y%row][-~x%col]])

LifeGame()

'''
import math
from math import *
import sys
import fractions *
from fractions import *
import datetime
from datetime import *
import queue
import re
from re import *
import itertools
import bisect
import functools
import random
import time
import heapq
from heapq import *
import string
import collections
import decimal
'''