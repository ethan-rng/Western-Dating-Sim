from controller.constants import *
import pygame
import sys
from view.components.Button import Button

class Help1:
    """
    Class representing the first help screen in the game.

    Attributes:
    :game_state: String representing the state of the help1 screen.
    :help1: Pygame surface object representing the image for the help1 screen.
    :back_button: Button object representing the button to go back to the main menu.
    :next_button: Button object representing the button to proceed to the second help screen.
    """

    def __init__(self) -> None:
        """
        Initialize the Help1 object.
        """
        self.game_state = "help1"

        # Load help1 images
        path = os.path.join('view', 'assets', 'help1.png')
        help1 = pygame.image.load(path)
        self.help1 = pygame.transform.scale(help1, (screen_width, help1.get_height() / (help1.get_width() / screen_width)))

        # Load help1 menu buttons
        self.back_button = Button(screen_width/10, 7*(screen_height/8), (screen_width/4), (screen_height/13), "Back", GRAY, "main", pygame)
        self.next_button = Button(6.5*screen_width/10, 7*(screen_height/8), (screen_width/4), (screen_height/13), "Next", GRAY, "help2", pygame)

    def draw_help1(self, screen: pygame.Surface) -> None:
        """
        Draw the help1 screen on the pygame surface.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        screen.fill(LIGHT_GRAY)
        screen.blit(self.help1, (0, screen_height // 2 - self.help1.get_height() // 2))
        self.back_button.draw(screen)
        self.next_button.draw(screen)
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface) -> str:
        """
        Handle events in the help1 screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        while True:
            # Checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_sfx.play()
                    if self.back_button.draw(screen):
                        self.game_state = self.back_button.draw(screen)
                    elif self.next_button.draw(screen):
                        self.game_state = self.next_button.draw(screen)
                    return self.game_state

            self.draw_help1(screen)
