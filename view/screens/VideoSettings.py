from controller.constants import *
import pygame
import sys

from view.components.Button import Button


class VideoSettings:
    """
    Class representing the video settings screen.

    Attributes:
    :menu_state (str): The current state of the video settings menu.
    :videosettings (pygame.Surface): The image representing the video settings screen.
    :back_button (Button): The button for navigating back to the main menu.
    """
    def __init__(self) -> None:
        """
        Initializes the VideoSettings object.
        """
        self.menu_state = "videosettings"

        # load videosettings images
        path = os.path.join('view', 'assets', 'videosettings.png')
        videosettings = pygame.image.load(path)
        self.videosettings = pygame.transform.scale(videosettings, (screen_width, videosettings.get_height() / (videosettings.get_width() / screen_width)))

        # load videosettings menu buttons
        self.back_button = Button(screen_width/10, 7*(screen_height/8), (screen_width/4), (screen_height/13), "Back", GRAY, "main", pygame)

    def draw_videosettings(self, screen: pygame.Surface) -> None:
        """
        Draw the video settings screen on the given surface.

        Parameters:
        :screen (pygame.Surface): The surface to draw the video settings screen on.
        """
        screen.fill(LIGHT_GRAY)
        screen.blit(self.videosettings, (0, screen_height // 2 - self.videosettings.get_height() // 2))
        self.back_button.draw(screen)
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface) -> str:
        """
        Handle events for the video settings screen.

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

            self.draw_videosettings(screen)
