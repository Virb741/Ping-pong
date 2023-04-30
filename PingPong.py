from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite. __init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_height - 110:
                self.rect.y += self.speed
    def update_l(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < win_height - 110:
                self.rect.y += self.speed

font.init()
font1 = font.SysFont('Arial', 60)
win1 = font1.render("Player 1 WIN!", True, (0,255,0))
win2 = font1.render("Player 2 WIN!", True, (0,255,0))

win_wight = 600
win_height = 500
window = display.set_mode((win_wight,win_height))
display.set_caption("PingPong")

racket1 = Player('racket.png', 40,180,30,110,15)
racket2 = Player('racket.png', 540,180,30,110,15)

ball = GameSprite('tenis_ball.png', 225,225,50,50,10)

mixer.init()
mixer.music.load('Gymn.mp3')
mixer.music.play()

speed_x = 4
speed_y = 4

game = True
finish = False
clock = time.Clock()
FPS = 50

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill([180,180,255])
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
        ball.reset()
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        if ball.rect.x <= 0:
            finish = True
            window.blit(win1,(130,210))
        if ball.rect.x >= win_wight - 50:
            finish = True
            window.blit(win2,(130,210))
    display.update()
    clock.tick(FPS)
