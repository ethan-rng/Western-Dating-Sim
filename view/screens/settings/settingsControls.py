from controller.constants import *
import pygame
import sys
from view.components.Button import Button

class SettingsControls:
    
    def __init__(self) -> None:
        
        self.menu_state = "controls"
        
        #controls settings variables
        self.controls_keys = {"auto_key": pygame.K_g, "settings_key": pygame.K_t, "pause_key": pygame.K_p, "save_key": pygame.K_s, "load_key": pygame.K_l, "help_key": pygame.K_h}

        #load controls settings buttons
        self.auto_button = Button(screen_width/5.4, screen_height/3, (screen_width/4), (screen_height/13), "Auto: " + chr(self.controls_keys["auto_key"]), WHITE, "controls", pygame)
        self.settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) , (screen_width/4), (screen_height/13), "Settings: " + chr(self.controls_keys["settings_key"]), WHITE, "sound", pygame)
        self.pause_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Pause: " + chr(self.controls_keys["pause_key"]), WHITE, "video", pygame)
        self.save_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Save: " + chr(self.controls_keys["save_key"]), WHITE, "language", pygame)
        self.load_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Load: " + chr(self.controls_keys["load_key"]), WHITE, "accessibility", pygame)
        self.help_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Help: " + chr(self.controls_keys["help_key"]), WHITE, "account", pygame)
        self.back_controls_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)    
    
    def draw_settings_controls(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.draw_text("Controls", title_font, BLACK, screen_width/20, screen_height/16, screen )
        self.draw_text("Click on a button, then press a key that is not binded", font, BLACK, screen_width/20, screen_height/16 + screen_height/14, screen)
        self.auto_button.draw(screen)
        self.settings_button.draw(screen)
        self.pause_button.draw(screen)
        self.save_button.draw(screen)
        self.load_button.draw(screen)
        self.help_button.draw(screen)
        self.back_controls_button.draw(screen)
        pygame.display.flip()
        
    
    def event_handler(self, screen: pygame.Surface) -> str:
        settings_control_active = True
        while settings_control_active:
            #checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        settings_control_active = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.auto_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in self.controls_keys.values():
                                        # Assign the pygame key to the action in the keys dict.
                                        self.controls_keys["auto_key"] = event.key
                                        self.auto_button.updateText("Auto: " + chr(event.key))
                                        key_pressed = True  

                    elif self.settings_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in self.controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        self.controls_keys["settings_key"] = event.key
                                        self.settings_button.updateText("Settings: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif self.pause_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in self.controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        self.controls_keys["pause_key"] = event.key
                                        self.pause_button.updateText("Pause: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif self.save_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in self.controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        self.controls_keys["save_key"] = event.key
                                        self.save_button.updateText("Save: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif self.load_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in self.controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        self.controls_keys["load_key"] = event.key
                                        self.load_button.updateText("Load: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif self.help_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in self.controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        self.controls_keys["help_key"] = event.key
                                        self.help_button.updateText("Help: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif self.back_controls_button.draw(screen):
                        click_sfx.play()
                        self.menu_state = self.back_controls_button.draw(screen)
                        return self.menu_state
                    
            self.draw_settings_controls(screen)
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))