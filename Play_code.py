from pygame import  *
from random import *
from time import sleep

mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class MyPlayer(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        '''______________ДВИЖЕНИЕ______________'''
        if (keys_pressed[K_w] or keys_pressed[K_UP]) and self.rect.y > 150:
            if keys_pressed[K_LSHIFT]:
                self.speed = 1.5
                self.rect.y -= self.speed
            else:
                self.speed = 3
                self.rect.y -= self.speed


        if (keys_pressed[K_s] or keys_pressed[K_DOWN]) and self.rect.y < 920:
            if keys_pressed[K_LSHIFT]:
                self.speed = 1.5
                self.rect.y += self.speed
            else:
                self.speed = 3
                self.rect.y += self.speed

        if (keys_pressed[K_a] or keys_pressed[K_LEFT]) and self.rect.x > 165:
            if keys_pressed[K_LSHIFT]:
                self.speed = 1.5
                self.rect.x -= self.speed
            else:
                self.speed = 3
                self.rect.x -= self.speed

        if (keys_pressed[K_d] or keys_pressed[K_RIGHT]) and self.rect.x < 970:
            if keys_pressed[K_LSHIFT]:
                self.speed = 1.5
                self.rect.x += self.speed
            else:
                self.speed = 3
                self.rect.x += self.speed



    def game_over(self, new_image):
        self.image = transform.scale(image.load(new_image), (25, 30))
        window.blit(self.image, (self.rect.x, self.rect.y))





class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, max_x, min_x, max_y, min_y, width, height):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.max_x = max_x
        self.min_x = min_x

        self.max_y = max_y
        self.min_y = min_y

        self.direction = 'left'

    def update_x(self):
        #Отслеживание положения
        if self.rect.x <= self.min_x:
            self.direction = 'right'

        if self.rect.x >= self.max_x:
            self.direction = 'left'

        #Передвижение
        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed

    def update_y(self):
        #Отслеживание положения
        if self.rect.y <= self.min_y:
            self.direction = 'up'

        if self.rect.y >= self.max_y:
            self.direction = 'down'

        #Передвижение
        if self.direction == 'up':
            self.rect.y += self.speed

        else:
            self.rect.y -= self.speed




