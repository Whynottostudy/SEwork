import pygame
import random

class game_screen:
    def __init__(self, ROWS, COLS, TILE_SIZE, GAP_LEFT, GAP_TOP, GAP_BETWEEN=148):
        self.board = []
        self.selected = []
        self.hovered = None
        self.city = None
        self.ROWS = ROWS
        self.COLS = COLS
        self.TILE_SIZE = TILE_SIZE
        self.layers = 3
        self.tiles = []
        self.GAP_LEFT = GAP_LEFT
        self.GAP_TOP = GAP_TOP
        self.GAP_BETWEEN = GAP_BETWEEN
        self.GAP_VERTICAL = self.TILE_SIZE + 7
        self.patterns = []
        self.patterns = []
        self.pattern_count = {'hubei':[6, 6, 6, 6, 6, 6], 'hunan':[3, 3, 6, 6, 6, 6, 3, 3], 'fujian':[3, 3, 3, 3, 3, 3, 3, 3, 6, 6]}
        

    def draw_board(self, screen, gap=16):
        for layer in range(self.layers):
            for row in range(self.ROWS):
                for col in range(self.COLS):
                    tile = self.board[layer][row][col]
                    if tile is not None:
                        x = self.GAP_LEFT + gap * layer + col * self.GAP_BETWEEN
                        y = self.GAP_TOP + row * self.GAP_VERTICAL
                        screen.blit(tile, (x, y))
                        
    def get_patterns(self, city):
        if city == 'fujian':
            self.patterns = [pygame.image.load(f'patterns/fujian/pattern_{i}.jpg') for i in range(10)]
        elif city == 'hubei':
            self.patterns = [pygame.image.load(f'patterns/hubei/pattern_{i}.jpg') for i in range(6)]
        elif city == 'hunan':
            self.patterns = [pygame.image.load(f'patterns/hunan/pattern_{i}.jpg') for i in range(8)]
        self.city = city
        self.patterns = [pygame.transform.scale(p, (self.TILE_SIZE, self.TILE_SIZE)) for p in self.patterns]

    def choose_picture(self):
        # 选择图案
        r1, c1, layer = self.selected[0]
        self.board[layer][r1][c1] = None
        self.selected.clear()

    def creat_board(self, city='fujian'):
        self.board = [[[None for _ in range(self.COLS)] for _ in range(self.ROWS)] for _ in range(self.layers)]
        pattern_count = self.pattern_count[city].copy()
        random.shuffle(pattern_count)
        # 创建一个包含每种图案3倍数量的列表
        for pattern in self.patterns:
            self.tiles.extend([pattern] * pattern_count.pop())
        # 打乱图案列表
        random.shuffle(self.tiles)
        # 填充每一层的游戏板
        for layer in range(self.layers):
            random.shuffle(self.tiles)
            for row in range(self.ROWS):
                for col in range(self.COLS):
                    if self.tiles:
                        self.board[layer][row][col] = self.tiles[row * self.COLS + col]

    def check_game_screen(self):
        # 检查游戏板中是否还有相同的图案
        for layer in range(self.layers):
            for row in range(self.ROWS):
                for col in range(self.COLS):
                    if self.board[layer][row][col] is not None:
                        return False
        return True
    
    def get_row_col(self, x, y):
        col, row = (x - self.GAP_LEFT) // (self.GAP_BETWEEN), (y - self.GAP_TOP) // (self.GAP_VERTICAL)

        return col , row

    def get_image_x_y(self, row, col, layer, gap=16):
        image_x = col * (self.GAP_BETWEEN) + self.GAP_LEFT + layer * gap
        image_y = row * (self.GAP_VERTICAL) + self.GAP_TOP
        return image_x, image_y

    def is_point_inside_image(self, x, y, layer, gap=16):
        col, row = self.get_row_col(x, y)
        image_x, image_y = self.get_image_x_y(row, col, layer, gap)
        if x >= image_x and x < image_x + self.TILE_SIZE and y >= image_y and y < image_y + self.TILE_SIZE:
            return True
        return False  
    
    def is_top_layer(self, row, col, layer):
        for l in range(layer + 1, self.layers):
            if l < self.layers and self.board[l][row][col] is not None:
                return False
        return True
    
    def draw_hover_box(self, screen):
        if self.hovered is not None:
            row, col, layer = self.hovered
            image_x , image_y = self.get_image_x_y(row, col, layer) 
            pygame.draw.rect(screen, (244, 250, 57), (image_x, image_y, self.TILE_SIZE, self.TILE_SIZE), 5)