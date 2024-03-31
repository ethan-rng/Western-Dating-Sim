from typing import List
from models import Player
import os

class Chapter:
    def __init__(self, 
                currPlayer:Player,
                title:str,
                dialogueLines:List[str], 
                dialogueImagePaths:List[str],
                ) -> None:
        
        self.curPlayer = currPlayer
        self.title = title
        self.dialogueLines: List[str] = dialogueLines
        self.dialogueImagePaths: List[str] = dialogueImagePaths
        self.currentDialogueIndex: int = 0


