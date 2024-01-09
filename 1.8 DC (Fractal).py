import pygame
import random
import math
screen = pygame.display.set_mode((1000, 800))

def drawSnow(lev, x1, y1, x5, y5):
    if lev == 0:
        if lev < 10:
            pygame.draw.line(screen, (random.randrange(5, 200), random.randrange(5, 200), random.randrange(5, 200)), (x1, y1), (x5, y5), 1)
        else:
            pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x5, y5), 1)

        pygame.display.flip()
    else:
        #calculate delta between points
        deltaX = x5 - x1
        deltaY = y5 - y1
        #find x2 (cut distance to a third)
        x2 = x1+ deltaX/3
        y2 = y1+ deltaY/3
        
        #find x4 (the other point 2/3rds across the line)
        x4 = x1 +2*deltaX/3
        y4 = y1 +2*deltaY/3
        
        #calculate x3 (the point that sticks out)
        x3 = (x2+ x4 + math.sqrt(3) * (y2- y4))/2
        y3 = (y2+ y4 + math.sqrt(3) * (x4- x2))/2
       
       
        #recursively call itself
        drawSnow(lev-1, x1, y1, x2, y2)
        drawSnow(lev-1, x2, y2, x3, y3)
        drawSnow(lev-1, x3, y3, x4, y4)
        drawSnow(lev-1, x4, y4, x5, y5)

level = 0
while True:
    level += 1
    drawSnow(level, 1000, 800, 450, 0)
    pygame.display.flip()
