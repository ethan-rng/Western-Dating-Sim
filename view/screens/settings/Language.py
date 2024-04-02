from controller.constants import *
import pygame
import sys

from view.components.Button import Button


class Language:
    """
    Class representing the language settings screen.

    Attributes:
    :menu_state (str): The current state of the language menu.
    :language (pygame.Surface): The image representing the language settings screen.
    :back_button (Button): The button for navigating back to the main menu.
    """

    def __init__(self) -> None:
        """
        Initializes the Language object.
        """
        self.menu_state = "language"

        # load language images
        path = os.path.join('view', 'assets', 'language.png')
        language = pygame.image.load(path)
        self.language = pygame.transform.scale(language, (screen_width, language.get_height() / (language.get_width() / screen_width)))

        # load language menu buttons
        self.back_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)

    def draw_language(self, screen: pygame.Surface) -> None:
        """
        Draw the language settings screen on the given surface.

        Parameters:
        :screen (pygame.Surface): The surface to draw the language settings screen on.
        """
        screen.fill(LIGHT_GRAY)
        screen.blit(self.language, (0, screen_height // 2 - self.language.get_height() // 2))
        self.back_button.draw(screen)
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface) -> str:
        """
        Handle events for the language settings screen.

        Parameters:
        :screen (pygame.Surface): The surface to handle events on.
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
                        self.menu_state = self.back_button.draw(screen)
                    return self.menu_state

            self.draw_language(screen)
