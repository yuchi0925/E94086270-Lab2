#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import time


WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50


# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# initialization
pygame.init()


# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (ENEMY_WIDTH, ENEMY_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))


# set the title
pygame.display.set_caption("My first game")


#clock
clock = pygame.time.Clock()
start_time = time.time()  #取得遊戲開始秒數


class Game:
    def __init__(self):
        # window
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            clock.tick(FPS)
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        
            # draw background
            self.window.blit(background_image, (0, 0))
            
            # draw enemy and health bar
            self.window.blit(enemy_image,(50, 270))
            pygame.draw.rect(self.window, RED, [50, 260, 50, 5])
           
            # draw menu (and buttons)
            pygame.draw.rect(self.window, BLACK, [0, 0, WIN_WIDTH, 80])
            self.window.blit(pause_image, (940, 0))
            self.window.blit(continue_image, (860, 0))
            self.window.blit(sound_image, (780, 0))
            self.window.blit(muse_image, (700, 0))
                             
            #draw HP        
            for i in range(2):
                for j in range(5):
                    hp_x = 0
                    hp_y = 0
                    hp_x += hp_x + (400 + j * 40)
                    hp_y += i * 40
                    if (i * 5 + j) < self.hp:                                           
                        self.window.blit(hp_image, (hp_x, hp_y))
                    else:
                        self.window.blit(hp_gray_image, (hp_x, hp_y))
                        
            # draw time          
            current_time = time.time()  #取得遊戲現在秒數
            total_seconds = int(current_time - start_time)  #程式實際執行秒數 = 現在累積秒數 - 開始秒數
            min = str(total_seconds // 60).zfill(2)  # zfill(2) -> 不滿兩位數自動往左補0
            sec = str(total_seconds % 60).zfill(2)
            time_str = min + ":" + sec
            time_font = pygame.font.SysFont("Times New Roman", 35)  #字體變數 = pygame.font.SysFont(字體名稱, 字體尺寸)
            time_text = time_font.render(time_str, True, WHITE, BLACK) #文字變數 = 字體變數.render(文字, 平滑值, 文字顏色, 背景顏色)
            self.window.blit(time_text, (0, 565))
            
            pygame.display.update()            
        pygame.quit()
        
if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()



# In[ ]:




