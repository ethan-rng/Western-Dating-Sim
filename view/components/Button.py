import pygame
import sys

pygame.init()

# initilizing fonts
font = pygame.font.SysFont(None, 45)


class Button:
    """
    Represents a button in a pygame application.

    Attributes:
        :x (float): The x-coordinate of the top-left corner of the button.
        :y (float): The y-coordinate of the top-left corner of the button.
        :width (float): The width of the button.
        :height (float): The height of the button.
        :text (str): The text displayed on the button.
        :color (tuple[int]): The color of the button.
        :action: The action associated with clicking the button.
        :pygame_instance: The instance of the pygame module.
    """
    def __init__(self, x, y, width, height, text, color, action, pygame_instance):
        """
        Initializes a Button object.

        Parameters:
            :x (float): The x-coordinate of the top-left corner of the button.
            :y (float): The y-coordinate of the top-left corner of the button.
            :width (float): The width of the button.
            :height (float): The height of the button.
            :text (float): The text displayed on the button.
            :color (tuple[int]): The color of the button.
            :action: The action associated with clicking the button.
            :pygame_instance: The instance of the pygame module.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.updateText(text)
        self.font = pygame.font.SysFont(None, 45)
        self.color = color
        self.action = action
        self.pygame_instance = pygame_instance

    def updateText(self, text):
        """
        Updates the text displayed on the button.

        Parameters:
            text (str): The new text to be displayed on the button.
        """
        self.text = text
        self.render = font.render(self.text, True, 'black')
        self.text_width = self.render.get_width()
        self.text_height = self.render.get_height()

    def draw(self, screen):
        """
        Draws the button on the screen.

        Parameters:
            screen: The pygame surface on which the button will be drawn.
        """
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return self.action

        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.render
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
