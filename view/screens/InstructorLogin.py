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
        
    def draw_login(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.draw_text("Login", title_font, BLACK, screen_width/20, screen_height/16, screen)
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
                        click_sfx.play()
                        if not self.username == '' and not self.password == '':
                            if self.username == "instructor":
                                try:
                                    instructor: Instructor = Instructor(self.password)
                                except IncorrectPassword:
                                    IncorrectPassword(self.username, self.password)
                                except IncorrectPrivilege:
                                    IncorrectPrivilege()
                                else:
                                    self.game_state = self.continue_button.draw(screen)
                                    return self.game_state
                                
                                
            self.draw_login(screen)
    
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))
