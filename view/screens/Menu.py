import pygame
import os
import sys
from controller.constants import *
from view.components.Button import Button

class Menu:
    """
    Class representing the main menu of the game.

    Attributes:
    :background_image: Pygame surface object representing the background image.
    :grey_rectangle: Pygame surface object representing the grey rectangle.
    :logo: Pygame surface object representing the game logo.
    :title: Pygame surface object representing the game title.
    :menu_items: List of strings representing the menu items.
    :game_state: String representing the current state of the game.
    """

    def __init__(self) -> None:
        """
        Initialize the main menu.
        """
        background_image = pygame.image.load(os.path.join('view', 'assets', 'tower-thumb.jpg')).convert()
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        self.background_image = pygame.transform.scale(background_image, (screen_width + 200, screen_height + 200))

        path = os.path.join('view', 'assets', 'rectangle.png')
        grey_rectangle = pygame.image.load(os.path.join('view', 'assets', 'rectangle.png')).convert()
        self.grey_rectangle = pygame.transform.scale(grey_rectangle, (screen_width // 4, screen_height))

        logo = pygame.image.load(os.path.join('view', 'assets', 'logo.png')).convert()
        self.logo = pygame.transform.scale(logo, (screen_width // 4, screen_height // 5))

        path = os.path.join('view', 'assets', 'title.png')
        title = pygame.image.load(path).convert()
        self.title = pygame.transform.scale(title, (screen_width // 4, screen_height // 4 - screen_height // 5))

        # Main Menu Items
        self.menu_items = ["Start New Game", "Load Game", "Highscores", "Album", "Settings", "Help", "Quit"]

    def draw_menu(self, screen):
        """
        Draw the main menu on the screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        # Draw main menu screen
        screen.blit(self.background_image, (0, 0))  # draws background
        self.grey_rectangle.set_alpha(200)  # sets transparency of the grey ractangle
        screen.blit(self.grey_rectangle, (0, screen_height // 5))  # draws the grey rectangle
        pygame.draw.rect(screen, BLACK,
                         (0, screen_height // 4, screen_width // 4, 150 + screen_height - screen_height // 5),
                         4)  # draws the border around the grey rectangle
        screen.blit(self.logo, (0, 0))  # draws the logo
        screen.blit(self.title, (0, screen_height // 5))  # draws the title
        pygame.draw.rect(screen, BLACK,
                         (0, screen_height // 5, screen_width // 4, screen_height // 4 - screen_height // 5),
                         4)  # draws the border around the title
        # draws out the menu screen
        for index, item in enumerate(self.menu_items):
            menu_text = font.render(item, True, BLACK)
            x = screen_width // 8 - (menu_text.get_width() // 2)
            y = (screen_height // 2 - (menu_text.get_height() * len(self.menu_items) // 2) + (index * 75))
            screen.blit(menu_text, (x, y))
        # write the names of our group
        message = baby_font.render("Created as a part of CS2212 at Western by Group 29", True, BLACK)
        screen.blit(message, (screen_width // 50, 39 * screen_height // 40))
        message2 = baby_font.render("Jasper, Aaron, Lecia, Ethan, Jasmine", True, BLACK)
        screen.blit(message2, (screen_width // 50, screen_height))
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface) -> str:
        """
        Handle events on the main menu.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        menu_active = True
        while menu_active:
            # checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        menu_active = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if mouse click is within the bounds of any menu item
                    for index, item in enumerate(self.menu_items):
                        menu_text = font.render(item, True, BLACK)
                        x = screen_width // 8 - (menu_text.get_width() // 2)
                        y = (screen_height // 2 - (menu_text.get_height() * len(self.menu_items) // 2) + (index * 75))
                        item_rect = menu_text.get_rect(topleft=(x, y))
                        if item_rect.collidepoint(event.pos):
                            click_sfx.play()
                            self.menu_click(index)
                            return self.game_state

            self.draw_menu(screen)

    def menu_click(self, index: int) -> None:
        """
        Handle menu item clicks.

        Parameters:
        :index: Integer representing the index of the clicked menu item.
        """
        # This function handles the menu clicks
        if index == 0:
            self.game_state = "login"
        elif index == 1:
            self.game_state = "load"
        # takes you to the highscores table
        elif index == 2:
            self.game_state = "highscores"
        # takes you to the albums
        elif index == 3:
            self.game_state = "album"
        # takes you to settings
        elif index == 4:
            self.game_state = "settings"
        # takes you to help menu
        elif index == 5:
            self.game_state = "help1"
        # quits the game
        elif index == 6:
            pygame.quit()
            sys.exit()


