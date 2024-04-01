from view.screens.chapters.Chapter import Chapter
from view.components.DialogueBox import DialogueBox
from view.components.Choices import ChoicesScreen
from view.screens.EndingScene import EndingScene

from models.Player import Player
from controller.constants import *

import pygame
from typing import List


class Chapter1(Chapter):
    def __init__(self, screen: pygame.Surface, gameSession: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict) -> None:

        super().__init__(1, screen, gameSession, dialogueLines, dialogueImagePaths, controls)

        # Control Variables for Chapter 1
        self.show_choices: bool = False
        self.showing_choices: bool = False
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0

    def draw_chapter1(self) -> str:
        current_background = self.dialogueImages[self.current_dialogue_index]
        self.screen.blit(current_background, (0, 0))
        dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
        dialogue_text = self.dialogueLines[self.current_dialogue_index]  # Get current line of dialogue
        dialogue_box.draw(dialogue_text)
        pygame.display.flip()

        if self.current_dialogue_index == 5 and not self.show_choices:
            self.show_choices = True  # Prepare to display choices
        return ""

    def event_handler(self) -> str:
        while True:
            for event in pygame.event.get():
                # Checks if Users Quit or if The Developer Mode Used "God Powers" (ie: jumped between screens)
                self.checkQuitGame(event)
                self.checkGodMode(event)

                # Handle scene transitions and user inputs
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_sfx.play()
                    self.current_dialogue_index += 1

                    # Check if we need to show choices
                    if self.current_dialogue_index == 5 and not self.show_choices:
                        choices_screen = ChoicesScreen(self.screen, ["Yes", "No"])
                        selected_choice_index = choices_screen.display()
                        self.show_choices = True

                        if selected_choice_index is not None:
                            if selected_choice_index == 0:
                                self.currPlayer.level = 2  # Proceed to next chapter
                                return "chp"
                            elif selected_choice_index == 1:
                                EndingScene(self.screen, "ending-ghosted.png", self.currPlayer)
                                return "main"

                # Redraw the scene for every frame
                self.draw_chapter1()

                if self.current_dialogue_index >= len(self.dialogueLines):
                    self.current_dialogue_index = 0
                    if not self.show_choices:
                        # If no choices need to be displayed, and dialogues are over, continue showing the same scene
                        break

