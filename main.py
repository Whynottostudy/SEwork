import pygame
import random
from game_screen_utils import  game_screen
from status_bar import status_bar
from show_screen_utils import show_screen

# 初始化 Pygame
pygame.init()

# 定义常量
TILE_SIZE = 120
ROWS, COLS = 6, 6
STATUS_BAR_HEIGHT = 100
GAP_LAYERS = 16
GAP_HEIGHT = 30
GAP_LEFT = 150
GAP_TOP = 30    
GAP_BETWEEN = TILE_SIZE + 3 * GAP_LAYERS + 10
GAP_VERTICAL = TILE_SIZE + 7
HEIGHT =  GAP_TOP + ROWS * GAP_VERTICAL
WINDOW_WIDTH = GAP_LEFT * 2 + GAP_BETWEEN * COLS
WINDOW_HEIGHT = HEIGHT + STATUS_BAR_HEIGHT + GAP_HEIGHT
FPS = 80
COUNTDOWN_TIME = 150

# 创建窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("旅了个游")

game_screen = game_screen(ROWS, COLS, TILE_SIZE, GAP_LEFT, GAP_TOP, GAP_BETWEEN) #游戏画面
status_bar = status_bar(ROWS, WINDOW_WIDTH, HEIGHT, TILE_SIZE, GAP_HEIGHT, STATUS_BAR_HEIGHT) #状态栏
show_screen = show_screen(WINDOW_WIDTH, WINDOW_HEIGHT, COUNTDOWN_TIME, game_screen, status_bar) #主界面 游戏结束界面

# 主游戏循环
running = True
game_state = 'main_menu'
clock = pygame.time.Clock()
pygame.key.stop_text_input()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == 'main_menu':
                x, y = event.pos
                game_state = show_screen.click_start(x, y)
            elif game_state == 'game_over' or game_state == 'win':
                game_state = 'main_menu'
                show_screen.reset_game()
            elif game_state == 'playing':
                x, y = event.pos
                show_screen.choose_pic(x, y)
                game_state = show_screen.click_back(game_state, x, y)
            elif game_state == 'choose_level':
                x, y = event.pos
                game_state = show_screen.choose_level(x, y)
                game_state = show_screen.click_back(game_state, x, y)  
        elif event.type == pygame.MOUSEMOTION:
            if game_state == "playing":
                x, y = event.pos
                show_screen.get_choose_hover_box(x, y)
                show_screen.get_back_hover_box(x, y)
            elif game_state == "choose_level":
                x, y = event.pos
                show_screen.get_level_hover_box( x, y)
                show_screen.get_back_hover_box(x, y)
            elif game_state == "main_menu":
                x, y = event.pos
                show_screen.get_start_box(x, y)
        elif event.type == pygame.KEYDOWN:
            if game_state == 'playing' :
                if event.key == pygame.K_p:
                    game_state = 'win'
                    show_screen.reset_game()
                elif event.key == pygame.K_c:
                    status_bar.clicked_images.clear()

    if game_state == "main_menu":
        show_screen.show_main_menu(screen)
    elif game_state == "choose_level":
        show_screen.show_choose_level(screen)
    elif game_state == "playing":
        game_state = show_screen.show_game_screen(screen)
        pygame.display.flip()
    elif game_state == "game_over":
        show_screen.show_game_over(screen)
    elif game_state == "win":
        show_screen.show_win_screen(screen)

pygame.quit()