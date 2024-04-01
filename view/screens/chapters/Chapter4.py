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


class Chapter4(Chapter):
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):
        super().__init__(4, screen, currPlayer, dialogueLines, dialogueImagePaths, controls)

        self.show_choices: bool = False
        self.choices_made: dict = {}
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0
        self.selected_choice_index = None
        self.next_background_index: int = None
        
        self.dialogue_options = {
            1: ["Tuxedo", "Casual Sweats", "Semi-Formal", "Pajamas"],
            3: ["Flowers", "Plushie", "Nothing"],
            5: ["Yes",  "No", "Split the Bill"],
            6: ["Yeah me too, it was fun.", "It was ok, I guess.", "I had a great time, you wanna do this again?"],
            8: ["I really enjoyed our time today! I was wondering if you'd be free tomorrow to grab dinner?", "Let's go out tomorrow for dinner. Just the two of us.", "Thanks for today. It was fun. Let's do this again.", "You're actually interesting. Let’s go out again.", "Yo homie, You wanna do this again?"]
        }

        self.dialogue_responses = {
            "Tuxedo": ("Looks too formal for a boba date. (-5 Points)", 1,3),
            "Casual Sweats": ("Perfect for a relaxed vibe. (+5 Points)", 1,3),
            "Semi-Formal": ("A nice balance, not too casual. (+3 Points)", 1,3),
            "Pajamas": ("A bit too informal, even for a chill date. (-3 Points)", 1,3),
            "Flowers": ("A sweet and traditional gesture. (+5 Points)", 3,4),
            "Plushie": ("Adorable and personal, a great choice. (+10 Points)", 3,4),
            "Nothing": ("It's okay, but a little effort goes a long way. (0 Points)", 3,4),
            "Yes": ("S: Thank you so much! I’ll get the next one!", 5,6),
            "No": ("S: Oh... okay", 5,7),
            "Split the Bill": ("S: Yeah sounds good", 5,8),
            "I had a great time, you wanna do this again?": ("S: Yeah for sure!", 9,13),
            "It was ok, I guess.": ("S: Haha.... ", 9,12),
            "Yeah me too, it was fun.": ("S: I'm glad. ", 9,11),
        }
        
        self.draw_chapter4()

    def draw_chapter4(self):
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
                        self.currPlayer.level = 5  # Proceed to next chapter
                        return "chp"
                
                    if not self.show_choices:
                            #if there is a next background index
                        if self.next_background_index:                  
                            self.current_scene_index = self.next_background_index
                            self.next_background_index = None
                        else:
                            self.current_scene_index += 1  # Proceed to the next background index
                       
                    self.draw_chapter4()  # Redraw dialogue.