from controller.constants import *
import os
import pygame
import sys
from models.Instructor import Instructor
from view.components.Button import Button
from view.components.InputBox import TextInputBox
from models.exceptions import *

class InstructorPanel:
    """
    Class representing the instructor panel in the game.

    Attributes:
    :game_state: String representing the current state of the game.
    :search_player_username: String representing the username entered for player search.
    :instructor: Instructor object representing the game instructor.
    :player_list: List of players in the game.
    :charisma_text: String representing the charisma of the player being viewed.
    :intelligence_text: String representing the intelligence of the player being viewed.
    :attractiveness_text: String representing the attractiveness of the player being viewed.
    :level_text: String representing the level of the player being viewed.
    :attraction_text: String representing the attraction score of the player being viewed.
    :error_message: String representing any error messages during player search.
    :username_input_box: TextInputBox object for entering the player's username.
    :username_search_button: Button object for searching a player by username.
    :back_button: Button object for returning to the settings.
    :view_charisma_rect: Pygame Rect object representing the rectangle for displaying charisma.
    :view_intelligence_rect: Pygame Rect object representing the rectangle for displaying intelligence.
    :view_attractiveness_rect: Pygame Rect object representing the rectangle for displaying attractiveness.
    :view_level_rect: Pygame Rect object representing the rectangle for displaying level.
    :view_attraction_rect: Pygame Rect object representing the rectangle for displaying attraction score.
    """

    def __init__(self) -> None:
        """
        Initialize the instructor panel.
        """
        self.game_state = "InstructorPanel"
        self.search_player_username = ''
        self.instructor = Instructor("12345")
        self.player_list = self.instructor.Players
        self.charisma_text = ''
        self.intelligence_text = ''
        self.attractiveness_text = ''
        self.level_text = ''
        self.attraction_text = ''
        self.error_message: str = ""
        
        self.username_input_box = TextInputBox(screen_width//11.5, screen_height//5, screen_width/2, screen_height/20, "Player Username:", DARK_GRAY, pygame)
        self.username_search_button = Button(screen_width//19, (screen_height//5) + (screen_height/8), (screen_width/2.1), (screen_height/13), "Search", WHITE, "search", pygame)
        self.back_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)

        self.view_charisma_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5, screen_width/2.5, screen_height/15)
        self.view_intelligence_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10), screen_width/2.5, screen_height/15)
        self.view_attractiveness_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10)*2, screen_width/2.5, screen_height/15)
        self.view_level_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10)*3, screen_width/2.5, screen_height/15)
        self.view_attraction_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10)*4, screen_width/2.5, screen_height/15)
        
    def draw_instructor_panel(self, screen: pygame.Surface) -> None:
        """
        Draw the instructor panel on the screen.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        screen.fill(DARK_GRAY)
        self.draw_text("Instructor Panel", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.username_input_box.draw(screen)
        self.username_search_button.draw(screen)
        self.back_button.draw(screen)
        
        # Draw charisma display box
        pygame.draw.rect(screen, WHITE, self.view_charisma_rect)
        charisma_label_surface = font.render("Charisma:", True, BLACK)
        charisma_label_rect = charisma_label_surface.get_rect(x=self.view_charisma_rect.x + 10, centery=self.view_charisma_rect.centery)
        screen.blit(charisma_label_surface, charisma_label_rect)
        charisma_text_surface = font.render(self.charisma_text, True, BLACK)
        charisma_text_rect = charisma_text_surface.get_rect(x=self.view_charisma_rect.right - 40, centery=self.view_charisma_rect.centery)
        screen.blit(charisma_text_surface, charisma_text_rect)
        
        # Draw intelligence display box
        pygame.draw.rect(screen, WHITE, self.view_intelligence_rect)
        intelligence_label_surface = font.render("Intelligence:", True, BLACK)
        intelligence_label_rect = intelligence_label_surface.get_rect(x=self.view_intelligence_rect.x + 10, centery=self.view_intelligence_rect.centery)
        screen.blit(intelligence_label_surface, intelligence_label_rect)
        intelligence_text_surface = font.render(self.intelligence_text, True, BLACK)
        intelligence_text_rect = intelligence_text_surface.get_rect(x=self.view_intelligence_rect.right - 40, centery=self.view_intelligence_rect.centery)
        screen.blit(intelligence_text_surface, intelligence_text_rect)
        
        # Draw attractiveness display box
        pygame.draw.rect(screen, WHITE, self.view_attractiveness_rect)
        attractiveness_label_surface = font.render("Attractiveness:", True, BLACK)
        attractiveness_label_rect = attractiveness_label_surface.get_rect(x=self.view_attractiveness_rect.x + 10, centery=self.view_attractiveness_rect.centery)
        screen.blit(attractiveness_label_surface, attractiveness_label_rect)
        attractiveness_text_surface = font.render(self.charisma_text, True, BLACK)
        attractiveness_text_rect = attractiveness_text_surface.get_rect(x=self.view_attractiveness_rect.right - 40, centery=self.view_attractiveness_rect.centery)
        screen.blit(attractiveness_text_surface, attractiveness_text_rect)
        
        # Draw level display box
        pygame.draw.rect(screen, WHITE, self.view_level_rect)
        level_label_surface = font.render("Level:", True, BLACK)
        level_label_rect = level_label_surface.get_rect(x=self.view_level_rect.x + 10, centery=self.view_level_rect.centery)
        screen.blit(level_label_surface, level_label_rect)
        level_text_surface = font.render(self.level_text, True, BLACK)
        level_text_rect = level_text_surface.get_rect(x=self.view_level_rect.right - 40, centery=self.view_level_rect.centery)
        screen.blit(level_text_surface, level_text_rect)
        
        # Draw attraction score display box
        pygame.draw.rect(screen, WHITE, self.view_attraction_rect)
        attraction_label_surface = font.render("Attraction score:", True, BLACK)
        attraction_label_rect = attraction_label_surface.get_rect(x=self.view_attraction_rect.x + 10, centery=self.view_attraction_rect.centery)
        screen.blit(attraction_label_surface, (attraction_label_rect))
        attraction_text_surface = font.render(self.attraction_text, True, BLACK)
        attraction_text_rect = attraction_text_surface.get_rect(x=self.view_attraction_rect.right - self.view_attraction_rect.width/3.2, centery=self.view_attraction_rect.centery)
        screen.blit(attraction_text_surface, attraction_text_rect)
        
        # Drawing Error Message For any errors 
        if self.error_message:
            error_font = pygame.font.SysFont(None, 80)
            text_surface = error_font.render(self.error_message, True, RED)
            # Calculate x position to center the text
            text_x = (screen_width - text_surface.get_width()) / 2
            text_y = (screen_height * 9) / 13
            screen.blit(text_surface, (text_x, text_y))
            
        pygame.display.flip()
        
    def event_handler(self, screen: pygame.Surface) -> str:
        """
        Handle events on the instructor panel.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        """
        newgame_active = True
        while newgame_active:  
            # Checks for the actions of the player
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Press ESC to exit menu
                        newgame_active = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.back_button.draw(screen)
                        return self.game_state
                    
                    if self.username_search_button.draw(screen):
                        click_sfx.play()
                        try:
                            self.charisma_text = str(self.instructor.viewStats(self.username)["charisma"])
                            self.intelligence_text = str(self.instructor.viewStats(self.username)["intelligence"])
                            self.attractiveness_text = str(self.instructor.viewStats(self.username)["attraction"])                       
                            self.level_text = str(self.instructor.viewProgress(self.username)["level"])
                            self.attraction_text = str(self.instructor.viewProgress(self.username)["attractionScore"])
                        except UserNotFound:
                            self.error_message = "user does not exist"
                        else:
                            self.error_message = ""
                            self.draw_instructor_panel(screen)
                    
                    if self.username_input_box.draw(screen):
                        click_sfx.play()
                        self.username_input_box.event_handler(screen)
                        self.username = self.username_input_box.user_text
                    
            self.draw_instructor_panel(screen)
            
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface) -> None:
        """
        Helper function to draw text on the screen.

        Parameters:
        :text: String representing the text to be drawn.
        :font: Pygame font object representing the font of the text.
        :text_col: Tuple representing the color of the text.
        :x: Float representing the x-coordinate of the text.
        :y: Float representing the y-coordinate of the text.
        :screen: Pygame surface object representing the game screen.
        """
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))
