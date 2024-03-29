import pygame
from sys import exit
import random
import math
G = 1.0

def constrain(n,low,high) :
    return max(min(n,high),low)

class Attractor :
    def __init__(self,x,y,m) :
        self.pos = pygame.math.Vector2(x,y)
        self.mass = m
        self.r = math.sqrt(m) * 10

    def attract(self,mover) :
        force = self.pos - mover.pos
        distance = constrain(pygame.math.Vector2.magnitude(force),5,25)
        strength = G * (self.mass * mover.mass) / (distance * distance)
        force = pygame.math.Vector2.normalize(force)
        force = force * strength
        mover.applyForce(force)

    def show(self,surface) :
        pygame.draw.circle(surface,'white',self.pos,self.mass * 2)

class Mover :
    def __init__(self,x,y,m):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2()
        self.acc = pygame.math.Vector2()
        self.mass = m
        self.r =math.sqrt(m) * 10

    def applyForce(self,force) :
        f = force/self.mass
        self.acc += f
        
    def update(self):
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel 
        self.acc *= 0

    
    def show(self,surface):
        
        pygame.draw.circle(surface,'white',self.pos,self.mass * 2,1)



screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
mover = []
for i in range(10) :
    mover.append(Mover(random.randint(50,350),random.randint(50,350),random.randint(3,15)))
# mover = Mover(50,50,5)
attractor = Attractor(200,200,5)
while True :
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    for mov in mover :
        
        mov.update()
        attractor.attract(mov)
        mov.show(screen)
    attractor.show(screen)
    pygame.display.update()
    clock.tick(30)
