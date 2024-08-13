import pygame as pg
import random

# запаковка в exe
# auto-py-to-exe



randx = random.randint(0, 400)
randy = random.randint(0, 400)

if randx == 250 and randy == 250:
    randx = random.randint(0, 400)
    randy = random.randint(0, 400)


# создаем спрайты
class Cat(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/cat.png")
        self.image = pg.transform.scale(self.image, (128, 128))

        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)

        self.direction = "left"

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a] and self.rect.left > 0:
            if self.direction == "right":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "left"
            self.rect.x -= VELOCITY
        
        if keys[pg.K_d] and self.rect.right < WINDOW_WIDTH:
            if self.direction == "left":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "right"
            self.rect.x += VELOCITY
        if keys[pg.K_w] and self.rect.top > 0:
            self.rect.y -= VELOCITY
        if keys[pg.K_s] and self.rect.bottom < 500:
            self.rect.y += VELOCITY



class Mouse(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/mouse.png")
        self.image = pg.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = (randx, randy)

        self.direction = "left"

    # def update(self):
    #     keys = pg.key.get_pressed()

    #     # if keys[pg.K_a] and self.rect.left > 0:
    #     #     if self.direction == "right":
    #     #         self.image = pg.transform.flip(self.image, True, False)
    #     #         self.direction = "left"
    #     #     self.rect.x -= VELOCITY
        
        # if keys[pg.K_d] and self.rect.right < WINDOW_WIDTH:
        #     if self.direction == "left":
        #         self.image = pg.transform.flip(self.image, True, False)
        #         self.direction = "right"
        #     self.rect.x += VELOCITY
        # if keys[pg.K_w] and self.rect.top > 0:
        #     self.rect.y -= VELOCITY
        # if keys[pg.K_s] and self.rect.bottom < 500:
        #     self.rect.y += VELOCITY



background_image = pg.image.load("images/background.png")
background_image = pg.transform.scale(background_image, (500, 500))
background_rect = background_image.get_rect()
background_rect.center = (250, 250)






# Инициализируем pygame
pg.init()


icon = pg.image.load("images/mouse.png")
pg.display.set_icon(icon)


# создаем игровой дисплей
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Hungry Cat!")


FPS = 60
clock = pg.time.Clock()

# объявляем цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# звуки
sound_1 = pg.mixer.Sound("sounds/mixkit-fairy-arcade-sparkle-866.wav")
sound_1.set_volume(0.1)

# фоновая музыка
pg.mixer.music.load("sounds/cat_music.mp3")

# запуск музыки
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1, 0.0)


# скорость движения
VELOCITY = 5

# очки
score = 0

# шрифт
font = pg.font.Font("fonts/NotoSansDisplay-Regular.ttf", 26)

# создаем объекты спрайтов
cat = Cat()
mouse = Mouse()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    cat.update()
    mouse.update()

    
    # проверяем столкновения (коллизии) двух спрайтов
    if cat.rect.colliderect(mouse.rect):
        sound_1.play()
        randx = random.randint(25, 375)
        randy = random.randint(25, 375)
        mouse.rect.center = (randx, randy)
        score += 1

    # if score == 50:
    #     sound_1 = pg.mixer.Sound("sounds/mixkit-sweet-kitty-meow-93.wav")
    #     sound_1.set_volume(0.1)
    




    # заливка экрана
    screen.fill((BLACK))

    # отрисовка спрайтов
    screen.blit(background_image, background_rect)
    screen.blit(mouse.image, mouse.rect)
    screen.blit(cat.image, cat.rect)

    # отрисовка счета
    score_text = font.render(str(score), True, RED)
    screen.blit(score_text, (440, 20))


   


    pg.display.flip()
    clock.tick(FPS)

# выход из игры
pg.quit()