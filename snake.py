from wiggleface import *
import random
import math

w = wiggleface()
w.score = 0
w.x = 4
w.y = 4
w.snake = []
w.delayMax = 30
w.delay = w.delayMax
w.direction = 2
w.fillWiggle(False)
w.lastPress = -1
def update():
    if w.time % 5 != 0: # Slow things down.
        return
    w.text = "Score: " + str(w.score)
    w.grid[w.x][w.y] = (4, False)

    # Handle input.
    w.lastPress = 0 if w.keys[w.Key_Up] else 1 if w.keys[w.Key_Right] else 2 if w.keys[w.Key_Down] else 3 if w.keys[w.Key_Left] else w.lastPress

    # Time to move
    if w.time % 90 == 0:
        # Clear old position?
        w.grid[w.x][w.y] = (0, False)
        # Change direction only if player pressed a key and it is to the left or right of current direction.
        if w.lastPress != -1 and w.direction != (w.lastPress+2)%4:
            w.direction = w.lastPress
        # Update position.
        w.x = w.x+1 if w.direction == 1 else w.x-1 if w.direction == 3 else w.x
        w.y = w.y+1 if w.direction == 2 else w.y-1 if w.direction == 0 else w.y
        w.lastpress = -1

    # Game over conditions: hit self or wall.

    # Fruit.

w.start(update)