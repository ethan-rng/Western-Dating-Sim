from view.screens.chapters.Chapter import Chapter
from view.components.dialoguebox import DialogueBox
import 
import pygame

class Chapter1(Chapter):
    def __init__(self, screen: pygame.Surface, currPlayer: Player,
                 title: str, dialogueLines: List[str], dialogueImagePaths: List[str]):
        
        super().__init__(1, screen, currPlayer, "Chapter 1", dialogueLines, dialogueImagePaths)
        self.draw()

    def draw(self):
        current_background = dialogue_background_images[current_dialogue_index]
        screen.blit(current_background, (0, 0))
        dialogue_box = DialogueBox(screen, font_size=50, box_height=200)
        dialogue_text = dialogue_lines[current_dialogue_index]  # Get current line of dialogue
        dialogue_box.draw(dialogue_text)
        pygame.display.flip()


        # Fifth Scene 
        if current_dialogue_index == 5 and not show_choices:
            choices_screen = ChoicesScreen(screen, ["Yes", "No"])
            selected_choice_index = choices_screen.display()  # Display choices and get selected option
            show_choices = True  # Avoid displaying choices again if we're still on this dialogue point
            choices_made[current_dialogue_index] = selected_choice_index  # Remember the choice made
        
            # Logic to set the next dialogue index based on the choice
            if selected_choice_index is not None:
                if selected_choice_index == 0:
                    current_scene_index += 1
                    update_scene(current_scene_index)
                if selected_choice_index == 1:
                    # For example, choosing the first option might skip to another dialogue point
                    current_dialogue_index = 0
         
            show_choices = False  # Reset for the next time choices need to be displayed

            pygame.display.flip()



