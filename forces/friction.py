import pygame
from sys import exit
import random
import math

class Mover :
    def __init__(self,x,y,m):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2()
        self.acc = pygame.math.Vector2()
        self.mass = m
        self.r =math.sqrt(m) * 10
        self.c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def applyForce(self,force) :
        f = force/self.mass
        self.acc += f

    def friction(self) :
        diff = 400 - (self.pos.y + self.r)
        if diff < 1 :
            force = pygame.math.Vector2.normalize(self.vel)
            force *= -1
            m = 0.1
            normal = self.mass
            force = pygame.math.Vector2.normalize(force)
            force *=( m * normal)
            self.applyForce(force)

    def edges(self) :
        if self.pos.x >= 400-self.r:
            self.pos.x = 400-self.r
            self.vel.x *= -1

        if self.pos.x <= self.r :
            self.pos.x = self.r
            self.vel.x *= -1

        if self.pos.y >= 400-self.r :
            self.pos.y = 400-self.r
            self.vel.y *= -1

        if self.pos.y <= self.r:
            self.pos.y = self.r
            self.vel.y *= -1
        
    def update(self):
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel 
        self.acc *= 0

    
    def show(self,surface):
        
        pygame.draw.circle(surface,self.c,self.pos,self.r)



screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
mover = []
for i in range(10) :
    c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    mover.append(Mover(random.randint(0,400),200,random.randint(1,8)))


temp = False
while True :
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w :
                temp = True
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w :
                temp = False

    for mov in mover :
        if temp :
            wind = pygame.math.Vector2(0.1,0)
            mov.applyForce(wind)
        
        gravity = pygame.math.Vector2(0,0.5)
        weightA = gravity * mov.mass
    
        mov.applyForce(weightA)
    
        mov.friction()
        mov.edges()
        mov.update()
        mov.show(screen)

    pygame.display.update()
    clock.tick(30)
