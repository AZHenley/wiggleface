# Importing the library
import pygame
import math

class wiggleface:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800,600))
        self.time = 1000
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

    def start(self, update):
        # Run until the user asks to quit
        done = False
        while not done:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Fill the background with white
            self.surface.fill(self.colors[-1])

            update()

            scaling = math.sin(self.time/30)*5
            for j in range(self.columns):
                for k in range(self.rows):
                    tX = self.xOffset + j * (self.width + self.xGap)
                    tY = self.yOffset + k * (self.height + self.yGap)
                    #c = (j+k+(self.time//30))%8
                    c = self.grid[j][k][0]
                    if self.grid[j][k][1]:
                        rectrot(self.surface, self.colors[c], pygame.Rect((tX, tY), (self.width-scaling, self.height-scaling)), 0, 1, self.time/3)
                    else:
                        rectrot(self.surface, self.colors[c], pygame.Rect((tX, tY), (self.width, self.height)), 0, 1, 0)

            pygame.display.flip()
            self.time += 1

        # Done! Time to quit.
        pygame.quit()

# https://stackoverflow.com/a/66688131/938695
def rectrot( surface, color, pos, fill, border_radius, angle ):
    """
    - angle in degree
    """
    max_area = max(pos[2],pos[3])
    s = pygame.Surface((max_area,max_area))
    s = s.convert_alpha()
    s.fill((0,0,0,0))
    pygame.draw.rect(s, color,(0,0,pos[2],pos[3]),fill, border_radius=border_radius)
    s = pygame.transform.rotate(s,angle)
    surface.blit( s, (pos[0],pos[1]) )
