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
menu_items = ['Start New Game', 'Load Game', 'Tutorials', 'High Scores', 'Exit']

def draw_menu():
    screen.fill(BLACK)
    title = font_title.render('Western Dating Simulator', True, WHITE)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height -  4 * (screen_height // 5)))
    for index, item in enumerate(menu_items):
        menu_text = font.render(item, True, WHITE)
        x = screen_width // 2 - (menu_text.get_width() // 2)
        y = screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 90)
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
                    x = screen_width // 2 - (menu_text.get_width() // 2)
                    y = screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 90)
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
    #takes you to the tutorial menu
    elif index == 2:
        print("Tutorials")
    #takes you to the high scores table
    elif index == 3:
        print("High Scores")
    #quits the game
    elif index == 4:
        pygame.quit()
        sys.exit()
        

# Call the main menu before entering the main game loop
main_menu()

