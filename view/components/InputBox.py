# import sys module
import pygame
import sys
from controller.constants import *


class TextInputBox:
    """
    Represents a text input box for user interaction in a pygame application.

    Attributes:
        :x (float): The x-coordinate of the top-left corner of the text input box.
        :y (float): The y-coordinate of the top-left corner of the text input box.
        :width (float): The width of the text input box.
        :height (float): The height of the text input box.
        :label (str): The label associated with the text input box.
        :color (tuple): The color of the text input box.
        :pygame_instance: An instance of the pygame module.
        :user_text (str): The text entered by the user.
        :input_rect (pygame.Rect): The rectangular area for the text input box.
        :active (bool): Indicates whether the text input box is currently active (accepting input) or not.
    """
    def __init__(self, x, y, width, height, label, color, pygame_instance) -> None:
        # pygame.init() will initialize all
        # imported module
        """
        Initializes a TextInputBox object.

        Parameters:
            :x (float): The x-coordinate of the top-left corner of the text input box.
            :y (float): The y-coordinate of the top-left corner of the text input box.
            :width (float): The width of the text input box.
            :height (float): The height of the text input box.
            :label (str): The label associated with the text input box.
            :color (tuple): The color of the text input box.
            :pygame_instance: An instance of the pygame module.
        """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.user_text = ''

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.color = color
        self.pygame = pygame_instance
        self.input_rect = pygame.Rect(self.x + self.x * 1.7, self.y + self.y // 6.5, self.width, self.height)
        self.active = False

    def draw(self, screen: pygame.Surface) -> bool:
        """
        Draws the text input box on the screen.

        Parameters:
            :screen (pygame.Surface): The pygame surface on which the text input box will be drawn.
        """
        pos = pygame.mouse.get_pos()

        if self.input_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.active = True
                return self.active

        input_box_rect = pygame.Rect(self.x - self.x // 2.5, self.y + self.y // 10, self.width / 1.057,
                                     self.height * 1.5)
        pygame.draw.rect(screen, WHITE, input_box_rect)

        pygame.draw.rect(screen, self.color, self.input_rect)
        text_surface = font.render(self.user_text, True, BLACK)

        text_label_surface = font.render(self.label, True, 'black')
        text_label_rect = text_label_surface.get_rect(center=(self.x + self.x, self.y + 70))

        text_label_rect.centery = input_box_rect.centery
        self.input_rect.centery = input_box_rect.centery

        screen.blit(text_surface, (self.input_rect.x + 6, self.input_rect.y + 10))
        screen.blit(text_label_surface, text_label_rect)

        if self.label == "Player Username:":
            self.input_rect.w = max(screen_width / 4, text_surface.get_width() + 10)
            self.input_rect.x = input_box_rect.x * 5
        # set width of textfield so that text cannot get
        # outside of user's text input
        else:
            self.input_rect.w = max(screen_width / 1.35, text_surface.get_width() + 10)

    def updateText(self, screen: pygame.Surface) -> None:
        """
        Updates the text input box with the user's input text.

        Parameters:
            :screen (pygame.Surface): The pygame surface on which the text input box will be updated.
        """
        pygame.draw.rect(screen, self.color, self.input_rect)
        text_surface = font.render(self.user_text, True, BLACK)

        # render at position stated in arguments
        screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        self.input_rect.w = max(10, text_surface.get_width() + 10)

    def event_handler(self, screen: pygame.Surface) -> None:
        """
        Handles events related to the text input box.

        Parameters:
            :screen (pygame.Surface): The pygame surface on which the events will be handled.
        """
        while self.active == True:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.input_rect.collidepoint(pos):
                        self.active = False

                if event.type == pygame.KEYDOWN:

                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:

                        # get text input from 0 to -1 i.e. end.
                        self.user_text = self.user_text[:-1]
                        self.updateText(screen)
                        pygame.display.flip()

                    # Unicode standard is used for string
                    # formation
                    else:
                        self.user_text += event.unicode
                        self.updateText(screen)
                        pygame.display.flip()