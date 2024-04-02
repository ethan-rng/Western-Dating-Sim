from view.screens.chapters.Chapter import Chapter
from view.components.DialogueBox import DialogueBox
from view.components.Choices import ChoicesScreen
from view.screens.EndingScene import EndingScene
from models.Player import Player
from controller.constants import *
import time

import pygame
from typing import List
import sys


class Chapter3(Chapter):
    """
    Class representing Chapter 3 of the game.

    Attributes:
    :show_choices (bool): Flag indicating whether choices need to be displayed.
    :choices_made (dict): Dictionary storing choices made during the chapter.
    :current_dialogue_index (int): Index of the current dialogue in the chapter.
    :current_scene_index (int): Index of the current scene in the chapter.
    :selected_choice_index (int): Index of the selected choice.
    :next_background_index (int): Index of the next background image.
    :dialogue_options (dict): Dictionary mapping dialogue indices to available choices.
    :dialogue_responses (dict): Dictionary mapping choices to their respective responses.

    """
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):
        """
        Initializes Chapter3 object.

        Parameters:
        :screen (pygame.Surface): The surface to display the chapter scenes.
        :currPlayer (Player): The current player object.
        :title (str): The title of the chapter.
        :dialogueLines (List[str]): List of dialogue lines in the chapter.
        :dialogueImagePaths (List[str]): List of file paths to dialogue images.
        :controls (dict): Dictionary of control mappings.
        """
        super().__init__(3, screen, currPlayer, dialogueLines, dialogueImagePaths, controls)

        self.show_choices: bool = False
        self.choices_made: dict = {}
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0
        self.selected_choice_index = None
        self.next_background_index: int = None

        self.dialogue_options = {
            1: ["Wtf?", "Yeah a little, no worries.", "Yeah it looks like shit.", "LMFAO, my house is messier"],
            5: ["Your drawing sucks", "Thanks! It looks ok", "Wow it looks really nice!",
                "Wow! It looks like me! I love it!"],
            10: ["Maybe, you’re the problem", "Yeah, but we can all be.", "Sounds like a shit brother",
                 "My siblings are the same, love them though"]
        }

        self.dialogue_responses = {
            "Wtf?": ("What a rude response (-5)"),
            "Yeah a little, no worries.": ("Truthful but polite (2)"),
            "Yeah it looks like shit.": ("What a rude response (-5)"),
            "LMFAO, my house is messier": ("Nice one! (+5)"),
            "Your drawing sucks": ("What a rude response (-10)"),
            "Thanks! It looks ok": ("You can come up with a better response (0)"),
            "Wow it looks really nice!": ("Not bad (5)"),
            "Wow! It looks like me! I love it!": ("Nice one! (10)"),
            "Maybe, you’re the problem": ("What a rude response (-10)"),
            "Yeah, but we can all be.": ("What are you thinking... (-5)"),
            "Sounds like a shit brother": ("...Just why (-10)"),
            "My siblings are the same, love them though": ("Good job! (5)")
        }

        self.draw_chapter3()

    def draw_chapter3(self):
        """
        Draw the scenes and dialogues for Chapter 3.
        """
        while True:
            current_background = self.dialogueImages[self.current_scene_index]
            self.screen.blit(current_background, (0, 0))
            dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
            dialogue_text = self.dialogueLines[self.current_dialogue_index]
            dialogue_box.draw(dialogue_text)

            if not self.show_choices and self.current_dialogue_index in self.dialogue_options:
                # Dialogue options are available for this index, index 2 and 4
                # Show choices and display
                self.show_choices = True
                choices_screen = ChoicesScreen(self.screen, self.dialogue_options[self.current_dialogue_index])
                self.selected_choice_index = choices_screen.display()

                # if selected choice index isnt none...
                if self.selected_choice_index is not None:
                        # show the selected choice response and background text
                    selected_option_text = self.dialogue_options[self.current_dialogue_index][self.selected_choice_index]
                        # Get the response text
                    response_text = self.dialogue_responses[selected_option_text]
                        # store the choice made
                    self.choices_made[self.current_dialogue_index] = selected_option_text
                    self.show_choices = False

                        # After updating indices, get the new background and draw it
                    #current_background = self.dialogueImages[background_index]
                    self.screen.blit(current_background, (0, 0))
                    dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
                    dialogue_box.draw(response_text)
                    self.selected_choice_index = None
            pygame.display.flip()

            return ""

    def event_handler(self):
        """
        Handle events and user inputs for Chapter 3.
        """
        while True:
            for event in pygame.event.get():
                # Checks if Users Quit or if The Developer Mode Used "God Powers" (ie: jumped between screens)
                self.checkQuitGame(event)
                if self.checkGodMode(event):
                    self.currPlayer.level = self.checkGodMode(event)
                    return "chp"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #click_sfx.play()
                    self.current_dialogue_index += 1
                    if self.current_dialogue_index >= len(
                            self.dialogueLines) - 1:  # Check if dialogue is over, next chapter

                        # Calculating Player's Score This Chapter and Updating It
                        for choice in self.choices_made.values():
                            if choice == "Yeah it looks like shit.":
                                self.currPlayer.updateStats("Serena", -5)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "Wtf?":
                                self.currPlayer.updateStats("Serena", -5)
                            elif choice == "Yeah a little, no worries.":
                                self.currPlayer.updateStats("Serena", 2)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "LMFAO, my house is messier":
                                self.currPlayer.updateStats("Serena", 5)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "Your drawing sucks":
                                self.currPlayer.updateStats("Serena", -10)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "Thanks! It looks ok":
                                self.currPlayer.updateStats("Serena", 0)
                            elif choice == "Wow it looks really nice!":
                                self.currPlayer.updateStats("Serena", 5)
                            elif choice == "Wow! It looks like me! I love it!":
                                self.currPlayer.updateStats("Serena", 10)
                            elif choice == "Maybe, you’re the problem":
                                self.currPlayer.updateStats("Serena", -10)
                            elif choice == "Yeah, but we can all be.":
                                self.currPlayer.updateStats("Serena", -5)
                            elif choice == "Sounds like a shit brother":
                                self.currPlayer.updateStats("Serena", -7)
                            elif choice == "My siblings are the same, love them though":
                                self.currPlayer.updateStats("Serena", 5)
                            else:
                                raise Exception("Choice Isn't Valid")

                        if self.currPlayer.attractionScore["Serena"] >= 20:
                            EndingScene(self.screen, "yesbbt.png", self.currPlayer)
                            self.currPlayer.level = 4  # Proceed to next chapter
                            return "chp"
                        elif self.currPlayer.attractionScore["Serena"] < 20:
                            EndingScene(self.screen, "ending-rejected.png", self.currPlayer)
                            return "main"

                    if not self.show_choices:
                        # if there is a next background index
                        if self.next_background_index:
                            self.current_scene_index = self.next_background_index
                            self.next_background_index = None
                        else:
                            self.current_scene_index += 1  # Proceed to the next background index

                    self.draw_chapter3()  # Redraw dialogue.