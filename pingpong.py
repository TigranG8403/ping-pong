#GitHib repository:
#https://github.com/TigranG8403/ping-pong/

#En
#The .exe file is located in the "main" folder.
#License: "Creative Commons"
#Read the "README.rd" file in the GitHub repository.

#---Ru/En

#Ru
#.exe файл находится в папке "main".
#Лицензия: "Creative Commons"
#Прочитайте файл "README.rd" в репозитории GitHub.


#-----------------
#Импортируем PyGame
from pygame import *

#Текст
#Text
font.init() #"Конструктор" текста #The "constructor" of the text
font = font.Font(None, 35)
lose1 = font.render('Игрок 1 проиграл!', True, (180, 0, 0)) #Текст "Игрок 1 проиграл!" #Text "Игрок 1 проиграл!"
lose2 = font.render('Игрок 2 проиграл', True, (180, 0, 0)) #Текст "Игрок 2 проиграл!" #Text "Игрок 2 проиграл!"

#Создаем супер-класс GameSprite для создания персонажей
#Creating a super GameSprite class to create characters
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    #Отображение созданных нами объектов
    #Display of objects created by us
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) #Отображение объектов в окне #Displaying objects in the window

#Создаем дочерний класс супер-класса GameSprite для управления персонажем
#Creating a child class of the GameSprite super class to control the character
class Player(GameSprite):
    #Управление по нажатию на кнопки
    #Control by pressing the buttons
    def update_r(self):
        keys = key.get_pressed()
        #Условия
        #Conditions
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_h - 150:
            self.rect.y += self.speed

    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_h - 150:
            self.rect.y += self.speed

#Создание окна и фон
#Create window and background
background = (200, 255, 255) #Размеры фона #Background Dimensions
window_w = 600 #Размеры окна, ширина #Window dimensions, width
window_h = 500 #Размеры окна, высота #Window dimensions, height
window = display.set_mode((window_w, window_h)) #Размеры окна #Window dimensions
window.fill(background) #Фон #Background

#FPS и значения (переменные) счетчиков
#FPS and counter values (variables)
game = True #Статус игры (При game = False игра закроется) #Game status (If game = False, the game will close)
FPS = 60 #FPS
win = False #Статус победы (При win = True выведет надпись "ПОБЕДА!") #Victory status (If win = True, it will display the inscription "VICTORY!")
clock = time.Clock()

#Создание персонажей #Creating characters
racket1 = Player('racket.png', 30, 200, 4, 50, 150) #racket1
racket2 = Player('racket.png', 520, 200, 4, 50, 150) #racket2
ball = GameSprite('ball.png', 200, 200, 4, 50, 50) #ball

ball_direction_x = 3 #мяч_направление_x #ball_direction_x
ball_direction_y = 3 #мяч_направление_y #ball_direction_y

#Игровой цикл
#Game cycle
while game:
    #Выход из игры при закрытии окна
    #Exit the game when the window is closed
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
            if e.key == K_r:
                win = False
                ball.rect.x = 200
                ball.rect.y = 200
                ball_direction_x = 3
                ball_direction_y = 3

    if not win:
        window.fill(background)
        racket1.update1()
        racket2.update_r()
        ball.rect.x += ball_direction_x
        ball.rect.y += ball_direction_y

        #Столкновения спрайтов #Sprite collisions
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_direction_x *= -1

        #Условия победы и (или) проигрыша
        #Winning and (or) losing conditions
        if ball.rect.y > window_h - 50 or ball.rect.y < 0:
            ball_direction_y *= -1

        if ball.rect.x < 0:
            win = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > window_w:
            win = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    #Отображение интерфейса ПО
    #Software interface display
    display.update()
    clock.tick(FPS)
#-----------------


#GitHib repository:
#https://github.com/TigranG8403/ping-pong/

#En
#The .exe file is located in the "main" folder.
#License: "Creative Commons"
#Read the "README.rd" file in the GitHub repository.

#---Ru/En

#Ru
#.exe файл находится в папке "main".
#Лицензия: "Creative Commons"
#Прочитайте файл "README.rd" в репозитории GitHub.
