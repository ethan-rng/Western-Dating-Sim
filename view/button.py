import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, action, pygame_instance):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 40)
        self.color = color
        self.action = action
        self.pygame_instance = pygame_instance

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return self.action
                
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)