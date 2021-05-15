# Isaac Sikkema, 04-22-2021


from wiggleface import *
import random


class Game:
    def __init__(self, wf, win=None, lose=None):
        self.wf = wf
        self.win = win
        self.lose = lose

        self.objects = {}
        self.functions = {}
        self.moves = {}
        self.draws = {}
        self.key_binds = {}
    
    def add_object(self, obj):
        if len(self.objects) == 0:
            key = 0
        else:
            key = list(self.objects.keys())[-1] + 1
        
        self.objects[key] = obj
        return key
    
    def remove_object(self, key):
        try:
            del self.moves[key]
        except IndexError:
            pass

        try:
            del self.draws[key]
        except IndexError:
            pass

        del self.objects[key]

    def run_every(self, function, ticks=1):
        if len(self.functions) == 0:
            key = 0
        else:
            key = list(self.functions.keys())[-1] + 1

        self.functions[key] = (function, ticks)
        return key
    
    def move_every(self, key, ticks=1):
        self.moves[key] = ticks
    
    def draw_every(self, key, ticks=1):
        self.draws[key] = ticks

    def bind_key(self, key, function):
        self.key_binds[key] = function

    def run(self):
        for _k, (f, t) in self.functions.items():
            if self.wf.time % t == 0:
                f(self)
    
    def move(self):
        for k, t in self.moves.items():
            if t == 0:
                continue

            if self.wf.time % t == 0:
                self.objects[k].move()

    def draw(self):
        for k, t in self.draws.items():
            if t == 0:
                continue

            if self.wf.time % t == 0:
                self.objects[k].draw()
    
    def run_key_binds(self):
        for key, f in self.key_binds.items():
            if self.wf.keys[key]:
                f(self)

    def win_screen(self):
        self.wf.fill(4, True)
        self.wf.text = "You Win!"
    
    def lose_screen(self):
        self.wf.fill(1, True)
        self.wf.text = "Game Over."

    def play(self):
        if self.win is not None:
            if self.win(self):
                self.win_screen()
                return
        if self.lose is not None:
            if self.lose(self):
                self.lose_screen()
                return
        
        self.run_key_binds()
        self.run()
        self.move()
        self.draw()


class GameObject:
    BLOCK = 1
    WRAP = 2
    GHOST = 3

    def __init__(self, wf, pixels=None, wall_x=GHOST, wall_y=GHOST):
        if pixels is None:
            pixels = {}
        
        self.wf = wf
        self.pixels = pixels
        self.wall_x = wall_x
        self.wall_y = wall_y

        self.bounds = None
        self.__calc_bounds()
    
    def __calc_bounds(self):
        if len(self.pixels) == 0:
            self.bounds = None
            return
        
        maxx = 0
        maxy = 0
        minx = self.wf.columns-1
        miny = self.wf.rows-1
        for x, y in self.pixels:
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        
        self.bounds = ((minx, miny), (maxx, maxy))

    def __wraploc(self, loc):
        x, y = loc
        if self.wall_x == GameObject.WRAP:
            x = x % self.wf.columns
        if self.wall_y == GameObject.WRAP:
            y = y % self.wf.rows
        
        return (x, y)

    def draw(self):
        for k, v in self.pixels.items():
            x, y = k
            c, w = v
            if x < 0 or x >= self.wf.columns:
                continue
            if y < 0 or y >= self.wf.rows:
                continue

            self.wf.grid[x][y] = (c, w)
    
    def set_pixel(self, x, y, c, w):
        default = self.pixels.get((x, y))
        if default is None:
            default = self.wf.grid[x][y]
        
        dc, dw = default
        if c is None:
            c = dc
        if w is None:
            w = dw
        
        self.pixels[(x, y)] = (c, w)
        self.__calc_bounds()
    
    def move(self, dx, dy):
        if self.bounds is None:
            return

        ((minx, miny), (maxx, maxy)) = self.bounds
        if self.wall_x == GameObject.BLOCK:
            if not (minx+dx >= 0 and maxx+dx < self.wf.columns):
                return
        if self.wall_y == GameObject.BLOCK:
            if not (miny+dy >= 0 and maxy+dy < self.wf.rows):
                return
        
        new_pixels = {}
        for loc, v in self.pixels.items():
            x, y = loc
            new_pixels[self.__wraploc((x+dx, y+dy))] = v
        
        self.pixels = new_pixels
        self.__calc_bounds()
    
    def collides_with(self, obj):
        for a in self.pixels:
            for b in obj.pixels:
                if a == b:
                    return True
        
        return False


class Background(GameObject):
    def __init__(self, wf):
        super().__init__(wf)

        for x in range(self.wf.columns):
            for y in range(self.wf.rows):
                self.set_pixel(x, y, 0, False)


class Barrier(GameObject):
    def __init__(self, wf):
        super().__init__(wf)

        start = random.randrange(0, self.wf.columns)
        size = random.randrange(8, self.wf.columns-3)
        
        c = 1
        w = True
        for i in range(size):
            self.set_pixel((start+i)%self.wf.columns, -1, c, w)
    
    def move(self):
        super().move(0, 1)


class Player(GameObject):
    def __init__(self, wf):
        super().__init__(wf, wall_x=GameObject.WRAP, wall_y=GameObject.BLOCK)

        self.set_pixel(8, 12, 5, True)


def lose(game):
    for b in game.wf.barriers:
        if game.wf.player.collides_with(game.objects[b]):
            return True
    
    return False

def move_right(game):
    game.wf.player.move(1, 0)

def move_left(game):
    game.wf.player.move(-1, 0)

def move_up(game):
    game.wf.player.move(0, -1)

def move_down(game):
    game.wf.player.move(0, 1)

def new_barrier(game):
    b = Barrier(game.wf)
    key = game.add_object(b)
    game.move_every(key, 10)
    game.draw_every(key)

    game.wf.barriers.append(key)

def remove_barriers(game):
    barriers = game.wf.barriers
    for b in barriers:
        if game.objects[b].bounds[0][1] >= game.wf.rows:
            game.remove_object(b)
            barriers.remove(b)


wf = wiggleface()


def init():
    wf.fillWiggle(False)
    wf.barriers = []

    wf.game = Game(wf, lose=lose)

    wf.game.bind_key(wf.Key_Right, move_right)
    wf.game.bind_key(wf.Key_Left, move_left)
    wf.game.bind_key(wf.Key_Up, move_up)
    wf.game.bind_key(wf.Key_Down, move_down)

    wf.game.run_every(new_barrier, 50)
    wf.game.run_every(remove_barriers)

    b = wf.game.add_object(Background(wf))
    wf.game.draw_every(b)

    wf.player = Player(wf)
    p = wf.game.add_object(wf.player)
    wf.game.draw_every(p)

def update():
    wf.game.play()


wf.start(init, update)
