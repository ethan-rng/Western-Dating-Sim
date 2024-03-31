import pygame, os, sys

class Menu:
    def __init__(self) -> None:
        self.menu_state


    """ Public Method which handles menu clicks """
    def menu_click(self, index:int):
        if index == 0:
            self.menu_state = "start"
            return self.menu_state
        
        elif index == 1:
            self.menu_state = "load"
            return self.menu_state
        
        # Takes you to the highscores table
        elif index == 2:
            self.menu_state = "highscores"
            return self.menu_state
        
        # Takes you to the albums
        elif index == 3:
            self.menu_state = "album"
            return self.menu_state
        
        # Takes you to settings
        elif index == 4:
            self.menu_state = "settings"
            return self.menu_state
        
        # Takes you to help menu
        elif index == 5:
            self.menu_state = "help"
            return self.menu_state
        
        # Quits the game
        elif index == 6:
            pygame.quit()
            sys.exit()