from controller.constants import *
import os
import pygame

class Menu:
    def __init__(self) -> None:

        background_image = pygame.image.load(os.path.join('view', 'assets', 'tower-thumb.jpg')).convert()
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        background_image = pygame.transform.scale(background_image, (screen_width+200, screen_height+200))
        
        grey_rectangle = pygame.image.load(os.path.join('view', 'assets', 'rectangle.png')).convert()
        pygame.transform.scale(grey_rectangle, (screen_width // 4, screen_height ))
        
        logo = pygame.image.load(os.path.join('view', 'assets', 'logo.png')).convert()
        logo = pygame.transform.scale(logo, (screen_width // 4, screen_height // 5))

        path = os.path.join('view', 'assets', 'title.png')
        title = pygame.image.load(path).convert()
        path = os.path.join('view', 'assets', 'title.png')
        title = pygame.image.load(path).convert()
        title = pygame.transform.scale(title, (screen_width // 4, screen_height // 4 - screen_height // 5))


         # Main Menu Items
        menu_items = ["Start New Game", "Load Game", "Highscores", "Album","Settings", "Help", "Quit"]


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
                #write the names of our group
                message = baby_font.render("Created as a part of CS2212 at Western by Group 29", True, BLACK)
                screen.blit(message, (screen_width // 50, 39*screen_height//40))
                message2 = baby_font.render("Jasper, Aaron, Lecia, Ethan, Jasmine", True, BLACK)
                screen.blit(message2, (screen_width // 50, screen_height))
                pygame.display.flip()


     global current_dialogue_index
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


  #load main settings button
        controls_settings_button = Button(screen_width/5.4, screen_height/3, (screen_width/4), (screen_height/13), "Controls", WHITE, "controls", pygame)
        sound_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) , (screen_width/4), (screen_height/13), "Sound Settings", WHITE, "sound", pygame)
        video_settings_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Video Settings", WHITE, "video", pygame)
        language_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6), (screen_width/4), (screen_height/13), "Language", WHITE, "language", pygame)
        accessibility_settings_button = Button(screen_width/5.4, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Accessibility Settings", WHITE, "accessibility", pygame)
        account_settings_button = Button(screen_width - screen_width/2.6, (screen_height/3) + (screen_height/6)*2, (screen_width/4), (screen_height/13), "Account Settings", WHITE, "account", pygame)
        back_settings_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "main", pygame)
