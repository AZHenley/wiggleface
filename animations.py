from wiggleface import *
import random
import math

w = wiggleface()
w.text = "Just add techno music..."
w.t = 0
def update():
    t = w.t % 320
    for j in range(w.columns):
        for k in range(w.rows):
            if t < 80:
                c = random.randint(4, 6) if t % 25 == 0 else w.grid[j][k][0]
                m = True if j==t%(w.width*3)//3 else False
            elif t < 160:
                c = 0 if k-1 <= t%(w.height*2)//2 <= k+1 else 2
                m = False
            elif t < 240:
                c = round(math.sin(t-math.sqrt((k-5)**2+(j-3)**2)))%8 if t%5==0 else w.grid[j][k][0]
                m = False
            elif t < 320:
                c = (j+k+(w.time//15))%8
                m = False if j == 0 or j == w.columns-1 or k == 0 or k == w.rows-1 else True
            w.grid[j][k] = (c, m)
    w.t += 1
w.start(lambda:None,update)