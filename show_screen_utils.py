import pygame

class show_screen:
    def __init__(self,WINDOW_WIDTH, WINDOW_HEIGHT, COUNTDOWN_TIME, game_screen, status_bar):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.COUNTDOWN_TIME = COUNTDOWN_TIME
        self.game_screen = game_screen
        self.status_bar = status_bar
        self.WHITE = (255, 255, 255)
        self.level_box = None
        self.start_box = None
        self.back_box = None
        self.level_rect = [None, None, None]
        self.back_rect = None
        self.start_rect = None
        self.start_ticks = 0
        self.countdown = 0
        self.background = pygame.image.load("patterns/background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

    def show_main_menu(self, screen):
        color = (51, 255, 255)
        screen.blit(self.background, (0, 0))
        font_file = pygame.font.match_font('方正粗黑宋简体')
        font = pygame.font.Font(font_file, 92)
        text = font.render("旅了个游", True, color)
        screen.blit(text, (5 * self.WINDOW_WIDTH // 6 - text.get_width() // 2, self.WINDOW_HEIGHT // 6 - text.get_height() // 2 - 50))
        font = pygame.font.Font(font_file, 46)
        text = font.render("开始游戏", True, color)
        self.start_rect = pygame.Rect(self.WINDOW_WIDTH // 3 - text.get_width() // 2, 3 * self.WINDOW_HEIGHT // 4 - text.get_height() // 2 + 50, text.get_width(), text.get_height())
        surface = pygame.Surface((self.start_rect.width, self.start_rect.height))
        surface.set_alpha(128)
        surface.fill((255, 153, 51))
        pygame.draw.rect(screen, (255, 153, 51), self.start_rect, 2)
        screen.blit(surface, (self.start_rect.x, self.start_rect.y))
        screen.blit(text, (self.WINDOW_WIDTH // 3 - text.get_width() // 2, 3 * self.WINDOW_HEIGHT // 4 - text.get_height() // 2 + 50))
        if self.start_box is not None:
            pygame.draw.rect(screen, (204, 102, 0), self.start_box, 3)
        pygame.display.flip()

    def show_choose_level(self, screen):
        color = (51, 255, 255)
        screen.blit(self.background, (0, 0))
        font = pygame.font.SysFont(None, 96)
        levels = ["Hu Bei Province(easy)", "Hu Nan Province(normal)", "Fu Jian Province(hard)"]
        for i, level in enumerate(levels):
            text = font.render(level, True, color)
            rect = pygame.Rect(self.WINDOW_WIDTH // 2 - text.get_width() // 2, 200 + i * 200, text.get_width(), text.get_height())
            surface = pygame.Surface((rect.width, rect.height))
            surface.set_alpha(128)
            surface.fill((255, 153, 51))
            self.level_rect[i] = rect
            pygame.draw.rect(screen, (255, 153, 51), rect, 3)
            screen.blit(surface, (rect.x, rect.y))
            screen.blit(text, (self.WINDOW_WIDTH // 2 - text.get_width() // 2, 200 + i * 200))
        if self.level_box is not None:
            pygame.draw.rect(screen, (204, 102, 0), self.level_box, 3)
        self.show_back_button(screen)
        pygame.display.flip()
    
    def show_game_screen(self, screen):
        game_state = 'playing'
        screen.blit(self.background, (0, 0))
        self.game_screen.draw_board(screen)
        self.game_screen.draw_hover_box(screen)
        self.status_bar.draw_status_bar(screen)
        self.draw_countdown(screen, self.countdown)
        if (not self.status_bar.check_status()) or self.countdown == 0:
            game_state = "game_over"
        elif self.game_screen.check_game_screen():
            game_state = "win"
        self.show_back_button(screen)
        return game_state
    
    def show_win_screen(self, screen):
        color = (255, 0, 0)
        screen.blit(self.background, (0, 0))
        font_file = pygame.font.match_font('方正粗黑宋简体')
        font = pygame.font.Font(font_file, 102)
        text = font.render("恭喜你赢了!!!:)", True, color)
        screen.blit(text, (7 * self.WINDOW_WIDTH // 10 - text.get_width() // 2, self.WINDOW_HEIGHT // 6 - text.get_height() // 2 - 50))
        font = pygame.font.Font(font_file, 76)
        text = font.render("点击任意键重新开始", True, color)
        screen.blit(text, (7 * self.WINDOW_WIDTH // 10 - text.get_width() // 2, self.WINDOW_HEIGHT // 6 - text.get_height() // 2 + 50))
        pygame.display.flip()

    def show_game_over(self, screen):
        color = (204, 229, 255)
        screen.blit(self.background, (0, 0))
        font_file = pygame.font.match_font('方正粗黑宋简体')
        font = pygame.font.Font(font_file, 102)
        text = font.render("游戏失败TT", True, color)
        screen.blit(text, (7 * self.WINDOW_WIDTH // 10 - text.get_width() // 2, self.WINDOW_HEIGHT // 6 - text.get_height() // 2 - 50))
        font = pygame.font.Font(font_file, 76)
        text = font.render("点击任意键重新开始", True, color)
        screen.blit(text, (7 * self.WINDOW_WIDTH // 10 - text.get_width() // 2, self.WINDOW_HEIGHT // 6 - text.get_height() // 2 + 50))
        pygame.display.flip()
        
    def show_back_button(self, screen):
        color = (204, 229, 255)
        font_file = pygame.font.match_font('方正粗黑宋简体')
        font = pygame.font.Font(font_file, 24)
        text = font.render("返回主菜单", True, color)
        screen.blit(text, (0, 0))
        self.back_rect = pygame.Rect(0, 0, text.get_width(), text.get_height())
        surface = pygame.Surface((text.get_width(), text.get_height()))
        surface.set_alpha(128)
        surface.fill((224, 224, 224))
        pygame.draw.rect(screen, (224, 224, 224), (0, 0, self.back_rect.width, self.back_rect.height), 3)
        screen.blit(surface, (0, 0))
        if self.back_box is not None:
            pygame.draw.rect(screen, (160, 160, 160), self.back_box, 3)
    
    def draw_countdown(self, screen, countdown):
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
        self.countdown = max(self.COUNTDOWN_TIME - seconds, 0)
        font = pygame.font.SysFont(None, 55)
        text = font.render(f"Time Left: {self.countdown}", True, (255, 255, 255))
        screen.blit(text, (self.WINDOW_WIDTH - 300, self.WINDOW_HEIGHT - 80))
    
    def click_start(self, x, y):
        game_state = 'main_menu'  
        if self.start_box is not None and self.start_rect.collidepoint(x, y):
            game_state = 'choose_level'
        return game_state
    
    def click_back(self, game_state, x, y):
        if self.back_box is not None and self.back_rect.collidepoint(x, y):
            game_state = 'main_menu'
            self.reset_game()
        return game_state
    
    def choose_pic(self, x, y):
        col, row = self.game_screen.get_row_col(x, y)
        if 0 <= col < self.game_screen.COLS and 0 <= row < self.game_screen.ROWS: 
            for layer in range(self.game_screen.layers):
                if self.game_screen.board[layer][row][col] is not None and self.game_screen.is_top_layer(row, col, layer):
                    if self.game_screen.is_point_inside_image(x, y, layer):
                        self.game_screen.selected.append((row, col, layer))
                        self.status_bar.clicked_images.append(self.game_screen.board[layer][row][col])
                        self.game_screen.choose_picture()
                        break

    def choose_level(self, x, y):
        game_state = 'choose_level'
        if self.level_box is not None and self.level_rect[0].collidepoint(x, y):
            game_state = 'playing'
            self.game_screen.get_patterns("hubei")
            self.game_screen.creat_board("hubei")
            self.start_ticks = pygame.time.get_ticks()  # 重置开始时间
            self.countdown = self.COUNTDOWN_TIME  # 重置倒计时
        elif self.level_box is not None and self.level_rect[1].collidepoint(x, y):
            game_state = 'playing'
            self.game_screen.get_patterns("hunan")
            self.game_screen.creat_board('hunan')
            self.start_ticks = pygame.time.get_ticks()  # 重置开始时间
            self.countdown = self.COUNTDOWN_TIME  # 重置倒计时
        elif self.level_box is not None and self.level_rect[2].collidepoint(x, y):
            game_state = 'playing'            
            self.game_screen.get_patterns("fujian")
            self.game_screen.creat_board('fujian')
            self.start_ticks = pygame.time.get_ticks()  # 重置开始时间
            self.countdown = self.COUNTDOWN_TIME  # 重置倒计时
        
        return game_state

    def get_start_box(self, x, y):
        if self.start_rect is not None and self.start_rect.collidepoint(x, y):
            self.start_box = self.start_rect
        else:
            self.start_box = None
        
    def get_choose_hover_box(self, x, y):
        col, row = self.game_screen.get_row_col(x, y)
        if 0 <= col < self.game_screen.COLS and 0 <= row < self.game_screen.ROWS:
            for layer in range(self.game_screen.layers):
                if self.game_screen.board[layer][row][col] is not None and self.game_screen.is_top_layer(row, col, layer):
                    if self.game_screen.is_point_inside_image(x, y, layer):
                        self.game_screen.hovered = (row, col, layer)
                        break
                    else:
                        self.game_screen.hovered = None
                else:    
                    self.game_screen.hovered = None

    def get_level_hover_box(self, x, y):
        for rect in self.level_rect:
            if rect and rect.collidepoint(x, y):
                self.level_box = rect
                break
            else:
                self.level_box = None
    
    def get_back_hover_box(self, x, y):
        if self.back_rect is not None and self.back_rect.collidepoint(x, y):
            self.back_box = self.back_rect
        else:
            self.back_box = None

    def reset_game(self):
        self.game_screen.board.clear()
        self.status_bar.clicked_images.clear()
        self.game_screen.selected.clear()
        self.level_box = None  
        self.game_screen.tiles.clear()
        self.game_screen.patterns.clear()

    