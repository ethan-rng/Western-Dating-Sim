from typing import List
import os
import threading
import pygame
from controller.constants import *
from models.Player import Player
from view.screens.chapters.SceneTitle import SceneTitle


class Chapter:
    """
    Class representing a chapter in the game.

    Attributes:
    :sceneIndex (int): The index of the current scene in the chapter.
    :screen (pygame.Surface): The surface to display the chapter scenes.
    :currPlayer (Player): The current player object.
    :dialogueLines (List[str]): List of dialogue lines in the chapter.
    :dialogueImages (List[pygame.Surface]): List of images corresponding to dialogue scenes.
    :currentDialogueIndex (int): Index of the current dialogue scene.
    :controls (dict): Dictionary of control mappings.
    """
    def __init__(self, sceneIndex: int, screen: pygame.Surface, currPlayer: Player,
                 dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict) -> None:
        """
        Initializes the Chapter object.

        Parameters:
        :sceneIndex (int): The index of the current scene in the chapter.
        :screen (pygame.Surface): The surface to display the chapter scenes.
        :currPlayer (Player): The current player object.
        :dialogueLines (List[str]): List of dialogue lines in the chapter.
        :dialogueImagePaths (List[str]): List of file paths to dialogue images.
        :controls (dict): Dictionary of control mappings.
        """
        self.sceneIndex: int = sceneIndex
        self.screen: pygame.Surface = screen
        self.currPlayer: Player = currPlayer
        self.dialogueLines: List[str] = dialogueLines

        self.dialogueImages: List[pygame.Surface] = [pygame.image.load(path).convert() for path in dialogueImagePaths]
        for i, img in enumerate(self.dialogueImages):
            self.dialogueImages[i] = pygame.transform.scale(img, (screen_width, screen_height))

        self.currentDialogueIndex: int = 0
        self.controls: dict = controls

        self.updateScene()

    """ Public Method Which Simply Transitions The Chapter With A SceneTitle Element """
    def updateScene(self) -> None:
        """
        Transition the chapter with a SceneTitle element.
        """
        while True:
            for event in pygame.event.get():
                self.checkQuitGame(event)

                # Breaks Event Loop When User Presses Mouse Button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

            # Drawing out the Starting Scene
            pygame.display.set_caption(SCENE_TITLES[self.sceneIndex])
            scene_title = SceneTitle(self.screen, SCENE_TITLES[self.sceneIndex])
            scene_title.draw()
            pygame.display.flip()

    """ Public Method Which Just Detects If The Game Has Been Quit (to be called in the beginning of the event loop)"""
    def checkQuitGame(self, event: pygame.event.Event) -> None:
        """
        Check if the game has been quit.

        Parameters:
        :event (pygame.event.Event): The pygame event.

        """
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.currPlayer.saveProgress()
            pygame.quit()
            sys.exit()

    """ Public Method Which Allows the Developer to Change Their Stats and View Them """
    def checkGodMode(self, event: pygame.event.Event) -> None:
        """
        Check if the developer is in god mode.

        Parameters:
        :event (pygame.event.Event): The pygame event.

        """
        if type(self.currPlayer) == "<class 'models.Developer.Developer'>":
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL):
                if event.key == pygame.K_1:
                    self.currPlayer.jumpToScreen(1)

                elif event.key == pygame.K_2:
                    self.currPlayer.jumpToScreen(2)

                elif event.key == pygame.K_3:
                    self.currPlayer.jumpToScreen(3)

                elif event.key == pygame.K_4:
                    self.currPlayer.jumpToScreen(4)

                elif event.key == pygame.K_5:
                    self.currPlayer.jumpToScreen(5)

                elif event.key == pygame.K_6:
                    self.currPlayer.jumpToScreen(6)



