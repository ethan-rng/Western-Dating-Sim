import pygame, sys
from controller.constants import *
from view.components.Button import Button
from view.components.Slider import Slider
from models.Player import Player
from models.exceptions import *

class NewGameScreen:
    """
    Class representing the screen for creating a new game.

    Attributes:
    :currPlayer: Player object representing the current player.
    :intelligence: Integer representing the intelligence stat.
    :charisma: Integer representing the charisma stat.
    :attractiveness: Integer representing the attractiveness stat.
    :continue_button: Button object for continuing the game.
    :intelligence_slider: Slider object for adjusting intelligence stat.
    :charisma_slider: Slider object for adjusting charisma stat.
    :attractiveness_slider: Slider object for adjusting attractiveness stat.
    :error_message: String containing error message, if any.
    """

    def __init__(self, currPlayer: Player) -> None:
        """
        Initialize a new game screen.

        Parameters:
        :currPlayer: Player object representing the current player.
        """
        self.currPlayer: Player = currPlayer
        self.intelligence: int = 1
        self.charisma: int = 1
        self.attractiveness: int = 1

        # Initialize UI components
        self.continue_button = Button(screen_width / 2.48, (screen_height / 3) + (screen_height / 6) * 3,
                                      (screen_width / 4), (screen_height / 13), "Continue", WHITE, "chp", pygame)
        self.intelligence_slider = Slider(
            (screen_width - screen_width / 2.8, screen_height // 4 + (screen_height // 8)), (screen_width / 1.8, 20),
            "Intelligence", 0.1, 0, 10)
        self.charisma_slider = Slider(
            (screen_width - screen_width / 2.8, screen_height // 4 + (screen_height // 8) * 2),
            (screen_width / 1.8, 20), "Charisma", 0.1, 0, 10)
        self.attractiveness_slider = Slider(
            (screen_width - screen_width / 2.8, screen_height // 4 + (screen_height // 8) * 3),
            (screen_width / 1.8, 20), "Attractiveness", 0.1, 0, 10)

        self.error_message: str = ""

    def draw_newgame_screen(self, screen: pygame.Surface) -> None:
        """
        Draw the new game screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        # Drawing UI components
        screen.fill(DARK_GRAY)
        self.draw_text("New Game", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.draw_text("Allocate you stat points (up to 10)", font, BLACK, screen_width/20, screen_height/16 + screen_height/12, screen)
        self.continue_button.draw(screen)
        self.intelligence_slider.draw(screen)
        self.charisma_slider.draw(screen)
        self.attractiveness_slider.draw(screen)

        # Drawing Error Message For Illegal Stat Combo
        if self.error_message:
            error_font = pygame.font.SysFont(None, 80)
            text_surface = error_font.render(self.error_message, True, RED)
            # Calculate x position to center the text
            text_x = (screen_width - text_surface.get_width()) / 2
            text_y = (screen_height * 9) / 13
            screen.blit(text_surface, (text_x, text_y))

        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface, username: str, password: str) -> str:
        """
        Handle events on the new game screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        :username: String representing the username.
        :password: String representing the password.

        Returns:
        :str: Menu state after handling events.
        """
        newgame_active = True

        while newgame_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        newgame_active = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle mouse click events
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
                        # Handle continue button click
                        click_sfx.play()
                        self.menu_state = self.continue_button.draw(screen)

                        try:
                            self.currPlayer.createPlayer(username, password, self.charisma, self.intelligence,
                                                         self.attractiveness)
                            self.currPlayer.login(username, password)
                            return self.menu_state

                        except IncorrectPassword:
                            self.error_message = "Wrong Password for the Developer Account"
                        except IllegalStats:
                            self.error_message = "Total Stats Must Add to 10 or Lower"

            self.draw_newgame_screen(screen)

    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface) -> None:
        """
        Draw text on the screen.

        Parameters:
        :text: String representing the text to be drawn.
        :font: Pygame font object representing the font of the text.
        :text_col: Tuple representing the color of the text.
        :x: Float representing the x-coordinate of the text.
        :y: Float representing the y-coordinate of the text.
        :screen: Pygame surface object representing the game screen.
        """
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))
