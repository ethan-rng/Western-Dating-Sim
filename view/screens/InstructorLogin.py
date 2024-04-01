import pygame, os
from controller.constants import *
from view.components.Button import Button
from view.components.InputBox import TextInputBox
from models.Instructor import Instructor
from models.exceptions import *
from hashlib import sha256


class InstructorLogin:
    def __init__(self) -> None:
        self.game_state = "instructor_login"
        self.username = ''
        self.password = ''
        self.continue_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Continue", WHITE, "instructor_panel", pygame)
        self.username_input_box = TextInputBox(screen_width//11.5, screen_height//5, screen_width, screen_height/20, "Username:", DARK_GRAY, pygame)
        self.password_input_box = TextInputBox(screen_width//11.5, screen_height//5 + screen_height//10, screen_width, screen_height/20, "Password:", DARK_GRAY, pygame)
        self.error_message: str = ""
        self.back_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3.7, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)


        
    def draw_login(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.draw_text("Login", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.continue_button.draw(screen)
        self.username_input_box.draw(screen)
        self.password_input_box.draw(screen)
        self.back_button.draw(screen)
        
        # Drawing Error Message For any errors 
        if self.error_message:
            error_font = pygame.font.SysFont(None, 80)
            text_surface = error_font.render(self.error_message, True, RED)
            # Calculate x position to center the text
            text_x = (screen_width - text_surface.get_width()) / 2
            text_y = (screen_height * 9) / 13
            screen.blit(text_surface, (text_x, text_y))
            
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
                        click_sfx.play()
                        if not self.username == '' and not self.password == '':
                            if self.username == "instructor":
                                if self.password == "12345":
                                    self.game_state = self.continue_button.draw(screen)
                                    return self.game_state
                                else:
                                    self.error_message = "You entered the wrong password"
                        else:
                            self.error_message = "Please enter a value into the username or password box"
                                    
                    elif self.back_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.back_button.draw(screen)
                        return self.game_state
                                    
                                
                                
            self.draw_login(screen)
    
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))
