player1_name = input('What is your Name? ')
num_players = int(input('How many are playing: '))

import pygame
import time
from pygame.locals import *

fileref = open('TopScore.txt')
conts = fileref.read()
bsplit = conts.split(': ')
oldScore = float(bsplit[1])
pygame.init()
Height = 800
Width = 800
win = pygame.display.set_mode((Height, Width))
border = win.get_rect()


class Real_player:
    def __init__(self, x, y, vel=6, size=20, color=(244, 244, 244)):
        self.x = x
        self.y = y
        self.vel = vel
        self.size = size
        self.color = color

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


pygame.display.set_caption("Run from Red!")
Font = pygame.font.Font('freesansbold.ttf', 20)
Line1 = Font.render('Run from Red!', True, (255, 0, 0), (0, 0, 0))
textView1 = Line1.get_rect()
textView1.center = (400, 300)
Line2 = Font.render('Press Enter to cycle through color selection', True, (255, 0, 0), (0, 0, 0))
textView2 = Line2.get_rect()
textView2.center = (400, 325)
Line3 = Font.render("When you are satisfied with the color press 'p'", True, (255, 0, 0), (0, 0, 0))
textView3 = Line3.get_rect()
textView3.center = (400, 350)
Line4 = Font.render('Use arrow keys to move', True, (255, 0, 0), (0, 0, 0))
textView4 = Line4.get_rect()
textView4.center = (400, 375)
Your_speed = Font.render('Your speed will increase by 0.5 every 30 seconds', True, (255, 0, 0), (0, 0, 0))
ViewSpeed = Your_speed.get_rect()
ViewSpeed.center = (400, 400)
Bad_guy_speed = Font.render('The Bad_guy speed will increase by 1 every 30 seconds', True, (255, 0, 0), (0, 0, 0))
ViewBad_Guy_speed = Bad_guy_speed.get_rect()
ViewBad_Guy_speed.center = (400, 425)
Line5 = Font.render("press 'q' to quit while in game.", True, (255, 0, 0), (0, 0, 0))
textView5 = Line5.get_rect()
textView5.center = (400, 450)
Line6 = Font.render('Have fun!!', True, (255, 0, 0), (0, 0, 0))
textView6 = Line6.get_rect()
textView6.center = (400, 475)


def show_title():
    title_shows = True
    while title_shows:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_shows = False
        win.blit(Line1, textView1)
        win.blit(Line2, textView2)
        win.blit(Line3, textView3)
        win.blit(Line4, textView4)
        win.blit(Your_speed, ViewSpeed)
        win.blit(Bad_guy_speed, ViewBad_Guy_speed)
        win.blit(Line5, textView5)
        win.blit(Line6, textView6)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            title_shows = False


player_1 = Real_player(400, 600, 6, 20)
player_2 = Real_player(100, 100, 4, 40)
bad_guy = Real_player(-40, -40, 4, 40, (255, 0, 0))


if num_players == 1:
    win.fill((0, 0, 0))
    show_title()
    player_1.get_color()
    Game = True
    while Game:
        score = 0
        score2 = 0
        player_1.x = 400
        player_1.y = 600
        player_1.vel = 6
        bad_guy.vel = 4


        def draw_game():
            global score
            global score2
            score = float(score) + 0.05
            score2 = '{:.1f}'.format(score)
            if float(score2) % 30 == 0:
                if score != 0:
                    bad_guy.vel += 1
                    player_1.vel += 0.5
            win.fill((0, 0, 0))
            # creates black backdrop
            player_1.add_box()
            bad_guy.add_box()
            HighScore = Font.render(f'HighScore: {oldScore}', True, (255, 0, 0), (0, 0, 0))
            View1 = HighScore.get_rect()
            View1.center = (715, 25)
            YourScore = Font.render(f'YourScore: {score2}', True, (255, 0, 0), (0, 0, 0))
            View2 = YourScore.get_rect()
            View2.center = (715, 50)
            win.blit(YourScore, View2)
            win.blit(HighScore, View1)
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

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                player_1.x -= player_1.vel
            if keys[pygame.K_RIGHT]:
                player_1.x += player_1.vel
            if keys[pygame.K_UP]:
                player_1.y -= player_1.vel
            if keys[pygame.K_DOWN]:
                player_1.y += player_1.vel
            if keys[pygame.K_q]:
                run = False
            draw_game()

        newref = open('TopScore.txt', 'w')
        if score > oldScore:
            if player1_name in bsplit:
                newref.write(f'{player1_name}: {score2}')
            else:
                newref.write(f'{player1_name}: {score2}')
        elif score < oldScore:
            newref.writelines(': '.join(bsplit))

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

if num_players == 2:
    win.fill((0, 0, 0))
    show_title()
    player_1.get_color()
    player_2.get_color()
    Game = True
    while Game:
        score = 0
        score2 = 0
        player_1.x = 400
        player_1.y = 600
        player_1.vel = 6
        player_2.x = 100
        player_2.y = 100
        player_2.vel = 4


        def draw_game():
            global score
            global score2
            score = float(score) + 0.05
            score2 = '{:.1f}'.format(score)
            if float(score2) % 30 == 0:
                if score != 0:
                    player_2.vel += 1
                    player_1.vel += 0.5
            win.fill((0, 0, 0))
            # creates black backdrop
            player_1.add_box()
            player_2.add_box()
            '''HighScore = Font.render(f'HighScore: {oldScore}', True, (255, 0, 0), (0, 0, 0))
            View1 = HighScore.get_rect()
            View1.center = (715, 25)'''
            YourScore = Font.render(f'YourScore: {score2}', True, (255, 0, 0), (0, 0, 0))
            View2 = YourScore.get_rect()
            View2.center = (715, 50)
            win.blit(YourScore, View2)
            # win.blit(HighScore, View1)
            pygame.display.update()


        run = True
        while run:
            pygame.time.delay(100)
            pygame.display.update()
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
                if player_2.x > Width - 20:
                    player_2.x = Width - 20
                    draw_game()
                if player_2.x < 0:
                    player_2.x = 0
                    draw_game()
                if player_2.y > Height - 20:
                    player_2.y = Height - 20
                    draw_game()
                if player_2.y < 0:
                    player_2.y = 0
                    draw_game()
            if pygame.Rect.colliderect(player_1.getRect(), player_2.getRect()):
                run = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    player_1.x -= player_1.vel
                if keys[pygame.K_RIGHT]:
                    player_1.x += player_1.vel
                if keys[pygame.K_UP]:
                    player_1.y -= player_1.vel
                if keys[pygame.K_DOWN]:
                    player_1.y += player_1.vel
                if keys[pygame.K_q]:
                    run = False
                draw_game()

                if keys[pygame.K_a]:
                    player_2.x -= player_2.vel
                if keys[pygame.K_d]:
                    player_2.x += player_2.vel
                if keys[pygame.K_w]:
                    player_2.y -= player_2.vel
                if keys[pygame.K_s]:
                    player_2.y += player_2.vel
                draw_game()