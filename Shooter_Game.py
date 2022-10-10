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
        self.vel = 2

    def shoot(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def getRect(self):
        return Rect(self.x, self.y, self.size, self.size)


class make_badGuys:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5
        self.size = 15
        self.color = (250, 0, 0)
    def add_box(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

    def getRect(self):
        return Rect(self.x, self.y, self.size, self.size)


pygame.display.set_caption("Shoot Red!")
Font = pygame.font.Font('freesansbold.ttf', 20)
player_1 = Make_player(400, 600, 8, 40)

win.fill((0, 0, 0))
player_1.get_color()
Game = True
while Game:
    Kills = 0
    bullets = []
    rounds_shot = 0
    badGuys = []
    player_1.x = 400
    player_1.y = 600

    def draw_game():
        global Kills
        win.fill((0, 0, 0))
        player_1.add_box()
        for bullet in bullets:
            bullet.shoot()
        for bad_guy in badGuys:
            bad_guy.add_box()
        YourKillCount = Font.render(f'Kill Count: {Kills}', True, (255, 0, 0), (0, 0, 0))
        View1 = YourKillCount.get_rect()
        View1.center = (715, 25)
        win.blit(YourKillCount, View1)
        ShotsTaken = Font.render(f'Shots: {rounds_shot}', True, (255, 0, 0), (0, 0, 0))
        View2 = ShotsTaken.get_rect()
        View2.center = (715, 50)
        win.blit(ShotsTaken, View2)
        pygame.display.update()


    run = True
    while run:
        global kills
        pygame.time.delay(80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if player_1.x > Width - 40:
            player_1.x = Width - 40
            draw_game()
        if player_1.x < 0:
            player_1.x = 0
            draw_game()
        if player_1.y > Height - 40:
            player_1.y = Height - 40
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
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            player_1.up = True
            player_1.right = True
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            player_1.up = True
            player_1.left = True
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            player_1.down = True
            player_1.right = True
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            player_1.down = True
            player_1.left = True
        for bullet in bullets:
            if bullet.y > 0:
                if player_1.down and player_1.left:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if bullet.y > 0 and bullet.x < 800:
                            bullet.y -= bullet.vel
                            bullet.x += bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
                elif player_1.down and player_1.right:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if bullet.y > 0 and bullet.x > 0:
                            bullet.y -= bullet.vel
                            bullet.x -= bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
                elif player_1.up and player_1.left:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if player_1.y < 800 and bullet.x < 800:
                            bullet.y += bullet.vel
                            bullet.x += bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
                elif player_1.up and player_1.right:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if bullet.y < 800 and bullet.x > 0:
                            bullet.y += bullet.vel
                            bullet.x -= bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
                elif player_1.down:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if bullet.y > 0:
                            bullet.y -= bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
                elif player_1.left:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if bullet.x < 800:
                            bullet.x += bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
                elif player_1.right:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if bullet.x > 0:
                            bullet.x -= bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
                elif player_1.up:
                    shoot = True
                    while shoot:
                        for bad_guy in badGuys:
                            if pygame.Rect.colliderect(bad_guy.getRect(), bullet.getRect()):
                                bullets.pop(bullets.index(bullet))
                                badGuys.pop(badGuys.index(bad_guy))
                                Kills += 1
                                shoot = False
                        if bullet.y < 800:
                            bullet.y += bullet.vel
                            draw_game()
                        else:
                            bullets.pop(bullets.index(bullet))
                            shoot = False
        if keys[pygame.K_SPACE]:
            rounds_shot += 1
            bulletx = player_1.x
            bullety = player_1.y
            bullets.append(projectiles(bulletx + 16, bullety + 16, 6, player_1.color))

            if rounds_shot / 2 == 0:
                badGuys.append(make_badGuys(bulletx - 50, bullety - 75))
            elif rounds_shot / 1 == 1:
                badGuys.append(make_badGuys(bulletx + 50, bullety + 75))
            elif rounds_shot % 2 == 0:
                badGuys.append(make_badGuys(bulletx + 50, bullety - 75))
            elif rounds_shot % 5 == 0:
                badGuys.append(make_badGuys(bulletx - 50, bullety + 75))
        for bad_guy in badGuys:
            if pygame.Rect.colliderect(player_1.getRect(), bad_guy.getRect()):
                run = False
            if ((player_1.x - bad_guy.x) > (player_1.y - bad_guy.y)) or \
                    ((player_1.x - bad_guy.x) > (player_1.y + bad_guy.y)):
                if bad_guy.x < player_1.x - 10:
                    bad_guy.x += bad_guy.vel
                    draw_game()
            if (player_1.x + bad_guy.x) < (player_1.y + bad_guy.y) or \
                    ((player_1.x + bad_guy.x) > (player_1.y - bad_guy.y)):
                if bad_guy.x > player_1.x + 10:
                    bad_guy.x -= bad_guy.vel
                    draw_game()
            if ((player_1.x - bad_guy.x) < (player_1.y - bad_guy.y)) or \
                    ((player_1.x + bad_guy.x) < (player_1.y + bad_guy.y)):
                if bad_guy.y < player_1.y - 10:
                    bad_guy.y += bad_guy.vel
                    draw_game()
            if (player_1.x + bad_guy.x) > (player_1.y + bad_guy.y) or \
                    ((player_1.x - bad_guy.x) < (player_1.y + bad_guy.y)):
                if bad_guy.y > player_1.y + 10:
                    bad_guy.y -= bad_guy.vel
                    draw_game()
            elif (bad_guy.y - player_1.y) == (bad_guy.x - player_1.x):
                bad_guy.y -= bad_guy.vel
                bad_guy.x -= bad_guy.vel
                draw_game()
            elif (bad_guy.y - player_1.y) == (bad_guy.x + player_1.x):
                bad_guy.y -= bad_guy.vel
                bad_guy.x += bad_guy.vel
                draw_game()
            elif (bad_guy.y + player_1.y) == (bad_guy.x + player_1.x):
                bad_guy.x += bad_guy.vel
                bad_guy.y += bad_guy.vel
                draw_game()
            elif (bad_guy.y - player_1.y) == (bad_guy.x + player_1.x):
                bad_guy.x += bad_guy.vel
                bad_guy.y -= bad_guy.vel
                draw_game()

        if keys[pygame.K_q]:
            run = False
        draw_game()
    exit_screen = True
    while exit_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_screen = False
        keys = pygame.key.get_pressed()
        deathLine = Font.render('You Died!!', True, (255, 0, 0), (0, 0, 0))
        textViewD = deathLine.get_rect()
        textViewD.center = (425, 425)
        win.blit(deathLine, textViewD)
        deathLine2 = Font.render('Wanna Play again? Press enter else Press q', True, (255, 0, 0), (0, 0, 0))
        textViewD2 = deathLine2.get_rect()
        textViewD2.center = (440, 450)
        win.blit(deathLine2, textViewD2)
        pygame.display.update()
        if keys[pygame.K_RETURN]:
            exit_screen = False
        elif keys[pygame.K_q]:
            pygame.quit()
