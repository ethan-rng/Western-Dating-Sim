import pygame, os
from controller.constants import *
from view.components.Button import Button
from view.components.Slider import Slider
from view.components.inputBox import TextInputBox


class NewGameScreen:
    
    def __init__(self) -> None:
        self.intelligence = 0
        self.charisma = 0
        self.attractiveness = 0
        self.continue_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Continue", WHITE, "chp1", pygame)
        self.intelligence_slider = Slider((screen_width - screen_width/2.8, screen_height//4), (screen_width/1.8,20), "Intelligence", 0.5, 0, 10)
        self.charisma_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + screen_height//6), (screen_width/1.8,20), "Charisma", 0.5, 0, 10)
        self.attractiveness_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + (screen_height//6 *2)), (screen_width/1.8,20), "Attractiveness", 0.5, 0, 10)
        self.name_input = TextInputBox(screen_width - screen_width/2.8, screen_height//3, screen_width/1.8, font)
        
    def draw_newgame_screen(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.continue_button.draw(screen)
        self.intelligence_slider.draw(screen)
        self.charisma_slider.draw(screen)
        self.attractiveness_slider.draw(screen)
        self.name_input.draw(screen)
        pygame.display.flip()
        
    def event_handler(self, screen: pygame.Surface) -> str:
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
                    click_sfx.play()
                    mouse_pos = pygame.mouse.get_pos()
                    mouse = pygame.mouse.get_pressed()

                    if self.intelligence_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.intelligence_slider.moveSlider(mouse_pos)
                        self.intelligence_slider.updateText()
                        self.intelligence = self.intelligence_slider.getValue()
                    self.intelligence_slider.draw(screen)

                    if self.charisma_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.charisma_slider.moveSlider(mouse_pos)
                        self.charisma_slider.updateText()
                        self.charisma = self.charisma_slider.getValue()
                    self.charisma_slider.draw(screen)

                    if self.attractiveness_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        self.attractiveness_slider.moveSlider(mouse_pos)
                        self.attractiveness_slider.updateText()
                        self.attractiveness = self.attractiveness_slider.getValue
                    self.attractiveness_slider.draw(screen)


                    if self.continue_button.draw(screen):
                        click_sfx.play()
                        menu_state = self.continue_button.draw(screen)
                        return menu_state

            self.draw_newgame_screen(screen)