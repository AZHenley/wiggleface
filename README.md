# The Wiggleface Game Engine

![](animations.gif)

Wiggleface is a silly game engine created as an in-class activity for my students. It gives you access to 16x16 wiggling pixels with a restricted palette of 8 colors running at 30 FPS.

See rainbow.py, animations.py, or snake.py for example usage. Needs `pip install pygame`. Play the examples like `python3 snake.py`.

## Using Wiggleface

You only need `wiggleface.py`. A game can be created by supplying the engine with two functions, like so:

    from wiggleface import *
    w = wiggleface()
    def init():
        pass
    def update():
        pass
    w.start(init, update)
    
When you call `w.start()`, it will execute your `init()` once and then will execute `update()` each frame until the game ends.

To draw to the screen, set `w.grid[x][y]` with a tuple containing a value between 0 and 7 representing the color and a boolean for whether the pixel should wiggle or not. The palette could be found [here](https://lospec.com/palette-list/endesga-8). For example: `w.grid[3][8] = (2,True)` will set the pixel at (3,8) to be orange and wiggling.

You can output a single line of text below the grid of pixels by setting `w.text`. It is useful for displaying the score or short messages to the player.

The number of frames elapsed is stored in `w.time` and can be used for timing. 

For input, the state of keys are stored in `w.keys` as a boolean and are updated each frame automatically. Access these using the predefined key constants, like `w.keys[w.Key_Left]`.

A few helper functions exist for setting all of the pixels: `fill(c,m)`, `fillColor(c)`, and `fillWiggle(m)`.

<img src="https://github.com/AZHenley/wiggleface/blob/main/snake.png" height="400" width="400" >
