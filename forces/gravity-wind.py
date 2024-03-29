import pygame
from sys import exit
import random
import math

def random2D() :
    angle = random.uniform(0,2.0*math.pi)
    length = 1
    pos = pygame.math.Vector2(length * math.cos(angle), length * math.sin(angle))
    return pos    

def magSq(v) :
    return (v.x*v.x + v.y*v.y)  

def limit(v,max) :
    if magSq(v) > max*max :
     v = pygame.math.Vector2.normalize(v) * max


class Mover :
    def __init__(self,x,y,m,c):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2()
        self.acc = pygame.math.Vector2()
        self.mass = m
        self.r =math.sqrt(m) * 10
        self.c = c

    def applyForce(self,force) :
        f = force/self.mass
        self.acc += f

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
mover1 = Mover(100,200,50,'red')
mover2 = Mover(200,200,2,'blue')
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

    if temp :
        wind = pygame.math.Vector2(0.1,0)
        mover1.applyForce(wind)
        mover2.applyForce(wind)

    gravity = pygame.math.Vector2(0,0.5)
    weightA = gravity * mover1.mass
    weightB = gravity * mover2.mass
    mover1.applyForce(weightA)
    mover2.applyForce(weightB)

    mover1.edges()
    mover1.update()
    mover1.show(screen)

    mover2.edges()
    mover2.update()
    mover2.show(screen)
    pygame.display.update()
    clock.tick(30)
