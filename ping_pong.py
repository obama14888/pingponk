from pygame import *
clock = time.Clock()
fps = 60
x = 150
y = 200
speed = 10
speed_x = 3
speed_y = 3 
window = display.set_mode((700,500))
display.set_caption('лабиринт')
background = transform.scale(image.load('background.jpg'),(700,500))
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 595:
            self.rect.y += self.speed
        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 640 - 55:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
racket = Player('racket.png',0,150,5)
ball = Ball('ball.png',100,100,5)
racket2 = Player2('racket.png',650,200,5)
game = True

font.init()
font = font.Font(None,35)
lose1 = font.render('1 игрок проиграл',True,(180,0,0))
lose2 = font.render('2 игрок проиграл',True,(180,0,0))
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 600-50 or ball.rect.y < 0:
        speed *= -1
    if sprite.collide_rect(racket,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1
    if ball.rect.y > 500-50 or ball.rect.y <0:
        speed_y *= -1
    if ball.rect.x > 700-50 or ball.rect.x <0:
        speed_x *= -1
    if ball.rect.x > 700-50:
        print(lose1)
        break 
    if ball.rect.x <0:
        print(lose2)
        break
    ball.reset()
    racket.reset()
    racket.update()
    racket2.reset()
    racket2.update()





    clock.tick(fps)
    display.update()