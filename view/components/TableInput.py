import pygame
from controller.constants import *
from controller.constants import *

class TableInput:
    def __init__(self, x, y, width, height, label, score) -> None:
        self.base_rect = pygame.Rect(x,y,width,height)
        self.label_surface = font.render(label, True, BLACK)
        self.label_rect = self.label_surface.get_rect(x = self.base_rect.x + 10, centery = self.base_rect.centery)
        self.score_surface = font.render(str(score), True, BLACK)
        self.score_rect = self.score_surface.get_rect(x = self.base_rect.right - 80,centery = self.base_rect.centery)
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.base_rect)
        screen.blit(self.label_surface, self.label_rect)
        screen.blit(self.score_surface, self.score_rect)