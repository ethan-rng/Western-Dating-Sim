from view.screens.chapters.Chapter import Chapter
from view.components.DialogueBox import DialogueBox
from view.components.Choices import ChoicesScreen
from controller.constants import *
from models.Player import Player

import pygame
from typing import List
import sys


class Chapter1(Chapter):
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):

        super().__init__(1, screen, currPlayer, dialogueLines, dialogueImagePaths, controls)

        # Control Variables for Chapter 1
        self.show_choices: bool = False
        self.showing_choices: bool = False
        self.choices_made: dict = {}
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0

        self.draw_chapter1()

    def draw_chapter1(self):
        current_background = self.dialogueImages[self.current_dialogue_index]
        self.screen.blit(current_background, (0, 0))
        dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
        dialogue_text = self.dialogueLines[self.current_dialogue_index]  # Get current line of dialogue
        dialogue_box.draw(dialogue_text)
        pygame.display.flip()

        # Fifth Scene
        if self.current_dialogue_index == 5 and not self.show_choices:
            choices_screen = ChoicesScreen(self.screen, ["Yes", "No"])
            selected_choice_index = choices_screen.display()  # Display choices and get selected option
            self.show_choices = True  # Avoid displaying choices again if we're still on this dialogue point
            self.choices_made[self.current_dialogue_index] = selected_choice_index  # Remember the choice made

            # Logic to set the next dialogue index based on the choice
            if selected_choice_index is not None:
                if selected_choice_index == 0:
                    self.current_scene_index += 1
                    self.updateScene(self.current_scene_index)
                if selected_choice_index == 1:
                    # For example, choosing the first option might skip to another dialogue point
                    self.current_dialogue_index = 0

            self.show_choices = False  # Reset for the next time choices need to be displayed

            pygame.display.flip()

    def event_handler(self):
        while True:
            for event in pygame.event.get():
                self.checkQuitGame(event)

                if self.show_choices:
                    choices = ["Yes", "No"]  # Example choices
                    choice_screen: ChoicesScreen = ChoicesScreen(self.screen, choices)
                    choice_screen.display()  # Display the choices screen
                    selected_choice = choice_screen.get_selected_choice()
                    if selected_choice is not None:
                        print(f"Player selected: {choices[selected_choice]}")
                        # Handle the choice here (e.g., modify game state based on the selection)
                        self.showing_choices = False  # Reset the flag after handling the choice

                if event.type == pygame.KEYDOWN:
                    click_sfx.play()
                    self.current_dialogue_index += 1  # Move to the next dialogue line
                    if self.current_dialogue_index >= len(self.dialogueLines):  # Loop or end dialogue
                        self.current_dialogue_index = 0  # Reset index or change state as needed
