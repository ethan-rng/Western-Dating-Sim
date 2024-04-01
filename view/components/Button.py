import pygame
import sys

pygame.init()

# initilizing fonts
font = pygame.font.SysFont(None, 45)


class Button:
    def __init__(self, x, y, width, height, text, color, action, pygame_instance):

        self.rect = pygame.Rect(x, y, width, height)
        self.updateText(text)
        self.font = pygame.font.SysFont(None, 45)
        self.color = color
        self.action = action
        self.pygame_instance = pygame_instance

    def updateText(self, text):
        self.text = text
        self.render = font.render(self.text, True, 'black')
        self.text_width = self.render.get_width()
        self.text_height = self.render.get_height()

    def draw(self, screen):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return self.action

        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.render
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
