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


class Chapter2(Chapter):
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str], controls: dict):
        super().__init__(2, screen, currPlayer, dialogueLines, dialogueImagePaths, controls)

        self.show_choices: bool = False
        self.choices_made: dict = {}
        self.current_dialogue_index: int = 0
        self.current_scene_index: int = 0

        self.dialogue_options = {
            2: ["Ask about her interests", "Ask about her background", "Scroll on your phone"],
            3: ["Yeah that sounds great", "Sorry, I might be a little busy"]
        }

        self.dialogue_responses = {
            "Ask about her interests": ("S: Thanks for asking! Music is one of my favourite ways to pass time. I’ve been competing in piano contests since I was young! I also love to draw...wait I can draw a picture of you!", 3),
            "Ask about her background": ("S: I grew up in Markham actually. I was never a sports kid and I did a lot of Olympiads and Kumon growing up. I always did like art though. I can draw a picture of you!", 4),
            "Scroll on your phone": ("S: Oh! I have an idea. As thanks for helping me get my sheet music back, I can draw a picture of you!", 5),
            "Yeah that sounds great": ("S: Sounds good! Let’s meet at my place tomorrow at 1pm!", 6),
            "Sorry, I might be a little busy": ("S: Don’t worry... it won’t take long. I’ll see you tomorrow at 1pm, my place okay?", 7)
        }

        self.draw_chapter2()

    def draw_chapter2(self):
        while True:
            current_background = self.dialogueImages[self.current_dialogue_index]
            self.screen.blit(current_background, (0, 0))
            dialogue_box = DialogueBox(self.screen, font_size=50, box_height=200)
            dialogue_text = self.dialogueLines[self.current_dialogue_index]
            dialogue_box.draw(dialogue_text)

            if self.current_dialogue_index in self.dialogue_options and not self.show_choices:
                # Dialogue options are available for this index
                self.show_choices = True
                choices_screen = ChoicesScreen(self.screen, self.dialogue_options[self.current_dialogue_index])
                selected_choice_index = choices_screen.display()

                if selected_choice_index is not None:
                    selected_option_text = self.dialogue_options[self.current_dialogue_index][selected_choice_index]
                    response_text, background_index = self.dialogue_responses[selected_option_text]

                    self.choices_made[self.current_dialogue_index] = selected_option_text
                    self.dialogueLines[self.current_dialogue_index] = response_text
                    self.current_scene_index = background_index

                    self.show_choices = False

                    self.current_dialogue_index += 1

                    # After updating indices, get the new background and draw it
                    current_background = self.dialogueImages[self.current_scene_index]
                    self.screen.blit(current_background, (0, 0))


            dialogue_box.draw(dialogue_text)
            pygame.display.flip()
            self.event_handler()

    def event_handler(self):
        while True:
            for event in pygame.event.get():
                self.checkQuitGame(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.current_dialogue_index in self.dialogue_options:
                        # Check if we need to show choices
                        if self.current_dialogue_index == 3 and not self.show_choices:
                            choices_screen = ChoicesScreen(self.screen, self.dialogue_options[2])
                            selected_choice_index = choices_screen.display()
                            self.show_choices = True

                            if selected_choice_index is not None:
                                self.currPlayer.level = 3  # Proceed to next chapter
                                return "chp"

                    else:
                        if self.current_dialogue_index >= len(self.dialogueLines):  # Check if dialogue is over
                            self.current_dialogue_index = 0  # Reset or move to next scene
                        elif self.current_dialogue_index < len(self.dialogueLines):
                            self.current_dialogue_index += 1  # Proceed to the next line of dialogue
                self.draw_chapter2()  # Redraw dialogue