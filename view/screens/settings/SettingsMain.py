from controller.constants import *
import pygame
import sys
from view.components.Button import Button

class SettingsMain:
    """
    Class representing the main settings view in the game.

    Attributes:
    :game_state: String representing the state of the settings menu.
    :controls_settings_button: Button object representing the button for accessing controls settings.
    :sound_settings_button: Button object representing the button for accessing sound settings.
    :video_settings_button: Button object representing the button for accessing video settings.
    :language_settings_button: Button object representing the button for accessing language settings.
    :accessibility_settings_button: Button object representing the button for accessing accessibility settings.
    :back_settings_button: Button object representing the button to go back to the main menu.
    """

    def __init__(self) -> None:
        """
        Initialize the SettingsMain object.
        """
        self.game_state = "settings"
        
        # Load main settings buttons
        self.controls_settings_button = Button(screen_width/5.4, screen_height/3, (screen_width/4), (screen_height/13), "Controls", WHITE, "controls", pygame)
        self.sound_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) , (screen_width/4), (screen_height/13), "Sound Settings", WHITE, "sound", pygame)
        self.video_settings_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Video Settings", WHITE, "videosettings", pygame)
        self.language_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Language", WHITE, "language", pygame)
        self.accessibility_settings_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Instructor Login", WHITE, "instructor_login", pygame)
        self.back_settings_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "main", pygame)

    def draw_settings_main(self, screen: pygame.Surface) -> None:
        """
        Draw the main settings view on the screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        screen.fill(DARK_GRAY)
        self.draw_text("Settings", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.controls_settings_button.draw(screen)
        self.sound_settings_button.draw(screen)
        self.video_settings_button.draw(screen)
        self.language_settings_button.draw(screen)
        self.accessibility_settings_button.draw(screen)
        self.back_settings_button.draw(screen)
        pygame.display.flip()
        
    def event_handler(self, screen:pygame.Surface) -> str: 
        """
        Handle events in the main settings view.

        Parameters:
        :screen: Pygame surface object representing the game screen.

        """
        settings_main_active = True
        while settings_main_active:
            # Checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        settings_main_active = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.controls_settings_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.controls_settings_button.draw(screen)
                        return self.game_state
                    elif self.sound_settings_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.sound_settings_button.draw(screen)
                        return self.game_state
                    elif self.video_settings_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.video_settings_button.draw(screen)
                        return self.game_state
                    elif self.language_settings_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.language_settings_button.draw(screen)
                        return self.game_state
                    elif self.accessibility_settings_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.accessibility_settings_button.draw(screen)
                        return self.game_state
                    elif self.back_settings_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.back_settings_button.draw(screen) 
                        return self.game_state
                    
            self.draw_settings_main(screen)
    
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface) -> None:
        """
        Draw text on the screen.

        Parameters:
        :text: String representing the text to be drawn.
        :font: Pygame font object representing the font style.
        :text_col: Tuple representing the color of the text.
        :x: Float representing the x-coordinate of the text.
        :y: Float representing the y-coordinate of the text.
        :screen: Pygame surface object representing the game screen.
        """
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y)) 
