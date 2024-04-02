import pygame
from controller.constants import *
from models.Player import Player
import os


class EndingScene:
    """
    Class representing the ending scene of the game.

    Attributes:
    :screen: Pygame surface object representing the game screen.
    :endingFile: String representing the file path of the ending image.
    :currPlayer: Player object representing the current player.
    """

    def __init__(self, screen: pygame.surface, endingFile: str, currPlayer: Player):
        """
        Initialize the EndingScene object.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        :endingFile: String representing the file path of the ending image.
        :currPlayer: Player object representing the current player.
        """
        self.screen: pygame.surface = screen
        self.endingFile: str = os.path.join("view", "assets", endingFile)
        self.currPlayer: Player = currPlayer

        self.event_handler()

    def draw_ending_scene(self) -> None:
        """
        Draw the ending scene on the screen.
        """
        image = pygame.image.load(self.endingFile)

        # Scale the image to cover the whole screen
        image = pygame.transform.scale(image, (screen_width, screen_height))
        self.screen.blit(image, (0, 0))

        # Update the display
        pygame.display.flip()

    def event_handler(self) -> None:
        """
        Handle events in the ending scene.
        """
        while True:
            for event in pygame.event.get():
                self.checkQuitGame(event)

                # Returns to the Main Menu After User Presses Mouse Button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

            self.draw_ending_scene()

    def checkQuitGame(self, event: pygame.event.Event):
        """
        Public method to detect if the game has been quit.

        Parameters:
        :event: Pygame event object representing the current event.
        """
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.currPlayer.saveProgress()
            pygame.quit()
            sys.exit()

