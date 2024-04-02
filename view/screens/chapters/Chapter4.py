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
            7: ["I really enjoyed our time today! I was wondering if you'd be free tomorrow to grab dinner?", "Let's go out tomorrow for dinner. Just the two of us.", "You're actually interesting. Let’s go out again.", "Yo homie, You wanna do this again?"]
        }

        self.dialogue_responses = {
            "Tuxedo": ("Looks too formal for a boba date. (-5 Points)", 1,2),
            "Casual Sweats": ("Perfect for a relaxed vibe. (+5 Points)", 1,2),
            "Semi-Formal": ("A nice balance, not too casual. (+3 Points)", 1,2),
            "Pajamas": ("A bit too informal, even for a chill date. (-3 Points)", 1,2),
            "Flowers": ("A sweet and traditional gesture. (+5 Points)", 1,4),
            "Plushie": ("Adorable and personal, a great choice. (+10 Points)", 1,4),
            "Nothing": ("It's okay, but a little effort goes a long way. (0 Points)", 1,4),
            "Yes": ("S: Thank you so much! I’ll get the next one! [Shows you're thoughtful. (+5 Points)]", 6,9),
            "No": ("S: Oh... okay [Not the best move on a first date. (-5 Points)]", 7,9),
            "Split the Bill": ("S: Yeah sounds good [Fair and respectful. (0 Points)]", 8,9),
            "I had a great time, you wanna do this again?": ("S: Yeah for sure! [Shows interest and opens the door for another date. (+5 Points)]", 12,14),
            "It was ok, I guess.": ("S: Haha.... [Not very enthusiastic. (-5 Points)]", 10,14),
            "Yeah me too, it was fun.": ("S: I'm glad. [ Neutral, but positive. (0 Points)]", 11,14),
            "I really enjoyed our time today! I was wondering if you'd be free tomorrow to grab dinner?": ("Showing keen interest. (+5 Points)", 14, 15),
            "Let's go out tomorrow for dinner. Just the two of us.": ("Direct, but a bit presumptuous. (0 Points)", 14, 15),
            "You're actually interesting. Let’s go out again.": ("A backhanded compliment. (-3 Points)", 14, 15),
            "Yo homie, You wanna do this again?": ("Too casual and might come off as insincere. (-10 Points)", 14, 15)
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
                click_sfx.play()
                self.checkQuitGame(event)
                if event.type == pygame.MOUSEBUTTONDOWN:            

                    self.current_dialogue_index += 1 
                    if self.current_dialogue_index >= len(self.dialogueLines)-1:  # Check if dialogue is over, next chapter

                        # Calculating Player's Score This Chapter and Updating It
                        for choice in self.choices_made.values():
                            if choice == "Tuxedo":
                                self.currPlayer.updateStats("Serena", -5)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "Casual Sweats":
                                self.currPlayer.updateStats("Serena", 5)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "Semi-Formal":
                                self.currPlayer.updateStats("Serena", 3)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "Pajamas":
                                self.currPlayer.updateStats("Serena", -3)
                                print(self.currPlayer.attractionScore["Serena"])
                            elif choice == "Flowers":
                                self.currPlayer.updateStats("Serena", 5)
                            elif choice == "Plushie":
                                self.currPlayer.updateStats("Serena", 10)
                            elif choice == "Nothing":
                                self.currPlayer.updateStats("Serena", 0)
                            elif choice == "Yes":
                                self.currPlayer.updateStats("Serena", 5)
                            elif choice == "No":
                                self.currPlayer.updateStats("Serena", -5)
                            elif choice == "Split the Bill":
                                self.currPlayer.updateStats("Serena", 0)
                            elif choice == "I had a great time, you wanna do this again?":
                                self.currPlayer.updateStats("Serena", 5)
                            elif choice == "It was ok, I guess.":
                                self.currPlayer.updateStats("Serena", -5)
                            elif choice == "Yeah me too, it was fun.":
                                self.currPlayer.updateStats("Serena", 0)
                            elif choice == "I really enjoyed our time today! I was wondering if you'd be free tomorrow to grab dinner?":
                                self.currPlayer.updateStats("Serena", 5)
                            elif choice == "Let's go out tomorrow for dinner. Just the two of us.":
                                self.currPlayer.updateStats("Serena", 0)
                            elif choice == "You're actually interesting. Let’s go out again.":
                                self.currPlayer.updateStats("Serena", -3)
                            elif choice == "Yo homie, You wanna do this again?":
                                self.currPlayer.updateStats("Serena", -10)
                            else:
                                raise Exception("Choice Isn't Valid")
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