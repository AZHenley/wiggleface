# Importing the library
import pygame
import math

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
  
pygame.init()
surface = pygame.display.set_mode((800,600))
  
time = 0
# Color palette: https://lospec.com/palette-list/endesga-8
colors = [(253,253,248), (211,39,52), (218,125,34), (230,218,41), (40,198,65), (45,147,221), (123,83,173), (27,28,51)]
  
# Run until the user asks to quit
done = False
while not done:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the background with white
    surface.fill(colors[-1])

    columns = 16
    rows = 16
    xOffset = 32
    yOffset = 32
    xGap = 8
    yGap = 8
    width = 16
    height = 16
    scaling = math.sin(time/30)*3
    for j in range(columns):
        for k in range(rows):
            tX = xOffset + j * (width + xGap)
            tY = yOffset + k * (height + yGap)
            #pygame.draw.rect(surface, c, pygame.Rect((tX, tY), (width, height)))
            c = (j+k+(time//30))%8
            rectrot(surface, colors[c], pygame.Rect((tX, tY), (width-scaling, height-scaling)), 0, 1, time/3)

    pygame.display.flip()
    time += 1

# Done! Time to quit.
pygame.quit()