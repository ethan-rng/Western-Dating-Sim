import pygame, os
from controller.constants import *
from view.components.Button import Button
from view.components.InputBox import TextInputBox

class Login:
    def __init__(self) -> None:
        self.menu_state = "login"
        self.username = ''
        self.password = ''
        self.continue_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Continue", WHITE, "start", pygame)
        self.username_input_box = TextInputBox(screen_width//11.5, screen_height//5, screen_width, screen_height/20, "Username:", DARK_GRAY, pygame)
        self.password_input_box = TextInputBox(screen_width//11.5, screen_height//5+screen_height//8, screen_width, screen_height/20, "Password:", DARK_GRAY, pygame)
        
    def draw_login(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.continue_button.draw(screen)
        self.username_input_box.draw(screen)
        self.password_input_box.draw(screen)
        pygame.display.flip()
        
    def event_handler(self, screen: pygame.Surface) -> None:
        newgame_active = True
        while newgame_active:  
            #checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        newgame_active = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.username_input_box.draw(screen):
                        click_sfx.play()
                        self.username_input_box.event_handler(screen)
                        self.username = self.username_input_box.user_text
                    
                    elif self.password_input_box.draw(screen):
                        click_sfx.play()
                        self.password_input_box.event_handler(screen)
                        self.password = self.password_input_box.user_text
                        
                    elif self.continue_button.draw(screen):
                        
                        if not self.username == '':
                            if not self.password == '':
                                self.menu_state = self.continue_button.draw(screen)
                                return self.menu_state 
            self.draw_login(screen)
        