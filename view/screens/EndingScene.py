import pygame
from controller.constants import *
from models.Player import Player
import os


class EndingScene:
    def __init__(self, screen: pygame.surface, endingFile: str, currPlayer: Player):
        self.screen: pygame.surface = screen
        self.endingFile: str = os.path.join("view", "assets", endingFile)
        self.currPlayer: Player = currPlayer

        self.event_handler()

    def draw_ending_scene(self) -> None:
        image = pygame.image.load(self.endingFile)

        # Scale the image to cover the whole screen
        image = pygame.transform.scale(image, (screen_width, screen_height))
        self.screen.blit(image, (0, 0))

        # Update the display
        pygame.display.flip()

    def event_handler(self) -> None:
        while True:
            for event in pygame.event.get():
                self.checkQuitGame(event)

                # Returns to the Main Menu After User Presses Mouse Button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

            self.draw_ending_scene()

    """ Public Method Which Just Detects If The Game Has Been Quit (to be called in the beginning of the event loop)"""
    def checkQuitGame(self, event: pygame.event.Event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.currPlayer.saveProgress()
            pygame.quit()
            sys.exit()







