from controller.constants import *
import pygame
import sys

from view.components.Button import Button


class Album:
    """
    Class representing the album view in the game.

    Attributes:
    :menu_state: String representing the state of the album menu.
    :album: Pygame surface object representing the album image.
    :back_album_button: Button object representing the button to go back to the main menu.
    """

    def __init__(self) -> None:
        """
        Initialize the Album object.
        """
        self.menu_state = "album"

        # load album images
        path = os.path.join('view', 'assets', 'album.jpg')
        album = pygame.image.load(path)
        self.album = pygame.transform.scale(album, (screen_width, album.get_height() / (album.get_width() / screen_width)))

        # load album menu buttons
        self.back_album_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/5)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "main", pygame)

    def draw_album(self, screen: pygame.Surface) -> None:
        """
        Draw the album view on the screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        screen.fill(LIGHT_GRAY)
        screen.blit(self.album, (0, screen_height // 2 - self.album.get_height() // 2))
        self.back_album_button.draw(screen)
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface) -> str:
        """
        Handle events in the album view.

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
                    if self.back_album_button.draw(screen):
                        self.menu_state = self.back_album_button.draw(screen)
                    return self.menu_state

            self.draw_album(screen)

