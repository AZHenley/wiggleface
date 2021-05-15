#Built on the rainbow.py example
#Speedshoot by Bryce Bible
#Very rudimentary speed/accuracy crosshair game with lots of legacy code left in that I was too lazy to remove

from wiggleface import *
import random

w = wiggleface()
w.text = "Welcome to Wiggleface."

w.crosshairx = 7
w.crosshairy = 8

w.lastPress = -1
w.drawShoot = False

pointspots = [[2, 2], [10, 10], [8, 8], [6, 6]]

w.points = 0
w.frames = 0
w.adder = 0

w.health = 1000

w.speed = 60
w.gameover = False
w.lingermessage = False
w.lingercount = 0

#Hit the targets with the crosshair! The more targets on screen, the faster you lose health and the faster the targets come!
#Hit a deadshot to boost health and slow down the targets in addition to some sweet extra points!
def getcolor():
    if w.drawShoot:
        return 5
    else:
        return 1
def update():
    if w.health <= 0:
        w.gameover = True
    if w.gameover == True:
        for x in range(w.columns):
            for y in range(w.rows):
                w.grid[x][y] = (1, True)
                w.text = "Game over! You scored " + str(w.points)
        return


    w.text = "Points: " + str(w.points) + " - Health: " + str(w.health) + " - Speed: " + str(w.speed)
    w.frames += 1
    w.adder += 1
    if (w.lingermessage and w.lingercount):
        w.lingercount -= 1
        w.text = w.lingermessage
    if not w.frames % 2 == 0:
        return
    # Handle input.
    w.lastPress = 0 if w.keys[w.Key_Up] else 1 if w.keys[w.Key_Right] else 2 if w.keys[w.Key_Down] else 3 if w.keys[w.Key_Left] else 4 if w.keys[w.Key_Space] else w.lastPress

    if w.adder >= w.speed:
        w.speed -= 5
        pointspots.insert(0,[random.randint(0,15), random.randint(0,15)])
        w.adder = 0
        w.health -= (len(pointspots) * 10)
    if w.lastPress != -1:
        if w.lastPress == 1:
            w.crosshairx += 1
        if w.lastPress == 3:
            w.crosshairx -= 1
        if w.lastPress == 0:
            w.crosshairy -= 1
        if w.lastPress == 2:
            w.crosshairy += 1

        if w.lastPress == 4:
            w.drawShoot = True
            #w.text = "Bang"
            #w.lingermessage = w.text
            w.lingercount = 10
        w.lastPress = -1

    for j in range(w.columns):
        for k in range(w.rows):
            #m = False if j == 0 or j == w.columns-1 or k == 0 or k == w.rows-1 else True
            #w.grid[j][k] = ((j+k+(w.time//15))%8, m)

            if w.crosshairx > 15 or w.crosshairx < 0:
                w.crosshairx %= 16
            if w.crosshairy > 15 or w.crosshairy < 0:
                w.crosshairy %= 16

            if j == w.crosshairx:
                w.grid[j][k] = (1, w.drawShoot)
            if k == w.crosshairy:
                w.grid[j][k] = (1, w.drawShoot)
            if j != w.crosshairx and k != w.crosshairy:
                w.grid[j][k] = (0, False)

            if [j,k] in pointspots:
                w.grid[j][k] = (2, True)

            if [w.crosshairx, w.crosshairy] in pointspots and w.drawShoot:
                pointspots.remove([w.crosshairx, w.crosshairy])
                w.text = "Deadshot! Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 10
                w.speed += 5
                w.health += 10

            #Big crosshair
            if ([w.crosshairx+1, w.crosshairy+1] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx+1, w.crosshairy+1])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1
                
            if ([w.crosshairx+1, w.crosshairy-1] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx+1, w.crosshairy-1])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1
                
            if ([w.crosshairx-1, w.crosshairy+1] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx-1, w.crosshairy+1])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1
                
            if ([w.crosshairx-1, w.crosshairy-1] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx-1, w.crosshairy-1])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1


            if ([w.crosshairx, w.crosshairy-1] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx, w.crosshairy-1])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1
                
            if ([w.crosshairx, w.crosshairy+1] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx, w.crosshairy+1])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1

            if ([w.crosshairx-1, w.crosshairy] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx-1, w.crosshairy])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1

            if ([w.crosshairx+1, w.crosshairy] in pointspots) and w.drawShoot:
                pointspots.remove([w.crosshairx+1, w.crosshairy])
                w.text = "Nice shot!"
                w.lingermessage = w.text
                w.lingercount = 10
                w.points += 1                                
                


            #if w.drawShoot == True:
                #if j == (w.crosshairx + 2) or j == (w.crosshairx - 2):
                    #w.grid[j][k] = (1, False)
                #if k == (w.crosshairy + 2) or j == (w.crosshairy - 2):
                    #w.grid[j][k] = (1, False)
    #w.grid[w.crosshairx+1][w.crosshairy+1] = (1, w.drawShoot)
    #w.grid[w.crosshairx-1][w.crosshairy-1] = (1, w.drawShoot)
    #w.grid[w.crosshairx+1][w.crosshairy+1] = (1, w.drawShoot)
    #w.grid[w.crosshairx-1][w.crosshairy-1] = (1, w.drawShoot)
    if (w.crosshairx < 15):
        if (w.crosshairy < 15):
            w.grid[w.crosshairx+1][w.crosshairy+1] = (getcolor(), w.drawShoot)
        if (w.crosshairy > 0):
            w.grid[w.crosshairx+1][w.crosshairy-1] = (getcolor(), w.drawShoot)
    if (w.crosshairy < 15):
        if (w.crosshairx > 0):
            w.grid[w.crosshairx-1][w.crosshairy+1] = (getcolor(), w.drawShoot)
        if (w.crosshairx > 0 and w.crosshairy > 0):
            w.grid[w.crosshairx-1][w.crosshairy-1] = (getcolor(), w.drawShoot)
    w.grid[w.crosshairx][w.crosshairy] = (3, w.drawShoot)
    w.drawShoot = False
w.start(lambda:None,update)