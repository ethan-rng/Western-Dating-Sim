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
font = pygame.font.SysFont(None, 55)

# Main Menu Items
menu_items = ['Start New Game', 'Load Game', 'Tutorials', 'High Scores', 'Exit']

def draw_menu():
    screen.fill(BLACK)
    for index, item in enumerate(menu_items):
        menu_text = font.render(item, True, WHITE)
        x = screen_width // 2 - (menu_text.get_width() // 2)
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
                # Here you would check for other keypresses to navigate the menu or select an option
        
        draw_menu()

# Call the main menu before entering the main game loop
main_menu()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (e.g., black)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
