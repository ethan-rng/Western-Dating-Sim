import pygame, os
from view.components.button import Button
from view.components.slider import Slider
from view.components.inputBox import TextInputBox


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (160, 32, 240)
GRAY = (192, 192, 192)
DARK_GRAY = (132, 135, 140)
GREEN = (0, 255, 0)
LIGHT_GRAY = (234,234,234)

#initilizing fonts
font = pygame.font.SysFont(None, 45)

infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h

continueButton = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Continue", WHITE, "start_game", pygame)
intelligenceSlider = Slider((screen_width - screen_width/2.8, screen_height//4), (screen_width/1.8,20), "Intelligence", 0.5, 0, 10)
charismaSlider = Slider((screen_width - screen_width/2.8, screen_height//4 + screen_height//6), (screen_width/1.8,20), "Charisma", 0.5, 0, 10)
attractivenessSlider = Slider((screen_width - screen_width/2.8, screen_height//4 + (screen_height//6 *2)), (screen_width/1.8,20), "Attractiveness", 0.5, 0, 10)
    
clickSfx = pygame.mixer.Sound(os.path.join('view', 'assets', 'click.wav'))

class NewGameScreen:
    
    def __init__(self) -> None:
        self.intelligence = 0
        self.charisma = 0
        self.attractiveness = 0

        
    def drawNewScreen(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        continueButton.draw(screen)
        intelligenceSlider.draw(screen)
        charismaSlider.draw(screen)
        attractivenessSlider.draw(screen)
        pygame.display.flip()
        
    def newScreenEvents(self, screen: pygame.Surface) -> str:
        clickSfx.play()
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        if intelligenceSlider.container_rect.collidepoint(mouse_pos) and mouse[0]:
            intelligenceSlider.move_slider(mouse_pos)
            intelligenceSlider.updateText()
            self.intelligence = intelligenceSlider.get_value()
        intelligenceSlider.draw(screen)

        if charismaSlider.container_rect.collidepoint(mouse_pos) and mouse[0]:
            charismaSlider.move_slider(mouse_pos)
            charismaSlider.updateText()
            self.charisma = charismaSlider.get_value()
        charismaSlider.draw(screen)

        if attractivenessSlider.container_rect.collidepoint(mouse_pos) and mouse[0]:
            attractivenessSlider.move_slider(mouse_pos)
            attractivenessSlider.updateText()
            self.attractiveness = attractivenessSlider.get_value
        attractivenessSlider.draw(screen)


        if continueButton.draw(screen):
            clickSfx.play()
            menu_state = continueButton.draw(screen)
            print(menu_state)
            return menu_state