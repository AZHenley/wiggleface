from wiggleface import *
import random
import math

w = wiggleface()
w.score = -1
w.snake = [(4,4)]
w.delayMax = 30
w.delay = w.delayMax
w.direction = 2
w.fillWiggle(False)
w.lastPress = 0
w.fruit = (8,8)
w.justAte = False
w.gameOver = False
def init():
    w.grid[w.fruit[0]][w.fruit[1]] = (2,True)
def update():
    if w.time % 5 != 0 or w.gameOver: # Slow things down.
        return
    w.text = "Score: " + str(w.score)
    x,y = w.snake[0]

    # Fruit.
    if (x,y) == w.fruit:
        w.fruit = (random.randrange(0,w.width), random.randrange(0,w.height))
        w.grid[w.fruit[0]][w.fruit[1]] = (2,True)
        w.score += 1
        #w.snake.insert(0,w.snake[0])
        w.justAte = True

    # Handle input.
    w.lastPress = 0 if w.keys[w.Key_Up] else 1 if w.keys[w.Key_Right] else 2 if w.keys[w.Key_Down] else 3 if w.keys[w.Key_Left] else w.lastPress

    # Time to move
    if w.time % 90 == 0:
        # Change direction only if player pressed a key and it is to the left or right of current direction.
        if w.lastPress != -1 and w.direction != (w.lastPress+2)%4:
            w.direction = w.lastPress
        # Update position.
        x = x+1 if w.direction == 1 else x-1 if w.direction == 3 else x
        y = y+1 if w.direction == 2 else y-1 if w.direction == 0 else y
        w.lastpress = -1

        # Game over conditions: hit self or wall.
        if x == -1 or y == -1 or x == w.width or y == w.height or w.grid[x][y][0] == 4:
            w.gameOver = True
            w.fill(1,True)
            w.text += "   GAMEOVER!"
            return

        # Grow!
        w.snake.insert(0,(x,y))
        w.grid[x][y] = (4,False)
        # If a fruit wasn't just eaten.
        if not w.justAte:
            w.grid[w.snake[-1][0]][w.snake[-1][1]] = (0,False)
            w.snake.pop()
        w.justAte = False

w.start(init,update)