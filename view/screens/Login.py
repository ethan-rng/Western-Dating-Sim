from typing import Tuple, Any

import pygame, sys
from controller.constants import *
from view.components.Button import Button
from view.components.InputBox import TextInputBox
from models.exceptions import *
from controller.constants import *
from models.Player import Player
from models.Developer import Developer


class Login:
    def __init__(self) -> None:
        self.game_state = "login"
        self.username = ''
        self.password = ''
        self.continue_button = Button(screen_width / 2.48, (screen_height / 3) + (screen_height / 6) * 3,
                                      (screen_width / 4), (screen_height / 13), "Continue", WHITE, "start", pygame)
        self.username_input_box = TextInputBox(screen_width // 11.5, screen_height // 5, screen_width,
                                               screen_height / 20, "Username:", DARK_GRAY, pygame)
        self.password_input_box = TextInputBox(screen_width // 11.5, screen_height // 5 + screen_height // 8,
                                               screen_width, screen_height / 20, "Password:", DARK_GRAY, pygame)
        self.error_message = ""
        
        self.back_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3.7, (screen_width/4), (screen_height/13), "Back", WHITE, "main", pygame)


    def draw_login(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.draw_text("Login", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.continue_button.draw(screen)
        self.username_input_box.draw(screen)
        self.password_input_box.draw(screen)
        self.back_button.draw(screen)

        if self.error_message:
            font = pygame.font.SysFont(None, 80)
            text_surface = font.render(self.error_message, True, RED)
            # Calculate x position to center the text
            text_x = (screen_width - text_surface.get_width()) / 2
            text_y = (screen_height * 6) / 13
            screen.blit(text_surface, (text_x, text_y))
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface, currPlayer: Player, isLogin: bool) -> tuple[str, str, str] | str:
        newgame_active = True

        while newgame_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
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
                    
                    elif self.back_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.back_button.draw(screen)
                        return self.game_state, self.username, self.password

                    elif self.continue_button.draw(screen):
                        click_sfx.play()
                        if not self.username == '' and not self.password == '':
                            try:
                                if isLogin:
                                    # Developer
                                    if self.username == "developer":
                                        currPlayer: Developer = Developer(self.password)
                                    # Normal Player
                                    else:
                                        currPlayer.loadPlayer(self.username)
                                        currPlayer.login(self.username, self.password)

                                    self.game_state = "chp"
                                    return self.game_state, self.username, self.password
                                else:
                                    if currPlayer.userExists(self.username):
                                        raise DuplicateUser(self.username)

                                    self.game_state = self.continue_button.draw(screen)
                                    self.error_message = ""  # Clear the error message on successful action
                                    return self.game_state, self.username, self.password

                            except DuplicateUser:
                                self.error_message = "Please Pick A Username That Hasn't Been Picked"

                            except IncorrectPassword:
                                self.error_message = "Wrong Password For This User"

                            except UserNotFound:
                                self.error_message = "A User With This Username Doesn't Exist"

                        else:
                            self.error_message = "Please Fill In An Username and A Password"

            self.draw_login(screen)
        return "chp"
        
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))

        
