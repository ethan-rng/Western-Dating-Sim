from typing import List

class Chapter:
    def __init__(self, dialogueLines:List[str]=[]) -> None:
        self.dialogueLines: List[str] = dialogueLines
        self.currentDialogueIndex: int = 0
        self.menu_items = ["Start New Game", "Load Game", "Highscores", "Album","Settings", "Help", "Quit"]


