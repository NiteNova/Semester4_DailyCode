# plant factory code: The Plant Factory code is a demonstration of the Factory design pattern in Python
# In this pattern, a central 'Factory' (the Plant Factory in our code)
# takes care of creating objects (plants, like shamrocks) without needing to specify the exact class of the object.
# It simplifies the object creation process, allowing the program to easily create and manage different types of plants,
# showcasing how the Factory design pattern provides a streamlined and flexible approach to object creation in programming.
# disclaimer: I used ChatGPT to help write parts of this code :)

import pygame
import random
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plant Factory")


# Plant base class---------------------------------------------------------------------------
class Plant:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y

    def draw(self, screen):
        raise NotImplementedError("You must implement the draw method.")

# Concrete Plant class - Shamrock-------------------------------------------------------------
class Shamrock(Plant):
    def draw(self, screen):
        #black outlines
        pygame.draw.circle(screen, (0,0,0), (self.xpos-20, self.ypos+20), 22,2) #leaves
        pygame.draw.circle(screen, (0,0,0), (self.xpos, self.ypos-10), 22,5)
        pygame.draw.circle(screen, (0,0,0), (self.xpos+20, self.ypos+20), 22,2)
        pygame.draw.rect(screen, (0,0,0), (self.xpos-10, self.ypos+20, 15, 50),2)#stem
        #green interiors
        pygame.draw.rect(screen, (0,150,85), (self.xpos-10, self.ypos+20, 15, 50))#stem
        pygame.draw.circle(screen, (0,151,0), (self.xpos-20, self.ypos+20), 20) #leaves
        pygame.draw.circle(screen, (85,150,0), (self.xpos, self.ypos-10), 20)
        pygame.draw.circle(screen, (85,150,85), (self.xpos+20, self.ypos+20), 20)

class Iris(Plant):
    def draw(self, screen):
        #black outlines
        pygame.draw.circle(screen, (0,0,0), (self.xpos-20, self.ypos+20), 22,2) #leaves
        pygame.draw.circle(screen, (0,0,0), (self.xpos, self.ypos-10), 22,5)
        pygame.draw.circle(screen, (0,0,0), (self.xpos+20, self.ypos+20), 22,2)
        pygame.draw.rect(screen, (0,0,0), (self.xpos-10, self.ypos+20, 15, 50),2)#stem
        #green interiors
        pygame.draw.rect(screen, (0,150,85), (self.xpos-10, self.ypos+20, 15, 50))#stem
        pygame.draw.circle(screen, (255,181,226), (self.xpos-20, self.ypos+20), 20) #leaves
        pygame.draw.circle(screen, (206,112,232), (self.xpos, self.ypos-10), 20)
        pygame.draw.circle(screen, 	(163,71,229), (self.xpos+20, self.ypos+20), 20)

class DarkAngel(Plant):
    def draw(self, screen):
        #black outlines
        pygame.draw.circle(screen, (0,0,0), (self.xpos-20, self.ypos+20), 22,2) #leaves
        pygame.draw.circle(screen, (0,0,0), (self.xpos, self.ypos-10), 22,5)
        pygame.draw.circle(screen, (0,0,0), (self.xpos+20, self.ypos+20), 22,2)
        pygame.draw.rect(screen, (0,0,0), (self.xpos-10, self.ypos+20, 15, 50),2)#stem
        #green interiors
        pygame.draw.rect(screen, (0,150,85), (self.xpos-10, self.ypos+20, 15, 50))#stem
        pygame.draw.circle(screen, (0,0,0), (self.xpos-20, self.ypos+20), 20) #leaves
        pygame.draw.circle(screen, (136, 8, 8), (self.xpos, self.ypos-5), 20)
        pygame.draw.circle(screen, 	(0,0,0), (self.xpos+20, self.ypos+20), 20)



# add more plant classes here...

# Factory class---------------------------------------------------------------------------------
class PlantFactory:
    def create_plant(self, plant_type, x, y):
        if plant_type == "shamrock":
            return Shamrock(x, y)
        if plant_type == "Iris":
            return Iris(x, y)
        if plant_type == "DarkAngel":
            return DarkAngel(x, y)
        # Add more plant type conditions here...
        else:
            raise ValueError("Unknown plant type")

# Game setup
plant_factory = PlantFactory()
plants = []

# GAME LOOP----------------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # create a new shamrock at random positions
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(50, SCREEN_HEIGHT - 50)
    plants.append(plant_factory.create_plant("shamrock", x, y))
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(50, SCREEN_HEIGHT - 50)
    plants.append(plant_factory.create_plant("Iris", x, y))
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(50, SCREEN_HEIGHT - 50)
    plants.append(plant_factory.create_plant("DarkAngel", x, y))

    # render section------------------------
    screen.fill((0,0,0))  # Clear screen
    for plant in plants:
        plant.draw(screen)

    pygame.display.flip()
#end game loop-------------------------------------------------------------------------------------------
pygame.quit()
