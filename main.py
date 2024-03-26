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
PURPLE = (160, 32, 240)

# Font setup
font = pygame.font.SysFont(None, 45)

# Load images
background_image = pygame.image.load("tower-thumb.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width + 50, screen_height + 180))
grey_rectangle = pygame.image.load("rectangle.png").convert()
grey_rectangle = pygame.transform.scale(grey_rectangle, (screen_width // 4, screen_height ))
logo = pygame.image.load("logo.png").convert()
logo = pygame.transform.scale(logo, (screen_width // 4, screen_height // 5))
title = pygame.image.load("title.png").convert()
title = pygame.transform.scale(title, (screen_width // 4, screen_height // 4 - screen_height // 5))

# Main Menu Items
menu_items = ["Start New Game", "Load Game", "Highscores", "Album","Settings", "Help", "Quit"]

def draw_menu():
    screen.blit(background_image, (0, 0)) #draws background
    grey_rectangle.set_alpha(200) #sets transparency of the grey ractangle
    screen.blit(grey_rectangle, (0, screen_height // 5)) #draws the grey rectangle
    pygame.draw.rect(screen, BLACK, (0, screen_height // 4, screen_width // 4, screen_height - screen_height // 5), 4) #draws the border around the grey rectangle
    screen.blit(logo, (0, 0)) # draws the logo
    screen.blit(title, (0, screen_height // 5)) # draws the title
    pygame.draw.rect(screen, BLACK, (0, screen_height // 5, screen_width // 4, screen_height // 4 - screen_height // 5), 4) #draws the border around the title
    #draws out the menu screen
    for index, item in enumerate(menu_items):
        menu_text = font.render(item, True, BLACK)
        x = screen_width // 8 - (menu_text.get_width() // 2)
        y = (screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 75))
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
                    x = x = screen_width // 8 - (menu_text.get_width() // 2)
                    y = (screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 75))
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


