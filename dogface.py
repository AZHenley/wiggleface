# Importing the library
import pygame
  
pygame.init()
surface = pygame.display.set_mode((800,600))
  
# Initialing Color
color = (255,0,0)
  
# Run until the user asks to quit
done = False
while not done:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the background with white
    surface.fill((255, 255, 255))

    columns = 16
    rows = 16
    xOffset = 32
    yOffset = 32
    xGap = 8
    yGap = 8
    width = 16
    height = 16
    for j in range(columns):
        for k in range(rows):
            tX = xOffset + j * (width + xGap)
            tY = yOffset + k * (height + yGap)
            c = (255, 0, 0)
            pygame.draw.rect(surface, c, pygame.Rect((tX, tY), (width, height)))

    pygame.display.flip()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()