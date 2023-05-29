from pygame import *



window = display.set_mode((700, 500))
display.set_caption('ping_pong')
backround = transform.scale(image.load('background.jpg'), (700, 500))
t = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed

game = True
finish = False

racket1 = Player('racket.png',15, 20, 200, 30, 100)
racket2 = Player('racket.png',15, 630, 200, 30, 100)
ball = GameSprite('tenis_ball.png', 20, 300, 200, 50, 50)
while game:
    window.blit(backround, (0,0))
    racket1.update_r()
    racket1.reset()
    racket2.update_l()
    racket2.reset()
    ball.reset()

while game:
    window.blit(backround, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    t.tick(60)
    display.update()
