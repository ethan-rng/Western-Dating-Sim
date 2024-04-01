from controller.constants import *
import pygame
import sys

from view.components.button import Button

class Help2:
    def __init__(self) -> None:
        self.menu_state = "help2"
        
        #load help2 images
        path = os.path.join('view', 'assets', 'help2.png')
        help2 = pygame.image.load(path)
        self.help2 = pygame.transform.scale(help2, (screen_width, help2.get_height() / (help2.get_width() / screen_width)))
        
        #load help2 menu buttons
        self.back_to_help1_button = Button(screen_width/10, 7*(screen_height/8), (screen_width/4), (screen_height/13), "Back", GRAY , "help1", pygame)

    def draw_help2(self, screen: pygame.Surface) -> None:
        screen.fill(LIGHT_GRAY)
        screen.blit(self.help2, (0, 0))
        self.back_to_help1_button.draw(screen)
        pygame.display.flip()
        
    def event_handler(self, screen: pygame.Surface) -> str:
        help2_active = True
        while help2_active:
            #checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        help2 = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu_state == "help2":
                        if self.back_to_help1_button.draw(screen):
                            click_sfx.play()
                            self.menu_state = self.back_to_help1_button.draw(screen)
                            return self.menu_state
            
            self.draw_help2(screen)