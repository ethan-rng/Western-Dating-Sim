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
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):
        super().__init__(6, screen, currPlayer, dialogueLines, dialogueImagePaths, controls)

        self.show_choices: bool = False
        self.choices_made: dict = {}
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0
        self.selected_choice_index = None
        self.next_background_index: int = None
        
        self.dialogue_options = {
            2: ["Ask about her interests", "Ask about her background", "Scroll on your phone"],
            4: ["Yeah that sounds great", "Sorry, I might be a little busy"]
        }

        self.dialogue_responses = {
            "Ask about her interests": ("S: Thanks for asking! Music is one of my favourite ways to pass time. I’ve been competing in piano contests since I was young! I also love to draw...wait I can draw a picture of you!", 3,6),
            "Ask about her background": ("S: I grew up in Markham actually. I was never a sports kid and I did a lot of Olympiads and Kumon growing up. I always did like art though. I can draw a picture of you!", 4,6),
            "Scroll on your phone": ("S: *Silence*", 5,6),
            "Yeah that sounds great": ("S: Sounds good!", 7,9),
            "Sorry, I might be a little busy": ("S: Don’t worry... it won’t take long. ", 8,9)
        }
        
        self.draw_chapter6()

    def draw_chapter6(self):
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
                    if self.current_dialogue_index >= len(self.dialogueLines)-1:  # Check if dialogue is over, next chapter
                        self.currPlayer.level = 1  # Proceed to main menu
                        return "menu"
                
                    if not self.show_choices:
                            #if there is a next background index
                        if self.next_background_index:                  
                            self.current_scene_index = self.next_background_index
                            self.next_background_index = None
                        else:
                            self.current_scene_index += 1  # Proceed to the next background index
                       
                    self.draw_chapter6()  # Redraw dialogue.