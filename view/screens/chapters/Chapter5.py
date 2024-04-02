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


class Chapter5(Chapter):
    """
    Class representing Chapter 5 of the game.

    Attributes:
    :show_choices (bool): Flag indicating whether choices need to be displayed.
    :choices_made (dict): Dictionary storing choices made during the chapter.
    :current_dialogue_index (int): Index of the current dialogue in the chapter.
    :current_scene_index (int): Index of the current scene in the chapter.
    :selected_choice_index (int): Index of the selected choice.
    :next_background_index (int): Index of the next background image.
    :dialogue_options (dict): Dictionary mapping dialogue indices to available choices.

    """
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):
        """
        Initializes Chapter5 object.

        Parameters:
        :screen (pygame.Surface): The surface to display the chapter scenes.
        :currPlayer (Player): The current player object.
        :title (str): The title of the chapter.
        :dialogueLines (List[str]): List of dialogue lines in the chapter.
        :dialogueImagePaths (List[str]): List of file paths to dialogue images.
        :controls (dict): Dictionary of control mappings.
        """
        super().__init__(5, screen, currPlayer, dialogueLines, dialogueImagePaths, controls)

        self.show_choices: bool = False
        self.choices_made: dict = {}
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0
        self.selected_choice_index = None
        self.next_background_index: int = None
        
        self.dialogue_options = {
            1: ["I really like you. Will you be my girlfriend?", "I've had a great time getting to know you, I was wondering if you want to make this official?", "So, I was thinking, we get along pretty well, huh? Maybe we should start going out for real?", "I kinda like you more than just a friend. Do you wanna be my girlfriend?"],
        }
        self.draw_chapter5()

    def draw_chapter5(self):
        """
        Draw the scenes and dialogues for Chapter 5.
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
                                 # Calculating Player's Score This Chapter and Updating It
                    for choice in self.choices_made.values():
                        if choice == "I really like you. Will you be my girlfriend?":
                            self.currPlayer.updateStats("Serena", 0)
                            print(self.currPlayer.attraction)
                        elif choice == "I've had a great time getting to know you, I was wondering if you want to make this official?":
                            self.currPlayer.updateStats("Serena", 15)                                
                            print(self.currPlayer.attraction)
                        elif choice == "So, I was thinking, we get along pretty well, huh? Maybe we should start going out for real?":
                            self.currPlayer.updateStats("Serena", 20)
                        elif choice == "I kinda like you more than just a friend. Do you wanna be my girlfriend?":
                            self.currPlayer.updateStats("Serena", 10)
                        else:
                            raise Exception("Choice Isn't Valid")
                        
                    if self.currPlayer.attraction >= 70:
                        response_text = "Yes, I’d love that!"
                        self.currPlayer.saveProgress()

                        background_index= 2
                        self.selected_choice_index = 2
                    else:
                        response_text = "Oh, sorry. I never thought of you that way. I prefer to be friends..."
                        self.currPlayer.saveProgress()
                        background_index = 3
                        self.selected_choice_index = 1
       
                    # After updating indices, get the new background and draw it
                    current_background = self.dialogueImages[background_index]
                    self.screen.blit(current_background, (0, 0))
                    dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
                    dialogue_box.draw(response_text)
    
            pygame.display.flip()          
        
            return ""

    def event_handler(self):
        """
        Handle events for Chapter 5.
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

                    if self.selected_choice_index == 1:
                        EndingScene(self.screen, "ending-rejected.png", self.currPlayer)
                        return "main"
                    elif self.selected_choice_index == 2:
                        self.currPlayer.level = 6  # Proceed to next chapter
                        self.currPlayer.saveProgress
                        return "chp"
                            
                    self.current_dialogue_index += 1 
                    if not self.show_choices:
                            #if there is a next background index
                        if self.next_background_index:                  
                            self.current_scene_index = self.next_background_index
                            self.next_background_index = None
                        else:
                            self.current_scene_index += 1  # Proceed to the next background index
                        
                       
                    self.draw_chapter5()  # Redraw dialogue.