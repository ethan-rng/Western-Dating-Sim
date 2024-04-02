
import pygame
import sys
from controller.constants import *
from components.Button import Button
from components.InputBox import TextInputBox

class Load:
    def __init__(self) -> None:
        self.username_input_box = TextInputBox(screen_width // 11.5, screen_height // 5, screen_width,
                                               screen_height / 20, "Username:", DARK_GRAY, pygame)
        self.password_input_box = TextInputBox(screen_width // 11.5, screen_height // 5 + screen_height // 8,
                                               screen_width, screen_height / 20, "Password:", DARK_GRAY, pygame)
        self.continue_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Continue", WHITE, "chp", pygame)

    def draw(self, screen: pygame.Surface) -> None:
        self.username_input_box.draw(screen)
        self.password_input_box.draw(screen)
        self.continue_button.draw(screen)
    
    
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))