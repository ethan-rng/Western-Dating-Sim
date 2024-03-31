from typing import List
from models import Player
import os
import pygame

class Chapter:
    def __init__(self, 
                 screen: pygame.Surface,
                 currPlayer: Player,
                 title: str,
                 dialogueLines: List[str], 
                 dialogueImagePaths: List[str],
                ) -> None:
        
        self.screen: pygame.Surface = screen
        self.currPlayer: Player = currPlayer
        self.title: str = title
        self.dialogueLines: List[str] = dialogueLines
        self.dialogueImagePaths: List[str] = dialogueImagePaths
        self.currentDialogueIndex: int = 0


