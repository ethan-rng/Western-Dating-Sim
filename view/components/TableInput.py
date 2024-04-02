import pygame
from controller.constants import *
from controller.constants import *

class TableInput:
    """
    Represents a table input component in a pygame application.

    Attributes:
        :base_rect (pygame.Rect): The rectangular area representing the base of the table input.
        :label_surface: The rendered surface for the label text.
        :label_rect (pygame.Rect): The rectangular area representing the position and size of the label text.
        :score_surface: The rendered surface for the score text.
        :score_rect (pygame.Rect): The rectangular area representing the position and size of the score text.
    """
    def __init__(self, x, y, width, height, label, score) -> None:
        """
        Initializes a TableInput object.

        Parameterss:
            :x (float): The x-coordinate of the top-left corner of the table input.
            :y (float): The y-coordinate of the top-left corner of the table input.
            :width (float): The width of the table input.
            :height (float): The height of the table input.
            :label (str): The label associated with the table input.
            :score (float): The score value associated with the table input.
        """
        self.base_rect = pygame.Rect(x,y,width,height)
        self.label_surface = font.render(label, True, BLACK)
        self.label_rect = self.label_surface.get_rect(x = self.base_rect.x + 10, centery = self.base_rect.centery)
        self.score_surface = font.render(str(score), True, BLACK)
        self.score_rect = self.score_surface.get_rect(x = self.base_rect.right - 80,centery = self.base_rect.centery)
    
    def draw(self, screen):
        """
        Draws the table input component on the screen.

        Args:
            screen (pygame.Surface): The pygame surface on which the table input will be drawn.
        """
        pygame.draw.rect(screen, WHITE, self.base_rect)
        screen.blit(self.label_surface, self.label_rect)
        screen.blit(self.score_surface, self.score_rect)