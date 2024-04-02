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


class Chapter6(Chapter):
    """
    Represents the sixth chapter of the game.

    Attributes:
        :screen (pygame.Surface): The pygame surface to draw on.
        :currPlayer (Player): The current player object.
        :title (str): The title of the chapter.
        :dialogueLines (List[str]): List of dialogue lines.
        :dialogueImagePaths (List[str]): List of image paths for the dialogue scenes.
        :controls (dict): Dictionary of controls for the chapter.
        :show_choices (bool): Flag to indicate whether choices are shown.
        :choices_made (dict): Dictionary to store the choices made by the player.
        :current_dialogue_index (int): Index of the current dialogue.
        :current_scene_index (int): Index of the current scene.
        :selected_choice_index: Index of the selected choice.
        :next_background_index (int): Index of the next background scene.
        :dialogue_options (dict): Dictionary containing dialogue options.
        :dialogue_responses (dict): Dictionary containing responses to dialogue options.
    """
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):
        """
        Initializes Chapter6.

        Parameters:
            :screen (pygame.Surface): The pygame surface to draw on.
            :currPlayer (Player): The current player object.
            :title (str): The title of the chapter.
            :dialogueLines (List[str]): List of dialogue lines.
            :dialogueImagePaths (List[str]): List of image paths for the dialogue scenes.
            :controls (dict): Dictionary of controls for the chapter.
        """
        super().__init__(6, screen, currPlayer, dialogueLines, dialogueImagePaths, controls)

        self.show_choices: bool = False
        self.choices_made: dict = {}
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0
        self.selected_choice_index = None
        self.next_background_index: int = None
        
        self.dialogue_options = {
            1: ["Follow", "Don't Follow"]
        }

        self.dialogue_responses = {
            "Don't Follow": ("S: I'll just stay home", 3,6),
            "Follow": ("S: Aweee. You're here?", 4,5),
        }
        
        self.draw_chapter6()

    def draw_chapter6(self):
        """
        Draws Chapter6 on the screen.
        """
        while True:
            current_background = self.dialogueImages[self.current_scene_index]
            self.screen.blit(current_background, (0, 0))
            dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
            if self.current_dialogue_index < 2:
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
                    response_text, self.background_index, self.next_background_index = self.dialogue_responses[selected_option_text]
                        # store the choice made
                    self.choices_made[self.current_dialogue_index] = selected_option_text
                    self.show_choices = False

                        # After updating indices, get the new background and draw it
                    current_background = self.dialogueImages[self.background_index]
                    self.screen.blit(current_background, (0, 0))
                    dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
                    dialogue_box.draw(response_text)
                    self.selected_choice_index = None
            pygame.display.flip()          
            return ""

    def event_handler(self):
        """
        Handles events in Chapter6.
        """
        while True:
            for event in pygame.event.get():
                # Checks if Users Quit or if The Developer Mode Used "God Powers" (ie: jumped between screens)
                self.checkQuitGame(event)
                if self.checkGodMode(event):
                    self.currPlayer.level = self.checkGodMode(event)
                    return "chp"
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    click_sfx.play()
                    self.current_dialogue_index += 1 
                    if not self.show_choices:
                        #if there is a next background index
                        if self.next_background_index:                  
                            self.current_scene_index = self.next_background_index
                            self.next_background_index = None
                        else:
                            self.current_scene_index += 1  # Proceed to the next background index
                    
                    if self.current_dialogue_index >= 3:
                        self.currPlayer.saveProgress()

                        return "main"
                        
                    self.draw_chapter6()  # Redraw dialogue.