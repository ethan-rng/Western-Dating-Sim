from controller.constants import *
import pygame
import sys
from view.components.Button import Button
from view.components.Slider import Slider

class SettingsSound:
    """
    Class representing the sound settings view in the game.

    Attributes:
    :game_state: String representing the state of the sound settings menu.
    :general_volume_slider: Slider object representing the slider for adjusting the general volume.
    :music_volume_slider: Slider object representing the slider for adjusting the music volume.
    :sfx_volume_slider: Slider object representing the slider for adjusting the sound effects volume.
    :back_sound_button: Button object representing the button to go back to the settings menu.
    """

    def __init__(self) -> None:
        """
        Initialize the SettingsSound object.
        """
        self.game_state = "sound"
        
        # Sound settings variables
        self.general_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4), (screen_width/1.8,20), "Game Volume", 0.52, 0, 100)
        self.music_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + screen_height//6), (screen_width/1.8,20), "Music Volume", 0.52, 0, 100)
        self.sfx_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + (screen_height//6 *2)), (screen_width/1.8,20), "SFX Volume", 0.52, 0, 100)
        self.back_sound_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)
    
    def draw_settings_sound(self, screen:pygame.Surface) -> None:
        """
        Draw the sound settings view on the screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        screen.fill(DARK_GRAY)
        self.draw_text("Sound Settings", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.draw_text("Click on each bar to adjust the volume", font, BLACK, screen_width/20, screen_height/16 + screen_height/14, screen)
        self.general_volume_slider.draw(screen)
        self.music_volume_slider.draw(screen)
        self.sfx_volume_slider.draw(screen)
        self.back_sound_button.draw(screen)
        pygame.display.flip()
        
    def event_handler(self, screen: pygame.Surface) -> None:
        """
        Handle events in the sound settings view.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        settings_sound_active = True
        while settings_sound_active:
            # Checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        settings_sound_active = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_sfx.play()
                    mouse_pos = pygame.mouse.get_pos()
                    mouse = pygame.mouse.get_pressed()

                    if self.general_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.general_volume_slider.moveSlider(mouse_pos)
                        self.general_volume_slider.updateText()
                        click_sfx.set_volume(round((self.general_volume_slider.getValue()/100) * (self.sfx_volume_slider.getValue()/100),1))
                    self.general_volume_slider.draw(screen)

                    if self.music_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.music_volume_slider.moveSlider(mouse_pos)
                        self.music_volume_slider.updateText()
                        pygame.mixer.music.set_volume(self.music_volume_slider.getValue()/100)
                    self.music_volume_slider.draw(screen)

                    if self.sfx_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.sfx_volume_slider.moveSlider(mouse_pos)
                        self.sfx_volume_slider.updateText()
                        click_sfx.set_volume(round((self.general_volume_slider.getValue()/100) * (self.sfx_volume_slider.getValue()/100),1))
                    self.sfx_volume_slider.draw(screen)

                    if self.back_sound_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.back_sound_button.draw(screen)
                        return self.game_state
            
            self.draw_settings_sound(screen)
    
    """ Helper function to draw text on the screen """
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
