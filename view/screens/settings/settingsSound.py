from controller.constants import *
import pygame
import sys
from view.components.button import Button
from view.components.slider import Slider

class SettingsSound:
    def __init__(self) -> None:
        
        self.menu_state = "sound"
        
        #sound settings variables
        self.general_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4), (screen_width/1.8,20), "Game Volume", 0.5, 0, 100)
        self.music_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + screen_height//6), (screen_width/1.8,20), "Music Volume", 0.5, 0, 100)
        self.sfx_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + (screen_height//6 *2)), (screen_width/1.8,20), "SFX Volume", 0.5, 0, 100)
        self.back_sound_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)
    
    def draw_settings_sound(self, screen:pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.draw_text("Sound Settings", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.draw_text("Click on each bar to adjust the volume", font, BLACK, screen_width/20, screen_height/16 + screen_height/14, screen)
        self.general_volume_slider.draw(screen)
        self.music_volume_slider.draw(screen)
        self.sfx_volume_slider.draw(screen)
        self.back_sound_button.draw(screen)
        pygame.display.flip()
        
    def event_handler(self, screen: pygame.Surface) -> None:
        settings_sound_active = True
        while settings_sound_active:
            #checks for the actions of the player
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
                        #add set volume function once music is added
                    self.music_volume_slider.draw(screen)

                    if self.sfx_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.sfx_volume_slider.moveSlider(mouse_pos)
                        self.sfx_volume_slider.updateText()
                        click_sfx.set_volume(round((self.general_volume_slider.getValue()/100) * (self.sfx_volume_slider.getValue()/100),1))
                    self.sfx_volume_slider.draw(screen)


                    if self.back_sound_button.draw(screen):
                        click_sfx.play()
                        self.menu_state = self.back_sound_button.draw(screen)
            
            self.draw_settings_sound(screen)
    
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))