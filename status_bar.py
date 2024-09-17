import pygame

#STATUS_BAR_HEIGHT = 100
#GAP_HEIGHT = 20
#TILE_SIZE = 100
#ROWS = 6

class status_bar:    
    def __init__(self, ROWS, WINDOW_WIDTH, HEIGHT, TILE_SIZE, GAP_HEIGHT, STATUS_BAR_HEIGHT):    
        self.clicked_images = []
        self.ROWS = ROWS
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.GAME_SCREEN_HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE
        self.GAP_HEIGHT = GAP_HEIGHT
        self.STATUS_BAR_HEIGHT = STATUS_BAR_HEIGHT

    def draw_status_bar(self, screen, GAP_BETWEEN=148):
        x, y = 0, self.GAME_SCREEN_HEIGHT + self.GAP_HEIGHT
        rect = pygame.Rect(x, y, (self.ROWS -1 ) * self.TILE_SIZE, self.STATUS_BAR_HEIGHT)
        surface = pygame.Surface(rect.size)
        surface.set_alpha(128)
        surface.fill((204, 255, 255))
        screen.blit(surface, (x, y))
        pygame.draw.rect(screen, (204, 255, 255), (x, y, (self.ROWS - 1) * self.TILE_SIZE, self.STATUS_BAR_HEIGHT), 3)

        for i, image in enumerate(self.clicked_images):
            image = pygame.transform.scale(image, (self.STATUS_BAR_HEIGHT, self.STATUS_BAR_HEIGHT))
            screen.blit(image, ( i * self.STATUS_BAR_HEIGHT, 
                                self.GAME_SCREEN_HEIGHT + self.GAP_HEIGHT))

    def check_status(self):
        # 如果状态栏中有三种同样的图案，则将这三个图像消除，更新状态栏
        # 创建一个字典来记录每种图案的数量及其索引
        pattern_count = {}
        for i, image in enumerate(self.clicked_images):
            if image not in pattern_count:
                pattern_count[image] = []
            pattern_count[image].append(i)
        
        # 查找数量达到3的图案
        for image, indices in pattern_count.items():
            if len(indices) >= 3:
                # 移除这三个图案
                for index in sorted(indices[:3], reverse=True):
                    del self.clicked_images[index]
                break  # 只处理一次匹配，避免多次删除导致索引错误
        
        if len(self.clicked_images) >= 6:
            return False
        return True