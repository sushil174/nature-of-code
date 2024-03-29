import pygame
from sys import exit


pygame.init()
height, width = (400,400)
screen = pygame.display.set_mode((height,width))
clock = pygame.time.Clock()

class Vec :
    def __init__(self,x,y):
        self.pos = pygame.math.Vector2(x,y)
        self.mouse = pygame.math.Vector2()
        self.mag = pygame.math.Vector2()

    def update(self) :
        
        self.mouse = pygame.mouse.get_pos()
       
        
    def draw(self,surface) :
        pygame.draw.line(surface,'white',(0,0),self.pos,1)
        pygame.draw.line(surface,'white',(0,0),self.mouse,1)
        #self.mouse = self.pos -self.mouse
        pygame.draw.line(surface,'white',(200,200),self.mouse,1)

vec = Vec(200,200)
while True :
    screen.fill('black')
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    vec.update()
    vec.draw(screen)
    pygame.display.update()
    clock.tick(30)