from wiggleface import *

w = wiggleface()
w.text = "Welcome to Wiggleface."
def update():
    for j in range(w.columns):
        for k in range(w.rows):
            m = False if j == 0 or j == w.columns-1 or k == 0 or k == w.rows-1 else True
            w.grid[j][k] = ((j+k+(w.time//30))%8, m)
w.start(lambda:None,update)