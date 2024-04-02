from controller.constants import *
import pygame
import sys
from view.components.Button import Button

class Help2:
    """
    Class representing the second help screen in the game.

    Attributes:
    :game_state: String representing the state of the help2 screen.
    :help2: Pygame surface object representing the image for the help2 screen.
    :back_to_help1_button: Button object representing the button to go back to the first help screen.
    """

    def __init__(self) -> None:
        """
        Initialize the Help2 object.
        """
        self.game_state = "help2"

        # Load help2 images
        path = os.path.join('view', 'assets', 'help2.png')
        help2 = pygame.image.load(path)
        self.help2 = pygame.transform.scale(help2, (screen_width, help2.get_height() / (help2.get_width() / screen_width)))

        # Load help2 menu buttons
        self.back_to_help1_button = Button(screen_width/10, 7*(screen_height/8), (screen_width/4), (screen_height/13), "Back", GRAY , "help1", pygame)

    def draw_help2(self, screen: pygame.Surface) -> None:
        """
        Draw the help2 screen on the pygame surface.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        screen.fill(LIGHT_GRAY)
        screen.blit(self.help2, (0, 0))
        self.back_to_help1_button.draw(screen)
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface) -> str:
        """
        Handle events in the help2 screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        help2_active = True
        while help2_active:
            # Checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        help2_active = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_to_help1_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.back_to_help1_button.draw(screen)
                        return self.game_state

            self.draw_help2(screen)
