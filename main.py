import pygame
import sys
import os
from view.button import Button
from view.slider import Slider
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
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#game variables
menu_state = "main"

# Load images
path = os.path.join('view', 'assets', 'tower-thumb.jpg')
background_image = pygame.image.load(path).convert()
background_image = pygame.transform.scale(background_image, (screen_width + 50, screen_height + 180))
path = os.path.join('view', 'assets', 'rectangle.png')
grey_rectangle = pygame.image.load(path).convert()
grey_rectangle = pygame.transform.scale(grey_rectangle, (screen_width // 4, screen_height ))
path = os.path.join('view', 'assets', 'logo.png')
logo = pygame.image.load(path).convert()
logo = pygame.transform.scale(logo, (screen_width // 4, screen_height // 5))
path = os.path.join('view', 'assets', 'title.png')
title = pygame.image.load(path).convert()
title = pygame.transform.scale(title, (screen_width // 4, screen_height // 4 - screen_height // 5))

#load sounds
path = os.path.join('view', 'assets', 'click.wav')
click_sfx = pygame.mixer.Sound(path)

#load main settings button
controls_settings_button = Button(screen_width/5.4, screen_height/3, (screen_width/4), (screen_height/13), "Controls", WHITE, "controls", pygame)
sound_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) , (screen_width/4), (screen_height/13), "Sound Settings", WHITE, "sound", pygame)
video_settings_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Video Settings", WHITE, "video", pygame)
language_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Language", WHITE, "language", pygame)
accessibility_settings_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Accessibility Settings", WHITE, "accessibility", pygame)
account_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Account Settings", WHITE, "account", pygame)
back_settings_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "main", pygame)

#controls settings variables
controls_keys = {"auto_key": pygame.K_g, "settings_key": pygame.K_t, "pause_key": pygame.K_p, "save_key": pygame.K_s, "load_key": pygame.K_l, "help_key": pygame.K_h}

#load controls settings buttons
auto_button = Button(screen_width/5.4, screen_height/3, (screen_width/4), (screen_height/13), "Auto: " + chr(controls_keys["auto_key"]), WHITE, "controls", pygame)
settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) , (screen_width/4), (screen_height/13), "Settings: " + chr(controls_keys["settings_key"]), WHITE, "sound", pygame)
pause_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Pause: " + chr(controls_keys["pause_key"]), WHITE, "video", pygame)
save_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Save: " + chr(controls_keys["save_key"]), WHITE, "language", pygame)
load_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Load: " + chr(controls_keys["load_key"]), WHITE, "accessibility", pygame)
help_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Help: " + chr(controls_keys["help_key"]), WHITE, "account", pygame)
back_controls_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)

