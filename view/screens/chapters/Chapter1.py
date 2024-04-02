from view.screens.chapters.Chapter import Chapter
from view.components.DialogueBox import DialogueBox
from view.components.Choices import ChoicesScreen
from view.screens.EndingScene import EndingScene

from models.Player import Player
from controller.constants import *

import pygame
from typing import List


class Chapter1(Chapter):
    """
    Class representing Chapter 1 of the game.

    Attributes:
    :show_choices (bool): Flag indicating whether choices need to be displayed.
    :showing_choices (bool): Flag indicating if choices are currently being shown.
    :current_dialogue_index (int): Index of the current dialogue in the chapter.
    :current_scene_index (int): Index of the current scene in the chapter.
    """
    def __init__(self, screen: pygame.Surface, gameSession: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict) -> None:
        """
        Initializes Chapter1 object.

        Parameters:
        :screen (pygame.Surface): The surface to display the chapter scenes.
        :gameSession (Player): The current player object.
        :title (str): The title of the chapter.
        :dialogueLines (List[str]): List of dialogue lines in the chapter.
        :dialogueImagePaths (List[str]): List of file paths to dialogue images.
        :controls (dict): Dictionary of control mappings.
        """
        super().__init__(1, screen, gameSession, dialogueLines, dialogueImagePaths, controls)

        self.show_choices: bool = False
        self.showing_choices: bool = False
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0

    def draw_chapter1(self) -> str:
        """
        Draw the scenes and dialogues for Chapter 1.

        Returns:
        :str: An empty string.
        """
        current_background = self.dialogueImages[self.current_dialogue_index]
        self.screen.blit(current_background, (0, 0))
        dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
        dialogue_text = self.dialogueLines[self.current_dialogue_index]
        dialogue_box.draw(dialogue_text)
        pygame.display.flip()

        if self.current_dialogue_index == 6 and not self.show_choices:
            self.show_choices = True
        return ""

    def event_handler(self) -> str:
        """
        Handle events and user inputs for Chapter 1.

        """
        while True:
            for event in pygame.event.get():
                # Checks if Users Quit or if The Developer Mode Used "God Powers" (ie: jumped between screens)
                self.checkQuitGame(event)
                if self.checkGodMode(event):
                    self.currPlayer.level = self.checkGodMode(event)
                    return "chp"

                # Handle scene transitions and user inputs
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_sfx.play()
                    self.current_dialogue_index += 1

                    # Check if we need to show choices
                    if self.current_dialogue_index == 6 and not self.show_choices:
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
