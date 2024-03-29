import pygame
from sys import exit
import random
import math

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

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

    def drag(self) :
        drag = pygame.math.Vector2.normalize(self.vel)
        drag *= -1
        c = 0.2
        speed = pygame.math.Vector2.magnitude_squared(self.vel)
        drag = pygame.math.Vector2.normalize(drag)
        drag *=( c * speed)
        self.applyForce(drag)

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


pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
mover = []
for i in range(10) :
    c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    mover.append(Mover(random.randint(0,400),-200,random.randint(3,11)))


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
        if mov.pos.y >= 200  : mov.drag()
        mov.edges()
        mov.update()
        mov.show(screen)

    r = pygame.Rect(0,200,400,200)
    draw_rect_alpha(screen,(5, 86, 133, 100),r)
    # s = pygame.Surface((400,200))  # the size of your rect
    # s.set_alpha(50)                # alpha level
    # s.fill((255,255,255))           # this fills the entire surface
    #screen.blit(s, (0,200))    # (0,0) are the top-left coordinates
    pygame.display.update()
    clock.tick(30)
