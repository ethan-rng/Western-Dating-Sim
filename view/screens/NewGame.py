import pygame, os
from controller.constants import *
from view.components.Button import Button
from view.components.Slider import Slider
from view.components.InputBox import TextInputBox
from models.Player import Player
from models.exceptions import *
from models.Developer import Developer


class NewGameScreen:
    def __init__(self, currPlayer: Player) -> None:
        self.currPlayer: Player = currPlayer
        self.intelligence: int = 5
        self.charisma: int = 5
        self.attractiveness: int = 5

        self.continue_button = Button(screen_width / 2.48, (screen_height / 3) + (screen_height / 6) * 3,
                                      (screen_width / 4), (screen_height / 13), "Continue", WHITE, "chp", pygame)
        self.intelligence_slider = Slider(
            (screen_width - screen_width / 2.8, screen_height // 4 + (screen_height // 8)), (screen_width / 1.8, 20),
            "Intelligence", 0.5, 0, 10)
        self.charisma_slider = Slider(
            (screen_width - screen_width / 2.8, screen_height // 4 + (screen_height // 8) * 2),
            (screen_width / 1.8, 20), "Charisma", 0.5, 0, 10)
        self.attractiveness_slider = Slider(
            (screen_width - screen_width / 2.8, screen_height // 4 + (screen_height // 8) * 3),
            (screen_width / 1.8, 20), "Attractiveness", 0.5, 0, 10)

        self.error_message: str = ""

    def draw_newgame_screen(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.continue_button.draw(screen)
        self.intelligence_slider.draw(screen)
        self.charisma_slider.draw(screen)
        self.attractiveness_slider.draw(screen)

        # Drawing Error Message For Illegal Stat Combo
        if self.error_message:
            font = pygame.font.SysFont(None, 80)
            text_surface = font.render(self.error_message, True, RED)
            # Calculate x position to center the text
            text_x = (screen_width - text_surface.get_width()) / 2
            text_y = (screen_height * 9) / 13
            screen.blit(text_surface, (text_x, text_y))

        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface, username: str, password: str) -> str:
        newgame_active = True
        event_list = pygame.event.get()

        while newgame_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        newgame_active = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_sfx.play()
                    mouse_pos = pygame.mouse.get_pos()
                    mouse = pygame.mouse.get_pressed()

                    # Update sliders and variables based on mouse clicks
                    if self.intelligence_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.intelligence_slider.moveSlider(mouse_pos)
                        self.intelligence_slider.updateText()
                        self.intelligence = self.intelligence_slider.getValue()

                    if self.charisma_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.charisma_slider.moveSlider(mouse_pos)
                        self.charisma_slider.updateText()
                        self.charisma = self.charisma_slider.getValue()

                    if self.attractiveness_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.attractiveness_slider.moveSlider(mouse_pos)
                        self.attractiveness_slider.updateText()
                        self.attractiveness = self.attractiveness_slider.getValue()

                    if self.continue_button.rect.collidepoint(mouse_pos) and mouse[0]:
                        click_sfx.play()
                        self.menu_state = self.continue_button.draw(screen)

                        try:
                            self.currPlayer.createPlayer(username, password, self.charisma, self.intelligence,
                                                         self.attractiveness)
                            self.currPlayer.login(password)
                            return self.menu_state

                        except IncorrectPassword:
                            self.error_message = "Wrong Password for the Developer Account"
                        except IllegalStats:
                            self.error_message = "Total Stats Must Add to 10 or Lower"

            self.draw_newgame_screen(screen)
