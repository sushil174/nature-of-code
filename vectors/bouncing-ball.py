import pygame
from sys import exit


pygame.init()
height, width = (400,400)
screen = pygame.display.set_mode((height,width))
clock = pygame.time.Clock()

class Ball :
    def __init__(self,x,y):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2(2,2.5)


    def update(self) :
        self.pos += self.vel
        if self.pos.x > width or self.pos.x < 0 :
            self.vel.x *= -1

        if self.pos.y > height or self.pos.y < 0 :
            self.vel.y *= -1

    def draw(self,surface) :
        pygame.draw.circle(surface,'white',self.pos,20,1)


ball = Ball(200,200)
while True :
    screen.fill('black')
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    ball.update()
    ball.draw(screen)
    pygame.display.update()
    clock.tick(30)