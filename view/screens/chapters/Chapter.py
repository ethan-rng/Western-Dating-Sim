from typing import List
import os
import threading
import pygame
from controller.constants import *
from models.Player import Player
from view.screens.chapters.SceneTitle import SceneTitle


class Chapter:
    def __init__(self, sceneIndex: int, screen: pygame.Surface, currPlayer: Player,
                 dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict) -> None:

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
    def checkQuitGame(self, event: pygame.event.Event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.currPlayer.saveProgress()
            pygame.quit()
            sys.exit()

    """ Public Method Which Allows the Developer to Change Their Stats and View Them """
    def checkGodMode(self):
        if

