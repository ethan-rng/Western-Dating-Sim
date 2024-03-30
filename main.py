import pygame
import sys
from components.button import Button
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
GRAY = (192, 192, 192)
DARK_GRAY = (132, 135, 140)
GREEN = (0, 255, 0)

# Font setup
font = pygame.font.SysFont(None, 45)
title_font = pygame.font.SysFont(None, 90)

#create a helper function to draw text on the screen
""" Helper function to draw text on the screen """
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#game variables
menu_state = "main"

# Load images
background_image = pygame.image.load("tower-thumb.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width + 50, screen_height + 180))
grey_rectangle = pygame.image.load("rectangle.png").convert()
grey_rectangle = pygame.transform.scale(grey_rectangle, (screen_width // 4, screen_height ))
logo = pygame.image.load("logo.png").convert()
logo = pygame.transform.scale(logo, (screen_width // 4, screen_height // 5))
title = pygame.image.load("title.png").convert()
title = pygame.transform.scale(title, (screen_width // 4, screen_height // 4 - screen_height // 5))

#load sounds
click_sfx = pygame.mixer.Sound("assets\click.wav")

#load main settings button
controls_settings_button = Button(screen_width/5.4, screen_height/3, (screen_width/4), (screen_height/13), "Controls", WHITE, "controls", pygame)
sound_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) , (screen_width/4), (screen_height/13), "Sound Settings", WHITE, "sound", pygame)
video_settings_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Video Settings", WHITE, "video", pygame)
language_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Language", WHITE, "language", pygame)
accessibility_settings_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Accessibility Settings", WHITE, "accessibility", pygame)
account_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Account Settings", WHITE, "account", pygame)
back_settings_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "main", pygame)

# Main Menu Items
menu_items = ["Start New Game", "Load Game", "Highscores", "Album","Settings", "Help", "Quit"]

def draw_menu(menu_state):
    if menu_state == "main":
        #Draw main menu screen
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
        
    if menu_state == "settings":
        screen.fill(DARK_GRAY)
        draw_text("Settings", title_font, BLACK, screen_width/20, screen_height/16 )
        controls_settings_button.draw(screen)
        sound_settings_button.draw(screen)
        video_settings_button.draw(screen)
        language_settings_button.draw(screen)
        accessibility_settings_button.draw(screen)
        account_settings_button.draw(screen)
        back_settings_button.draw(screen)
        pygame.display.flip()        

def main_menu(menu_state):
    menu_active = True
    while menu_active:  
        #checks for the actions of the player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                    menu_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
               # Check if mouse click is within the bounds of any menu item
                if menu_state == "main":
                    for index, item in enumerate(menu_items):
                        menu_text = font.render(item, True, BLACK)
                        x = screen_width // 8 - (menu_text.get_width() // 2)
                        y = (screen_height // 2 - (menu_text.get_height() * len(menu_items) // 2) + (index * 75))
                        item_rect = menu_text.get_rect(topleft=(x, y))
                        if item_rect.collidepoint(event.pos):
                        click_sfx.play()
                            menu_state = menu_click(index)
                            
                elif menu_state == "settings":
                    if controls_settings_button.draw(screen):
                        menu_state =  controls_settings_button.draw(screen)
                    elif sound_settings_button.draw(screen):
                        menu_state = sound_settings_button.draw(screen)
                    elif video_settings_button.draw(screen):
                        menu_state = video_settings_button.draw(screen)
                    elif language_settings_button.draw(screen):
                        menu_state = language_settings_button.draw(screen)
                    elif accessibility_settings_button.draw(screen):
                        menu_state = accessibility_settings_button.draw(screen)
                    elif account_settings_button.draw(screen):
                        menu_state = account_settings_button.draw(screen)
                    elif back_settings_button.draw(screen):
                        menu_state = back_settings_button.draw(screen)
        
                else:
                    pass
                    
        
        draw_menu(menu_state)

def menu_click(index):
    # This function handles the menu clicks
    if index == 0:
        menu_state = "start"
        return menu_state
    elif index == 1:
        menu_state = "load"
        return menu_state
    #takes you to the highscores table
    elif index == 2:
        menu_state = "highscores"
        return menu_state
    #takes you to the albums
    elif index == 3:
        menu_state = "album"
        return menu_state
    #takes you to settings
    elif index == 4:
        menu_state = "settings"
        return menu_state
    #takes you to help menu
    elif index == 5:
        menu_state = "help"
        return menu_state
    #quits the game
    elif index == 6:
        pygame.quit()
        sys.exit()

# Call the main menu
main_menu(menu_state)