#sound settings variables
general_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4), (screen_width/1.8,20), "Game Volume", 0.5, 0, 100)
music_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + screen_height//6), (screen_width/1.8,20), "Music Volume", 0.5, 0, 100)
sfx_volume_slider = Slider((screen_width - screen_width/2.8, screen_height//4 + (screen_height//6 *2)), (screen_width/1.8,20), "SFX Volume", 0.5, 0, 100)
back_volume_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)


# Main Menu Items
menu_items = ["Start New Game", "Load Game", "Highscores", "Album","Settings", "Help", "Quit"]

def draw_menu(menu_state: str) -> None:
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
        
    elif menu_state == "settings":
        screen.fill(DARK_GRAY)
        draw_text("Settings", title_font, BLACK, screen_width/20, screen_height/16 )
        controls_settings_button.draw(screen)
        sound_settings_button.draw(screen)
        video_settings_button.draw(screen)
        language_settings_button.draw(screen)
        accessibility_settings_button.draw(screen)
        account_settings_button.draw(screen)
        back_settings_button.draw(screen)
        back_controls_button.draw(screen)
        pygame.display.flip()  
        
    elif menu_state == "controls":
        screen.fill(DARK_GRAY)
        draw_text("Controls", title_font, BLACK, screen_width/20, screen_height/16 )
        draw_text("Click on a button, then press a key that is not binded", font, BLACK, screen_width/20, screen_height/16 + screen_height/14)
        auto_button.draw(screen)
        settings_button.draw(screen)
        pause_button.draw(screen)
        save_button.draw(screen)
        load_button.draw(screen)
        help_button.draw(screen)
        back_controls_button.draw(screen)
        pygame.display.flip()
        
    elif menu_state == "sound":
        screen.fill(DARK_GRAY)
        draw_text("Sound Settings", title_font, BLACK, screen_width/20, screen_height/16 )
        draw_text("Click on each bar to adjust the volume", font, BLACK, screen_width/20, screen_height/16 + screen_height/14)
        general_volume_slider.draw(screen)
        music_volume_slider.draw(screen)
        sfx_volume_slider.draw(screen)
        back_volume_button.draw(screen)
        pygame.display.flip()
        


def main_menu(menu_state, controls_keys):
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
                
                #Settings buttons            
                elif menu_state == "settings":
                    if controls_settings_button.draw(screen):
                        click_sfx.play()
                        menu_state =  controls_settings_button.draw(screen)
                    elif sound_settings_button.draw(screen):
                        click_sfx.play()
                        menu_state = sound_settings_button.draw(screen)
                    elif video_settings_button.draw(screen):
                        click_sfx.play()
                        menu_state = video_settings_button.draw(screen)
                    elif language_settings_button.draw(screen):
                        click_sfx.play()
                        menu_state = language_settings_button.draw(screen)
                    elif accessibility_settings_button.draw(screen):
                        click_sfx.play()
                        menu_state = accessibility_settings_button.draw(screen)
                    elif account_settings_button.draw(screen):
                        click_sfx.play()
                        menu_state = account_settings_button.draw(screen)
                    elif back_settings_button.draw(screen):
                        click_sfx.play()
                        menu_state = back_settings_button.draw(screen)
                
                #Controls_buttons
                elif menu_state == "controls":
                    if auto_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in controls_keys.values():
                                        # Assign the pygame key to the action in the keys dict.
                                        controls_keys["auto_key"] = event.key
                                        auto_button.updateText("Auto: " + chr(event.key))
                                        key_pressed = True  

                    elif settings_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        controls_keys["settings_key"] = event.key
                                        settings_button.updateText("Settings: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif pause_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        controls_keys["pause_key"] = event.key
                                        pause_button.updateText("Pause: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif save_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        controls_keys["save_key"] = event.key
                                        save_button.updateText("Save: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif load_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        controls_keys["load_key"] = event.key
                                        load_button.updateText("Load: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif help_button.draw(screen):
                        click_sfx.play()
                        key_pressed = False
                        while key_pressed == False:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key not in controls_keys.keys():
                                        # Assign the pygame key to the action in the keys dict.
                                        controls_keys["help_key"] = event.key
                                        help_button.updateText("Help: " + chr(event.key))
                                        key_pressed = True
                                    
                    elif back_controls_button.draw(screen):
                        click_sfx.play()
                        menu_state = back_controls_button.draw(screen)
                
                #sound settings
                elif menu_state == "sound":
                    click_sfx.play()
                    
                    mouse_pos = pygame.mouse.get_pos()
                    mouse = pygame.mouse.get_pressed()
                    
                    if general_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        general_volume_slider.move_slider(mouse_pos)
                        general_volume_slider.updateText()
                        click_sfx.set_volume(round((general_volume_slider.get_value()/100) * (sfx_volume_slider.get_value()/100),1))
                    general_volume_slider.draw(screen)
                    
                    if music_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        music_volume_slider.move_slider(mouse_pos)
                        music_volume_slider.updateText()
                        #add set volume function once music is added
                    general_volume_slider.draw(screen)
                    
                    if sfx_volume_slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                        sfx_volume_slider.move_slider(mouse_pos)
                        sfx_volume_slider.updateText()
                        click_sfx.set_volume(round((general_volume_slider.get_value()/100) * (sfx_volume_slider.get_value()/100),1))
                    general_volume_slider.draw(screen)
                    
                    
                    if back_controls_button.draw(screen):
                        click_sfx.play()
                        menu_state = back_controls_button.draw(screen)
                    
                    
        
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
main_menu(menu_state,controls_keys)


