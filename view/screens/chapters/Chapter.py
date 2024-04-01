from typing import List
from models import Player
import os
import pygame
from controller.constants import *
from view.screens.chapters.SceneTitle import SceneTitle


class Chapter:
    def __init__(self, sceneIndex: int, screen: pygame.Surface, currPlayer: Player,
                 dialogueLines: List[str], dialogueImagePaths: List[str]) -> None:
        
        self.sceneIndex: int = sceneIndex
        self.screen: pygame.Surface = screen
        self.currPlayer: Player = currPlayer
        self.dialogueLines: List[str] = dialogueLines
        self.dialogueImagePaths: List[str] = dialogueImagePaths
        self.currentDialogueIndex: int = 0

        self.updateScene(self.sceneIndex)

    
    def updateScene(self, sceneIndex: int) -> None:            
        pygame.display.set_caption(SCENE_TITLES[sceneIndex])  
        scene_title = SceneTitle(self.screen, SCENE_TITLES[sceneIndex] )
        scene_title.draw()
        pygame.display.flip()



    