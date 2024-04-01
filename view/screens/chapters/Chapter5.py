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
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):
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

        self.dialogue_responses = {
            "Yes": ("Yes, I’d love that!", 2,4),
            "No": ("Oh, sorry. I never thought of you that way. I prefer to be friends...", 3,4),
        }
        
        self.draw_chapter5()

    def draw_chapter5(self):
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
                    response_text, background_index, self.next_background_index = self.dialogue_responses[selected_option_text]
                        # store the choice made
                    self.choices_made[self.current_dialogue_index] = selected_option_text
                    self.show_choices = False

                        # After updating indices, get the new background and draw it
                    current_background = self.dialogueImages[background_index]
                    self.screen.blit(current_background, (0, 0))
                    dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
                    dialogue_box.draw(response_text)
                    self.selected_choice_index = None
            pygame.display.flip()          
        
            return ""

    def event_handler(self):
        while True:
            for event in pygame.event.get():
                self.checkQuitGame(event)
                if event.type == pygame.MOUSEBUTTONDOWN:            

                    self.current_dialogue_index += 1 
                    if self.current_dialogue_index >= len(self.dialogueLines):  # Check if dialogue is over, next chapter
                        self.currPlayer.level = 6  # Proceed to next chapter
                        return "chp"
                
                    if not self.show_choices:
                            #if there is a next background index
                        if self.next_background_index:                  
                            self.current_scene_index = self.next_background_index
                            self.next_background_index = None
                        else:
                            self.current_scene_index += 1  # Proceed to the next background index
                       
                    self.draw_chapter5()  # Redraw dialogue.