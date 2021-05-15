#Author: Rachel Offutt
#Game: Minesweeper - Hella Messed up version
#Looooooot of work to do
from wiggleface import *
import random
import math

w = wiggleface()
w.BOMBS = 10
w.snake = [(random.randint(0,10),random.randint(0,10))]
w.delayMax = 15 # This controls the speed of the game.
w.delay = w.delayMax
w.direction = 2
w.fillWiggle(False)
w.lastPress = -1

bombs = { (random.randint(0,15),random.randint(0,15)), 
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15)),
        (random.randint(0,15),random.randint(0,15))}
w.justAte = False
w.gameOver = False

def updateBoardColors():
    posx, posy = w.snake[0]
    
    for i in range(-1, 1):
        for j in range(-1, 1):
            posx, posy = w.snake[0]
            posx += i
            posy += j

            if posx <= -1:
                posx = 0
            if posy <= -1: 
                posy = 0
            if posy == w.height:
                posy = w.height -1
            if posx == w.width:
                posx = w.width -1

            neighborbombs = 0
            for a in range(-1, 1):
                for b in range(-1, 1):
                    neighX = posx + a
                    if neighX <= -1:
                        neighX = 0
                    if neighX == w.width:
                        neighX = w.width -1

                    neighY = posy + b
                    if neighY <= -1:
                        neighY = 0
                    if neighY == w.height:
                        neighY = w.height -1

                    if (neighX, neighY) in bombs:
                        neighborbombs += 1
            if (posx, posy) in bombs:
                w.grid[posx][posy] = (4, True)
            w.grid[posx][posy] = (neighborbombs, False)


    numBombsClose = 0


def init():
    w.fill(6, False)

def update():
    w.text = "Bombs On Field: " + str(w.BOMBS)
    w.delay -= 1
    x,y = w.snake[0]
    
    # If we have hit a bomb
    if (x,y) in bombs:
        # TODO: Check if new position is not on top of the snake.
        w.gameOver =True
        w.fill(1, True)
        w.text += "      GAMEOVER"
        return
    
    # Handle input.
    w.lastPress = 0 if w.keys[w.Key_Up] else 1 if w.keys[w.Key_Right] else 2 if w.keys[w.Key_Down] else 3 if w.keys[w.Key_Left] else w.lastPress

    # Time to move
    if w.delay == 0:
        w.delay = w.delayMax # TODO: Decrement delay max to increase game speed (and difficulty).
        # Change direction only if player pressed a key and it is to the left or right of current direction.
        if w.lastPress != -1 and w.direction != (w.lastPress+2)%4:
            w.direction = w.lastPress
        # Update position.
        x = x+1 if w.direction == 1 else x-1 if w.direction == 3 else x
        y = y+1 if w.direction == 2 else y-1 if w.direction == 0 else y
        w.lastpress = -1

        #w.grid[x][y][0] == 4
        # Wall bounds
        if x == -1:
            x = 0
        if y == -1:
            y = 0
        if x == w.width:
            x = w.width - 1
        if y == w.height:
            y = w.height -1
            

        
        updateBoardColors()
        w.snake.insert(0,(x,y))
        w.grid[x][y] = (4,False)

        # Move our player around to the newest position
        w.grid[w.snake[-1][0]][w.snake[-1][1]] = (0,False)
        w.snake.pop()
        w.justAte = False


w.start(init,update)
