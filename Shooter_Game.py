import pygame
from pygame.locals import *

pygame.init()
Font = pygame.font.Font('freesansbold.ttf', 20)
Height = 800
Width = 800
win = pygame.display.set_mode((Height, Width))
border = win.get_rect()


class Make_player:
    def __init__(self, x, y, vel=6, size=20, color=(244, 244, 244)):
        self.x = x
        self.y = y
        self.vel = vel
        self.size = size
        self.color = color
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def get_color(self):
        color_selection = dict()
        color_selection['Blue'] = (0, 255, 255)
        color_selection['Green'] = (102, 205, 0)
        color_selection['Gold'] = (255, 215, 0)
        color_selection['Purple'] = (178, 58, 238)
        color_selection['Pink'] = (255, 20, 147)
        color_selection['White'] = (244, 244, 244)
        picking_color = True
        while picking_color:
            for i in color_selection:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        picking_color = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RETURN]:
                        self.color = color_selection[i]
                        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))
                        pygame.display.update()
                    elif keys[pygame.K_p]:
                        picking_color = False

    def add_box(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def getRect(self):
        return Rect(self.x, self.y, self.size, self.size)


class projectiles:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vel = 20

    def shoot(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))


pygame.display.set_caption("Shoot Red!")
player_1 = Make_player(400, 600, 8, 40)

win.fill((0, 0, 0))
player_1.get_color()
Game = True
while Game:
    Kills = 0
    bullets = []
    player_1.x = 400
    player_1.y = 600

    def draw_game():
        global Kills
        win.fill((0, 0, 0))
        player_1.add_box()
        for bullet in bullets:
            bullet.shoot()
        YourKillCount = Font.render(f'KilCount: {Kills}', True, (255, 0, 0), (0, 0, 0))
        View1 = YourKillCount.get_rect()
        View1.center = (715, 25)
        win.blit(YourKillCount, View1)
        pygame.display.update()


    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if player_1.x > Width - 20:
            player_1.x = Width - 20
            draw_game()
        if player_1.x < 0:
            player_1.x = 0
            draw_game()
        if player_1.y > Height - 20:
            player_1.y = Height - 20
            draw_game()
        if player_1.y < 0:
            player_1.y = 0
            draw_game()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_1.x -= player_1.vel
            player_1.left = True
            player_1.right = False
            player_1.down = False
            player_1.up = False
        if keys[pygame.K_RIGHT]:
            player_1.x += player_1.vel
            player_1.right = True
            player_1.left = False
            player_1.down = False
            player_1.up = False
        if keys[pygame.K_UP]:
            player_1.y -= player_1.vel
            player_1.up = True
            player_1.down = False
            player_1.right = False
            player_1.left = False
        if keys[pygame.K_DOWN]:
            player_1.y += player_1.vel
            player_1.down = True
            player_1.up = False
            player_1.right = False
            player_1.left = False
        for bullet in bullets:
            if bullet.x < 800 and bullet.y < 800:
                if player_1.right:
                    bullet.x += bullet.vel
                if player_1.up:
                    bullet.x += bullet.vel
                '''if bullet.y < 800 and player_1.up:
                    bullet.y += bullet.vel'''
                '''if bullet.y > 0 and player_1.down:
                    bullet.y -= bullet.vel'''
            else:
                bullets.pop(bullets.index(bullet))

        if keys[pygame.K_SPACE]:
            bulletx = player_1.x
            bullety = player_1.y
            if len(bullets) < 5:
                bullets.append(projectiles(bulletx, bullety, 6, player_1.color))







        if keys[pygame.K_q]:
            run = False
        draw_game()
    Game = False