class Wall():
    def __init__(self, wall_image, x, y, width, height):
        self.image = transform.scale(image.load(wall_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

    #Для эффекта бага и краша
    def bag(self, new_image):
        self.image = transform.scale(image.load(new_image), (self.width + randint(5, 10), self.height + randint(5, 10)))
        window.blit(self.image, (self.rect.x + randint(2, 5), self.rect.y + randint(2, 5)))

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


def loos_win():
    run = True
    bad_window = display.set_mode((1280, 720))

    display.set_caption('Game Over')
    error = transform.scale(image.load("Images/Bad_windown.jpg"), (1280, 720))
    bad_window.blit(error, (0, 0))
    mixer.music.load('Sounds/crash_music.mp3')
    mixer.music.play()
    while run:
        for i in event.get():
            if i.type == QUIT:
                run = False

        display.update()

def window_good():
    run = True
    good_window = display.set_mode((1280, 720))
    display.set_caption('Game Win')
    good = transform.scale(image.load("Images/good_windown.jpg"), (1280, 720))
    good_window.blit(good, (0, 0))
    mixer.music.load('Sounds/win.mp3')
    mixer.music.play()
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
                global all_game
                all_game = False
        display.update()


def play_window():
    mixer.music.load('Sounds/begine_play.mp3')
    mixer.music.play()
    global window, finish
    window = display.set_mode((1050, 951))
    display.set_caption('Лабиринт')
    game = True
    finish = False
    background = transform.scale(image.load("Images/main.png"), (1050, 951))

    management = GameSprite('Images/management.png', 400, 200, 0, 239, 30 )

    walls = ['Images/Walls/backgraund.png', 'Images/Walls/backgraund1.png', 'Images/Walls/backgraund2.png', 'Images/Walls/backgraund3.png', 'Images/Walls/backgraund4.jpg']

    player = MyPlayer('Images/file.png', 200, 430, 3, 25, 30)

    wall1 = Wall(walls[randint(0,4)], 300, 250, 10, 200 )
    wall2 = Wall(walls[randint(0,4)], 300, 510, 10, 300 )

    wall3 = Wall(walls[randint(0,4)], 300, 510, 100, 10 )
    wall4 = Wall(walls[randint(0,4)], 350, 410, 10, 100 )
    wall5 = Wall(walls[randint(0,4)], 300, 310, 100, 10 )
    wall6 = Wall(walls[randint(0,4)], 300, 250, 700, 10 )
    wall7 = Wall(walls[randint(0,4)], 450, 250, 10, 500 )
    wall8 = Wall(walls[randint(0,4)], 300, 800, 690, 10 )

    wall9 = Wall(walls[randint(0,4)], 360, 570, 90, 10 )
    wall10 = Wall(walls[randint(0,4)], 300, 625, 100, 10 )
    wall11 = Wall(walls[randint(0,4)], 360, 680, 90, 10 )
    wall12 = Wall(walls[randint(0,4)], 300, 735, 100, 10 )

    wall13 = Wall(walls[randint(0,4)], 700, 300, 10, 100 )
    wall14 = Wall(walls[randint(0,4)], 705, 400, 10, 100 )
    mannequin_wall1 = Enemy('Images/bad_file.png', 700, 480, 3, 700, 699, 400, 400, 25, 30)
    mannequin_wall2 = Enemy('Images/bad_file.png', 690, 515, 3, 690, 688, 400, 400, 25, 30)
    mannequin_wall3 = Enemy('Images/bad_file.png', 695, 550, 3, 696, 695, 400, 400, 25, 30)
    wall16 = Wall(walls[randint(0,4)], 705, 600, 10, 100 )
    wall17 = Wall(walls[randint(0,4)], 700, 700, 10, 100 )
    wall18 = Wall(walls[randint(0,4)], 450, 560, 185, 10 )
    wall19 = Wall(walls[randint(0,4)], 500, 450, 150, 10 )
    wall20 = Wall(walls[randint(0,4)], 500, 350, 10, 100 )
    wall21 = Wall(walls[randint(0,4)], 560, 390, 145, 10 )
    wall22 = Wall(walls[randint(0,4)], 560, 250, 10, 90 )
    wall23 = Wall(walls[randint(0,4)], 770, 325, 10, 170 )
    wall24 = Wall(walls[randint(0,4)], 830, 300, 10, 130 )
    wall25 = Wall(walls[randint(0,4)], 770, 485, 100, 10 )
    wall26 = Wall(walls[randint(0,4)], 830, 430, 100, 10 )
    wall27 = Wall(walls[randint(0,4)], 870, 485, 10, 100 )
    wall28 = Wall(walls[randint(0,4)], 980, 250, 10, 550 )
    wall29 = Wall(walls[randint(0,4)], 780, 540, 50, 200 )
    wall30 = Wall(walls[randint(0,4)], 870, 580, 60, 10 )
    wall31 = Wall(walls[randint(0,4)], 930, 430, 10, 100 )

    wall_class = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31]


    enemy1 = Enemy('Images/bad_file2.png', 460, 650, 4, 650, 470, 0, 0,25,30 )
    enemy2 = Enemy('Images/bad_file2.png', 640, 500, 4, 660, 460, 0, 0,25,30 )
    enemy3 = Enemy('Images/bad_file2.png', 650, 300, 3, 670, 580, 0, 0,25,30 )
    enemy4 = Enemy('Images/bad_file2.png', 950, 600, 3, 0, 0, 600, 300,25,30 )
    enemy5 = Enemy('Images/bad_file2.png', 730, 610, 4, 890, 820, 710, 265,25,30 )

    mannequin1 = Enemy('Images/bad_file.png', 380, 360, 3, 380, 379, 400, 400,25,30 )
    mannequin2 = Enemy('Images/bad_file.png', 640, 610, 3, 640, 639, 400, 400,25,30 )
    mannequin3 = Enemy('Images/bad_file.png', 520, 600, 3, 520, 519, 400, 400,25,30 )
    mannequin4 = Enemy('Images/bad_file.png', 480, 700, 3, 482, 480, 400, 400,25,30)
    mannequin5 = Enemy('Images/bad_file.png', 620, 700, 3, 620, 619, 400, 400,25,30 )
    mannequin6 = Enemy('Images/bad_file.png', 505, 305, 3, 505, 504, 450, 400,25,30 )
    mannequin7 = Enemy('Images/bad_file.png', 900, 295, 3, 900, 899, 400, 400,25,30 )
    mannequin8 = Enemy('Images/bad_file.png', 875, 350, 3, 875, 874, 400, 400,25,30)
    imag_antivirys = choice(['Images/Antivirus/antivirys_avast.png', 'Images/Antivirus/antivirys_360.png', ])
    antivirys = GameSprite(imag_antivirys,900, 700, 1, 35, 35)
    lose_sprite = [enemy1, enemy2, enemy3, enemy4, enemy5, mannequin1, mannequin2, mannequin3, mannequin4, mannequin5, mannequin6, mannequin7, mannequin8]
    while game:
        for i in event.get():
            if i.type == QUIT:
                mixer.music.load('Sounds/end_game.mp3')
                mixer.music.play()
                sleep(1.35)
                global all_game
                all_game = False
                game = False

            #просмотр управления
            if i.type == MOUSEBUTTONDOWN and i.button == 1:
                pos = mouse.get_pos()
                if management.rect.collidepoint(pos):

                    mixer.music.load('Sounds/open_management.mp3')
                    mixer.music.play()
                    global management_open
                    management_open = True








        if not finish:
            window.fill((0, 0, 0))
            window.blit(background, (0, 0))
            management.reset()



            wall1.draw()
            wall2.draw()
            wall3.draw()
            wall4.draw()
            wall5.draw()
            wall6.draw()
            wall7.draw()
            wall8.draw()

            wall9.draw()
            wall10.draw()
            wall11.draw()
            wall12.draw()

            wall13.draw()
            wall14.draw()
            mannequin_wall1.update_x()
            mannequin_wall1.reset()
            mannequin_wall2.update_x()
            mannequin_wall2.reset()
            mannequin_wall3.update_x()
            mannequin_wall3.reset()

            wall16.draw()
            wall17.draw()
            wall18.draw()
            wall19.draw()
            wall20.draw()
            wall21.draw()
            wall22.draw()
            wall23.draw()
            wall24.draw()
            wall25.draw()
            wall26.draw()
            wall27.draw()
            wall28.draw()
            wall29.draw()
            wall30.draw()
            wall31.draw()
            mannequin1.update_x()
            mannequin2.update_x()
            mannequin3.update_x()
            mannequin4.update_x()
            mannequin5.update_x()
            mannequin6.update_x()
            mannequin7.update_x()
            mannequin8.update_x()

            mannequin1.reset()
            mannequin2.reset()
            mannequin3.reset()
            mannequin4.reset()
            mannequin5.reset()
            mannequin6.reset()
            mannequin7.reset()
            mannequin8.reset()

            enemy1.update_x()
            enemy1.reset()

            enemy2.update_x()
            enemy2.reset()

            enemy3.update_x()
            enemy3.reset()

            enemy4.update_y()
            enemy4.reset()

            enemy5.update_y()
            enemy5.reset()

            bag_wall = wall_class[randint(0, len(wall_class) - 1)]
            bag_wall.bag(walls[randint(0, 4)])

            player.update()

            antivirys.reset()
            player.reset()

            for i in wall_class:
                if sprite.collide_rect(player, i):
                    mixer.music.load('Sounds/crash.mp3')
                    mixer.music.play()

                    finish = True
                    game = False
                    player.game_over('Images/bad_file.png')
                    display.update()
                    sleep(1)
                    management_open = False



            for w in lose_sprite:
                if sprite.collide_rect(player, w):
                    mixer.music.load('Sounds/crash.mp3')
                    mixer.music.play()
                    finish = True
                    game = False
                    player.game_over('Images/bad_file.png')
                    display.update()
                    sleep(1)

                    management_open = False
                    # Анимация

            if sprite.collide_rect(player, antivirys):
                mixer.music.load('Sounds/open_antivirus.mp3')
                mixer.music.play()
                window.fill((0, 0, 0))
                window.blit(background, (0, 0))
                #первый ряд
                good_file1 = GameSprite('Images/file.png', 200, 200, 0, 25, 30)
                good_file2 = GameSprite('Images/file.png', 250, 200, 0, 25, 30)
                good_file3 = GameSprite('Images/file.png', 300, 200, 0, 25, 30)
                good_file4 = GameSprite('Images/file.png', 350, 200, 0, 25, 30)
                good_file5 = GameSprite('Images/file.png', 400, 200, 0, 25, 30)

                #второй ряд
                good_file6 = GameSprite('Images/file.png', 200, 250, 0, 25, 30)
                good_file7 = GameSprite('Images/file.png', 250, 250, 0, 25, 30)
                good_file8 = GameSprite('Images/file.png', 200, 250, 0, 25, 30)
                good_file9 = GameSprite('Images/file.png', 250, 250, 0, 25, 30)
                good_file10 = GameSprite('Images/file.png', 200, 250, 0, 25, 30)
                good_file11 = GameSprite('Images/file.png', 250, 250, 0, 25, 30)
                good_file12 = GameSprite('Images/file.png', 200, 250, 0, 25, 30)
                good_file13 = GameSprite('Images/file.png', 250, 250, 0, 25, 30)


                good_file1.reset()
                good_file2.reset()
                good_file3.reset()
                good_file4.reset()
                good_file5.reset()
                good_file6.reset()
                good_file7.reset()
                good_file8.reset()
                good_file9.reset()
                good_file10.reset()
                good_file11.reset()
                good_file12.reset()
                good_file13.reset()

                display.update()
                sleep(1)
                window_good()
                finish = True
                game = False
                all_game = False

            if management_open:
                #окно с управлением
                texture_management = transform.scale(image.load('Images/control.png'), (475, 419))
                window.blit(texture_management, (300, 250))

                #кнопка закрыть
                texture_close = transform.scale(image.load('Images/close.png'), (45, 29))
                window.blit(texture_close, (730, 250))
                close = Rect(730, 250, 45, 29)
                draw.rect(window, (255, 255, 255), close)
                window.blit(texture_close, (730, 250))



                for i in event.get():
                    if i.type == MOUSEBUTTONDOWN and i.button == 1:
                        pos = mouse.get_pos()
                        if close.collidepoint(pos):
                            management_open = False
                            print('lflff')

                    if i.type == QUIT:
                        mixer.music.load('Sounds/end_game.mp3')
                        mixer.music.play()
                        sleep(1.35)

                        all_game = False
                        game = False

        clock.tick(120)
        display.update()
    return True

all_game = True

management_open = False
clock = time.Clock()

while all_game:
    if all_game:
        if play_window() and all_game:
            loos_win()
        else:
            if all_game:
                play_window()







