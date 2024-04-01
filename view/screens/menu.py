from controller.constants import *
import os
import pygame
import sys
from view.components.button import Button

class Menu:
    """
    A class to represent the main menu of a game.

    Attributes:
        screen (pygame.Surface): The surface on which the menu will be drawn.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        """
        Initializes the Menu class with the given screen.

        Parameters:
            screen (pygame.Surface): The surface on which the menu will be drawn.
        """

        # Load and prepare background image
        background_image = pygame.image.load(os.path.join('view', 'assets', 'tower-thumb.jpg')).convert()
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        background_image = pygame.transform.scale(background_image, (screen_width + 200, screen_height + 200))
        
        # Load and prepare grey rectangle
        grey_rectangle = pygame.image.load(os.path.join('view', 'assets', 'rectangle.png')).convert()
        grey_rectangle = pygame.transform.scale(grey_rectangle, (screen_width // 4, screen_height))
        
        # Load and prepare logo image
        logo = pygame.image.load(os.path.join('view', 'assets', 'logo.png')).convert()
        logo = pygame.transform.scale(logo, (screen_width // 4, screen_height // 5))

        # Load and prepare title image
        title = pygame.image.load(os.path.join('view', 'assets', 'title.png')).convert()
        title = pygame.transform.scale(title, (screen_width // 4, screen_height // 4 - screen_height // 5))

        # Define main menu items
        menu_items = ["Start New Game", "Load Game", "Highscores", "Album", "Settings", "Help", "Quit"]

        # Draw the main menu screen
        self.draw_menu(screen, background_image, grey_rectangle, logo, title, menu_items)

        # Main menu interaction loop
        menu_active = True
        while menu_active:
            menu_active = self.handle_events(screen, menu_items)

    def draw_menu(self, screen: pygame.Surface, background_image: pygame.Surface, grey_rectangle: pygame.Surface,
                  logo: pygame.Surface, title: pygame.Surface, menu_items: list[str]) -> None:
        """
        Draws the main menu components on the screen.

        Parameters:
            screen (pygame.Surface): The surface to draw on.
            background_image (pygame.Surface): The background image for the menu.
            grey_rectangle (pygame.Surface): The grey rectangle image for the menu.
            logo (pygame.Surface): The logo image for the menu.
            title (pygame.Surface): The title image for the menu.
            menu_items (list[str]): The list of menu item names.
        """
        screen.blit(background_image, (0, 0))
        grey_rectangle.set_alpha(200)
        screen.blit(grey_rectangle, (0, screen_height // 5))
        pygame.draw.rect(screen, BLACK, (0, screen_height // 4, screen_width // 4, 150 + screen_height - screen_height // 5), 4)
        screen.blit(logo, (0, 0))
        screen.blit(title, (0, screen_height // 5))
        pygame.draw.rect(screen, BLACK, (0, screen_height // 5, screen_width // 4, screen_height // 4 - screen_height // 5), 4)

        # Draw menu items
        for index, item in enumerate(menu_items):
            menu_text = font.render(item, True, BLACK)
            x = screen_width // 8 - (menu_text.get_width() // 2)
            y = (screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 75))
            screen.blit(menu_text, (x, y))

        # Draw group names
        message = baby_font.render("Created as a part of CS2212 at Western by Group 29", True, BLACK)
        screen.blit(message, (screen_width // 50, 39 * screen_height // 40))
        message2 = baby_font.render("Jasper, Aaron, Lecia, Ethan, Jasmine", True, BLACK)
        screen.blit(message2, (screen_width // 50, screen_height))

        pygame.display.flip()

    def handle_events(self, screen: pygame.Surface, menu_items: list[str]) -> bool:
        """
        Handles events in the main menu, such as mouse clicks and keyboard input.

        Parameters:
            screen (pygame.Surface): The surface to draw on.
            menu_items (list[str]): The list of menu item names.

        Returns:
            bool: The status of the menu, whether it's still active or not.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False  # Deactivate menu on ESC key

            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.process_mouse_click(event, menu_items)

        return True  # Menu remains active

    def process_mouse_click(self, event: pygame.event.Event, menu_items: list[str]) -> bool:
        """
        Processes mouse click events in the main menu.

        Parameters:
            event (pygame.event.Event): The event to process.
            menu_items (list[str]): The list of menu item names.

        Returns:
            bool: The status of the menu, whether it's still active or not.
        """
        for index, item in enumerate(menu_items):
            menu_text = font.render(item, True, BLACK)
            x = screen_width // 8 - (menu_text.get_width() // 2)
            y = (screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 75))
            item_rect = menu_text.get_rect(topleft=(x, y))
            if item_rect.collidepoint(event.pos):
                click_sfx.play()
                menu_state = self.menu_click(index)
                return False  # Deactivate menu after a click

        return True  # Menu remains active if no click is processed

    def menu_click(self, index: int) -> str:
        """
        Handles the action to be taken when a menu item is clicked.

        Parameters:
            index (int): The index of the clicked menu item.

        Returns:
            str: The state or action to proceed with, based on the clicked menu item.
        """
        if index == 0:
            return "start"
        elif index == 1:
            return "load"
        elif index == 2:
            return "highscores"
        elif index == 3:
            return "album"
        elif index == 4:
            return "settings"
        elif index == 5:
            return "help"
        elif index == 6:
            pygame.quit()
            sys.exit()
