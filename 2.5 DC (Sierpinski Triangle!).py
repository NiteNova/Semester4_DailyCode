import pygame
from pygame.math import Vector2
from pygame.rect import Rect


# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")


# definitions:



def main():
    # game setup:
    def midpoint(p1: int, p2: int):
        return ((p1 + p2) / 2)

    def sierp(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, counter: int, isEven: int):
        counter += 1
        if counter > 8:
            return 0
        if isEven == True:
            pygame.draw.polygon(screen, (50, 0, 100), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
        else:
            pygame.draw.polygon(screen, (0, 0, 0), ( ( midpoint(x1, x2) , midpoint(y1, y2) ) , ( midpoint(x2, x3), midpoint(y2, y3) ) , ( midpoint(x3, x1), midpoint(y3, y1) )  ))
        isEven *= -1
        pygame.display.flip()
        #top
        sierp(x1, y1, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x1), midpoint(y3, y1), counter, isEven )
        #left
        sierp(x2, y2, midpoint(x1, x2) , midpoint(y1, y2),midpoint(x3, x2) ,midpoint(y3, y2), counter, isEven  )
        #right
        sierp(x3, y3, midpoint(x2, x3), midpoint(y2, y3),midpoint(x3, x1), midpoint(y3, y1), counter, isEven )


    x1 = 400
    y1 = 80

    x2 = 100
    y2 = 600

    x3 = 700
    y3 = 600

    pygame.draw.polygon(screen, (0,0, 250), ((x1, y1), (x2, y2), (x3, y3)))
    sierp(x1, y1, x2, y2, x3, y3, 0,1)


    # main loop:
    running = True
    while running:
        # input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
