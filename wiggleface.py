# Austin Henley, 4/28/2021
import pygame
import math

class wiggleface:
    def __init__(self):
        print("Creating Wiggleface instance.")
        pygame.init()
        self.surface = pygame.display.set_mode((480,480))
        pygame.display.set_caption("Wiggleface")
        self.time = 1000
        self.font = pygame.font.SysFont("Arial", 18)
        # Color palette: https://lospec.com/palette-list/endesga-8
        self.colors = [(253,253,248), (211,39,52), (218,125,34), (230,218,41), (40,198,65), (45,147,221), (123,83,173), (27,28,51)]
        self.columns = 16
        self.rows = 16
        self.xOffset = 32
        self.yOffset = 32
        self.xGap = 8
        self.yGap = 8
        self.width = 16
        self.height = 16
        self.grid = [[(0,True)]*self.rows for z in range(self.columns)]
        self.text = ""

        # Keys.
        self.Key_Enter = pygame.K_RETURN
        self.Key_Space = pygame.K_SPACE
        self.Key_W = pygame.K_w
        self.Key_A = pygame.K_a
        self.Key_S = pygame.K_s
        self.Key_D = pygame.K_d
        self.Key_Up = pygame.K_UP
        self.Key_Down = pygame.K_DOWN
        self.Key_Left = pygame.K_LEFT
        self.Key_Right = pygame.K_RIGHT

    def start(self, init, update):
        print("Starting Wiggleface game loop.")
        init() # Call game's init function.
        done = False
        while not done:
            # Lock the framerate.
            pygame.time.Clock().tick(30)
            # Handle input.
            self.keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                    print("Shutting down Wiggleface.")
                    done = True
            # Clear screen.
            self.surface.fill(self.colors[-1])
            # Run game logic.
            update()

            scaling = math.sin(self.time/3)*4
            rot = self.time*3
            for j in range(self.columns):
                for k in range(self.rows):
                    tX = self.xOffset + j * (self.width + self.xGap)
                    tY = self.yOffset + k * (self.height + self.yGap)
                    c = self.grid[j][k][0]
                    # Check if cell is wiggling.
                    if self.grid[j][k][1]:
                        rectrot(self.surface, self.colors[c], pygame.Rect((tX, tY), (self.width-scaling, self.height-scaling)), 0, 1, rot)
                    else:
                        rectrot(self.surface, self.colors[c], pygame.Rect((tX, tY), (math.ceil(self.width*0.85), math.ceil(self.height*0.85))), 0, 1, 0)

            textObj = self.font.render(self.text, True, self.colors[0])
            self.surface.blit(textObj, (self.xOffset, tY + self.height*2))

            pygame.display.flip()
            self.time += 1

        # Done! Time to quit.
        pygame.quit()

    def fill(self, c, m):
            for j in range(self.columns):
                for k in range(self.rows):
                    self.grid[j][k] = (c,m)
    
    def fillColor(self, c):
            for j in range(self.columns):
                for k in range(self.rows):
                    self.grid[j][k] = (c,self.grid[j][k][1])

    def fillWiggle(self, m):
            for j in range(self.columns):
                for k in range(self.rows):
                    self.grid[j][k] = (self.grid[j][k][0],m)

# https://stackoverflow.com/a/66688131/938695
def rectrot(surface, color, pos, fill, border_radius, angle):
    # Angle is in degrees.
    max_area = max(pos[2],pos[3])
    s = pygame.Surface((max_area,max_area))
    s = s.convert_alpha()
    s.fill((0,0,0,0))
    pygame.draw.rect(s, color,(0,0,pos[2],pos[3]),fill, border_radius=border_radius)
    s = pygame.transform.rotate(s,angle)
    surface.blit(s,(pos[0],pos[1]))
