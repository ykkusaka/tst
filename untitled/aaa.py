import matplotlib.pyplot as plt
import random
from math import *

n=int(input('n:'));
q=[.5,.33,.38,.33,.29,.28][n-3];r=100
x=[];y=[];v=[];loopCount=10**5
for i in range(n):v.append([r*sin(i*pi*2/n),r*cos(i*pi*2/n)])
p=v[0]
for _ in[0]*loopCount:
    a=~-random.randint(1,n)
    x.append(p[0]);y.append(p[1])
    p=[p[0]*q+v[a][0]*(1-q),p[1]*q+v[a][1]*(1-q)]
    #plt.xlim(-90,90);plt.ylim(-50,100)
    #plt.plot(x[-1],y[-1],'.r',ms=3);plt.pause(.01)
plt.xlim(min(x),max(x));plt.ylim(min(y),max(y))
plt.plot(x,y,'.r',ms=3);plt.show()

'''
# x, y = [0], [0]
# loopCount=int(1e+5)
# def f(p,d):
#     global x,y
#     x.insert(0,abs(x[0]+p[0])/d)
#     y.insert(0,abs(y[0]+p[1])/d)
# def triangle(r=6,a=[500, 1000],b=[1000, 0],c=[0, 0]):
#     for _ in[0]*loopCount:
#         n=random.randint(1,r);div=2
#         if n<3:f(a,div)
#         elif n<5:f(b,div)
#         else:f(c,div)
#         #plt.plot(x[0],y[0],'.r',ms=3);plt.pause(.1)
# def square(r=8,a=[200, 1000],b=[1000, 1000],c=[800, 0],d=[0,0]):
#     for _ in[0]*loopCount:
#         n=random.randint(1,r);div=3
#         if n<3:f(a,div)
#         elif n<5:f(b,div)
#         elif n<7:f(c,div)
#         else:f(d,div)
# def pentagon(r=10,a=[1,0],b=[0.3090169943749474241023, 0.9510565162951535721164],c=[-0.8090169943749474241023, 0.5877852522924731291687],d=[-0.8090169943749474241023,- 0.5877852522924731291687]
#     ,e=[0.3090169943749474241023,-0.9510565162951535721164]):
#     s=[a[0],b[0],c[0],d[0],e[0],a[0]];t=[a[1],b[1],c[1],d[1],e[1],a[1]]
#     #plt.plot(s,t)
#     for _ in[0]*loopCount:
#         n=random.randint(1,r);div=3.8
#         if n<3:f(a,div)
#         elif n<5:f(b,div)
#         elif n<7:f(c,div)
#         elif n<9:f(d,div)
#         else:f(e,div)
# num=int(input())
# if num==3:triangle()
# elif num==4:square()
# elif num==5:pentagon()
# #plt.xlim([-10,max(x)+10]);plt.ylim([-10,max(y)+10])
# plt.plot(x,y,'.r',ms=3);plt.show()
'''
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
import pygame
import numpy
import calendar
'''