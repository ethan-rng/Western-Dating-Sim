import pygame
import sys

# Initialize Pygame
pygame.init()

# Get the current display resolution
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h

# Set up the display in fullscreen mode
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Dating Simulator Ver. Western")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font setup
font_title = pygame.font.SysFont(None, 100)
font = pygame.font.SysFont(None, 55)

# Main Menu Items
menu_items = ["Start New Game", "Load Game", "Highscores", "Album","Settings", "Help", "Quit"]

def draw_menu():
    screen.fill(BLACK)
    title = font_title.render("Western Dating Simulator", True, WHITE)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height -  6 * (screen_height // 7)))
    for index, item in enumerate(menu_items):
        menu_text = font.render(item, True, WHITE)
        x = 0 + screen_width // 10
        y = screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 60)
        screen.blit(menu_text, (x, y))
    pygame.display.flip()

def main_menu():
    menu_active = True
    while menu_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                    menu_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               # Check if mouse click is within the bounds of any menu item
                for index, item in enumerate(menu_items):
                    menu_text = font.render(item, True, WHITE)
                    x = 0 + screen_width // 10
                    y = screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 60)
                    item_rect = menu_text.get_rect(topleft=(x, y))
                    if item_rect.collidepoint(event.pos):
                        menu_click(index)
        
        draw_menu()
  
def menu_click(index):
    # This function handles the menu clicks
    if index == 0:
        print("Start the Game")
    elif index == 1:
        print("Load Game")
    #takes you to the highscores table
    elif index == 2:
        print("Highscores")
    #takes you to the albums
    elif index == 3:
        print("Album")
    #takes you to settings
    elif index == 4:
        print("Settings")
    #takes you to help menu
    elif index == 5:
        print("Help")
    #quits the game
    elif index == 6:
        pygame.quit()
        sys.exit()

# Call the main menu
main_menu()
