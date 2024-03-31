import pygame
import sys
import os

from controller.constants import *

from view.components.button import Button
from view.components.slider import Slider
from view.components.choices import ChoicesScreen
from view.components.dialoguebox import DialogueBox
from view.screens.title import SceneTitle


class runGame:
    """ Private helper function to draw text on the screen """
    def _draw_text(self, text:str, font:sys, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Get the current display resolution
        self.infoObject = pygame.display.Info()
        self.screen_width = infoObject.current_w
        self.screen_height = infoObject.current_h
        
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Dating Simulator Ver. Western")

        # Load images
        path = os.path.join('view', 'assets', 'tower-thumb.jpg')
        background_image = pygame.image.load(path).convert()
        self.background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        path = os.path.join('view', 'assets', 'rectangle.png')
        grey_rectangle = pygame.image.load(path).convert()
        self.grey_rectangle = pygame.transform.scale(grey_rectangle, (screen_width // 4, screen_height ))
        path = os.path.join('view', 'assets', 'logo.png')
        logo = pygame.image.load(path).convert()
        self.logo = pygame.transform.scale(logo, (screen_width // 4, screen_height // 5))
        path = os.path.join('view', 'assets', 'title.png')
        title = pygame.image.load(path).convert()
        self.title = pygame.transform.scale(title, (screen_width // 4, screen_height // 4 - screen_height // 5))
        
        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GRAY = (192, 192, 192)
        DARK_GRAY = (132, 135, 140)
        LIGHT_GRAY = (234,234,234)

        # Font setup
        self.font = pygame.font.SysFont(None, 45)
        self.title_font = pygame.font.SysFont(None, 90)
        self.baby_font = pygame.font.SysFont(None, 20)

        #game variables
        self.menu_state = "main"

        # Main Menu Items
        self.menu_items = ["Start New Game", "Load Game", "Highscores", "Album","Settings", "Help", "Quit"]

        def draw_menu(menu_state: str) -> None:
            global show_choices
            global choices_made
            global current_dialogue_index
            global current_scene_index 
            show_choices = False
            if menu_state == "main":
                #Draw main menu screen
                self.screen.blit(background_image, (0, 0)) #draws background
                grey_rectangle.set_alpha(200) #sets transparency of the grey ractangle
                self.screen.blit(grey_rectangle, (0, screen_height // 5)) #draws the grey rectangle
                pygame.draw.rect(self.screen, BLACK, (0, screen_height // 4, screen_width // 4, screen_height - screen_height // 5), 4) #draws the border around the grey rectangle
                self.screen.blit(logo, (0, 0)) # draws the logo
                self.screen.blit(title, (0, screen_height // 5)) # draws the title
                pygame.draw.rect(self.screen, BLACK, (0, screen_height // 5, screen_width // 4, screen_height // 4 - screen_height // 5), 4) #draws the border around the title
                #draws out the menu screen
                for index, item in enumerate(self.menu_items):
                    menu_text = font.render(item, True, BLACK)
                    x = screen_width // 8 - (menu_text.get_width() // 2)
                    y = (screen_height // 2 - (menu_text.get_height() * len(self.menu_items) // 2) + (index * 75))
                    self.screen.blit(menu_text, (x, y))
                #write the names of our group
                message = baby_font.render("Created as a part of CS2212 at Western by Group 29", True, BLACK)
                self.screen.blit(message, (screen_width // 50, 39*screen_height//40))
                message2 = baby_font.render("Jasper, Aaron, Lecia, Ethan, Jasmine", True, BLACK)
                self.screen.blit(message2, (screen_width // 50, screen_height))
                pygame.display.flip()
                
            elif menu_state == "settings":
                self.screen.fill(DARK_GRAY)
                draw_text("Settings", title_font, BLACK, screen_width/20, screen_height/16 )
                controls_settings_button.draw(screen)
                sound_settings_button.draw(screen)
                video_settings_button.draw(screen)
                language_settings_button.draw(screen)
                accessibility_settings_button.draw(screen)
                account_settings_button.draw(screen)
                back_settings_button.draw(screen)
                back_controls_button.draw(screen)
                pygame.display.flip()  
                
            elif menu_state == "controls":
                screen.fill(DARK_GRAY)
                draw_text("Controls", title_font, BLACK, screen_width/20, screen_height/16 )
                draw_text("Click on a button, then press a key that is not binded", font, BLACK, screen_width/20, screen_height/16 + screen_height/14)
                auto_button.draw(screen)
                settings_button.draw(screen)
                pause_button.draw(screen)
                save_button.draw(screen)
                load_button.draw(screen)
                help_button.draw(screen)
                back_controls_button.draw(screen)
                pygame.display.flip()
                
            elif menu_state == "sound":
                screen.fill(DARK_GRAY)
                draw_text("Sound Settings", title_font, BLACK, screen_width/20, screen_height/16 )
                draw_text("Click on each bar to adjust the volume", font, BLACK, screen_width/20, screen_height/16 + screen_height/14)
                general_volume_slider.draw(screen)
                music_volume_slider.draw(screen)
                sfx_volume_slider.draw(screen)
                back_sound_button.draw(screen)
                pygame.display.flip()

            elif menu_state == 'help':
                screen.fill(LIGHT_GRAY)
                screen.blit(help1, (0, screen_height // 2 - help1.get_height() // 2))
                back_button.draw(screen)
                next_button.draw(screen)
                pygame.display.flip()
            
            elif menu_state == 'help2':
                screen.fill(LIGHT_GRAY)
                screen.blit(help2, (0, 0))
                back_to_help1_button.draw(screen)
                pygame.display.flip()
            

            elif menu_state == 'help':
                screen.fill(LIGHT_GRAY)
                screen.blit(help1, (0, screen_height // 2 - help1.get_height() // 2))
                back_button.draw(screen)
                next_button.draw(screen)
                pygame.display.flip()
            
            elif menu_state == 'help2':
                screen.fill(LIGHT_GRAY)
                screen.blit(help2, (0, 0))
                back_to_help1_button.draw(screen)
                pygame.display.flip()
            

            elif menu_state == "start":
                update_scene(current_scene_index)

            elif menu_state == "chp1":
                current_background = dialogue_background_images[current_dialogue_index]
                screen.blit(current_background, (0, 0))
                dialogue_box = DialogueBox(screen, font_size=50, box_height=200)
                dialogue_text = dialogue_lines[current_dialogue_index]  # Get current line of dialogue
                dialogue_box.draw(dialogue_text)
                pygame.display.flip()
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

        def update_scene(scene_index):
            global current_scene_index, current_dialogue_index
            current_scene_index = scene_index
                
            # Reset dialogue index ??? Can set the dialogue back to 0 everytime there is a new scene 
            # current_dialogue_index = 0  
            pygame.display.set_caption(scene_titles[current_scene_index])  
            scene_title = SceneTitle(screen, scene_titles[current_scene_index] )
            scene_title.draw()
            pygame.display.flip()
            
        def main_menu(menu_state, controls_keys):
            global current_dialogue_index
            menu_active = True
            while menu_active:  
                #checks for the actions of the player
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if show_choices:
                        choices = ["Yes", "No"]  # Example choices
                        choice_screen = ChoicesScreen(screen, choices)
                        choice_screen.display()  # Display the choices screen
                        selected_choice = choice_screen.get_selected_choice()
                        if selected_choice is not None:
                            print(f"Player selected: {choices[selected_choice]}")
                            # Handle the choice here (e.g., modify game state based on the selection)
                            showing_choices = False  # Reset the flag after handling the choice
                        
                        
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                            menu_active = False
                            
                    if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mouse click is within the bounds of any menu item
                        if menu_state == "main":
                            for index, item in enumerate(menu_items):
                                menu_text = font.render(item, True, BLACK)
                                x = screen_width // 8 - (menu_text.get_width() // 2)
                                y = (screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 75))
                                item_rect = menu_text.get_rect(topleft=(x, y))
                                if item_rect.collidepoint(event.pos):
                                    click_sfx.play()
                                    menu_state = menu_click(index)
                        
                        #Settings buttons            
                        elif menu_state == "settings":
                            if controls_settings_button.draw(screen):
                                click_sfx.play()
                                menu_state = controls_settings_button.draw(screen)
                            elif sound_settings_button.draw(screen):
                                click_sfx.play()
                                menu_state = sound_settings_button.draw(screen)
                            elif video_settings_button.draw(screen):
                                click_sfx.play()
                                menu_state = video_settings_button.draw(screen)
                            elif language_settings_button.draw(screen):
                                click_sfx.play()
                                menu_state = language_settings_button.draw(screen)
                            elif accessibility_settings_button.draw(screen):
                                click_sfx.play()
                                menu_state = accessibility_settings_button.draw(screen)
                            elif account_settings_button.draw(screen):
                                click_sfx.play()
                                menu_state = account_settings_button.draw(screen)
                            elif back_settings_button.draw(screen):
                                click_sfx.play()
                                menu_state = back_settings_button.draw(screen)
                        
                        #Controls_buttons
                        elif menu_state == "controls":
                            if auto_button.draw(screen):
                                click_sfx.play()
                                key_pressed = False
                                while key_pressed == False:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key not in controls_keys.values():
                                                # Assign the pygame key to the action in the keys dict.
                                                controls_keys["auto_key"] = event.key
                                                auto_button.updateText("Auto: " + chr(event.key))
                                                key_pressed = True  

                            elif settings_button.draw(screen):
                                click_sfx.play()
                                key_pressed = False
                                while key_pressed == False:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key not in controls_keys.keys():
                                                # Assign the pygame key to the action in the keys dict.
                                                controls_keys["settings_key"] = event.key
                                                settings_button.updateText("Settings: " + chr(event.key))
                                                key_pressed = True
                                            
                            elif pause_button.draw(screen):
                                click_sfx.play()
                                key_pressed = False
                                while key_pressed == False:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key not in controls_keys.keys():
                                                # Assign the pygame key to the action in the keys dict.
                                                controls_keys["pause_key"] = event.key
                                                pause_button.updateText("Pause: " + chr(event.key))
                                                key_pressed = True
                                            
                            elif save_button.draw(screen):
                                click_sfx.play()
                                key_pressed = False
                                while key_pressed == False:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key not in controls_keys.keys():
                                                # Assign the pygame key to the action in the keys dict.
                                                controls_keys["save_key"] = event.key
                                                save_button.updateText("Save: " + chr(event.key))
                                                key_pressed = True
                                            
                            elif load_button.draw(screen):
                                click_sfx.play()
                                key_pressed = False
                                while key_pressed == False:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key not in controls_keys.keys():
                                                # Assign the pygame key to the action in the keys dict.
                                                controls_keys["load_key"] = event.key
                                                load_button.updateText("Load: " + chr(event.key))
                                                key_pressed = True
                                            
                            elif help_button.draw(screen):
                                click_sfx.play()
                                key_pressed = False
                                while key_pressed == False:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key not in controls_keys.keys():
                                                # Assign the pygame key to the action in the keys dict.
                                                controls_keys["help_key"] = event.key
                                                help_button.updateText("Help: " + chr(event.key))
                                                key_pressed = True
                                            
                            elif back_controls_button.draw(screen):
                                click_sfx.play()
                                menu_state = back_controls_button.draw(screen)
                        
                        #sound settings
                        elif menu_state == "sound":
                            click_sfx.play()
                            mouse_pos = pygame.mouse.get_pos()
                            mouse = pygame.mouse.get_pressed()

                            if general_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                                general_volume_slider.move_slider(mouse_pos)
                                general_volume_slider.updateText()
                                click_sfx.set_volume(round((general_volume_slider.get_value()/100) * (sfx_volume_slider.get_value()/100),1))
                            general_volume_slider.draw(screen)

                            if music_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                                music_volume_slider.move_slider(mouse_pos)
                                music_volume_slider.updateText()
                                #add set volume function once music is added
                            general_volume_slider.draw(screen)

                            if sfx_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                                sfx_volume_slider.move_slider(mouse_pos)
                                sfx_volume_slider.updateText()
                                click_sfx.set_volume(round((general_volume_slider.get_value()/100) * (sfx_volume_slider.get_value()/100),1))
                            general_volume_slider.draw(screen)


                            if back_sound_button.draw(screen):
                                click_sfx.play()
                                menu_state = back_sound_button.draw(screen)

                        elif menu_state == "start":
                            click_sfx.play()
                            # Listen for a click to switch to DialogueBox
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                # Here you change the state to display the dialogue box
                                menu_state = "chp1"

                        elif menu_state == "chp1":
                            click_sfx.play()
                            current_dialogue_index += 1  # Move to the next dialogue line
                            if current_dialogue_index >= len(dialogue_lines):  # Loop or end dialogue
                                current_dialogue_index = 0  # Reset index or change state as needed

                        #help menu page 1
                        elif menu_state == "help":
                            if back_button.draw(screen):
                                click_sfx.play()
                                menu_state = back_button.draw(screen)
                            elif next_button.draw(screen):
                                click_sfx.play()
                                menu_state = next_button.draw(screen)

                        #help menu page 2
                        elif menu_state == "help2":
                            if back_to_help1_button.draw(screen):
                                click_sfx.play()
                                menu_state = back_to_help1_button.draw(screen)
                
                draw_menu(menu_state)

        def menu_click(index):
            # This function handles the menu clicks
            if index == 0:
                menu_state = "start"
                return menu_state
            elif index == 1:
                menu_state = "load"
                return menu_state
            #takes you to the highscores table
            elif index == 2:
                menu_state = "highscores"
                return menu_state
            #takes you to the albums
            elif index == 3:
                menu_state = "album"
                return menu_state
            #takes you to settings
            elif index == 4:
                menu_state = "settings"
                return menu_state
            #takes you to help menu
            elif index == 5:
                menu_state = "help"
                return menu_state
            #quits the game
            elif index == 6:
                pygame.quit()
                sys.exit()


        # Call the main menu
        main_menu(menu_state,controls_keys)




