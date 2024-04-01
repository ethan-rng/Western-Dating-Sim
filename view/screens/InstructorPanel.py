from controller.constants import *
import os
import pygame
import sys
from models.Instructor import Instructor
from view.components.Button import Button
from view.components.InputBox import TextInputBox

class InstructorPanel:
    def __init__(self) -> None:
        self.game_state = "InstructorPanel"
        self.search_player_username = ''
        self.instructor = Instructor("12345")
        self.player_list = self.instructor.Players
        self.charisma_text = ''
        self.intelligence_text = ''
        self.attractiveness_text = ''
        self.level_text = ''
        self.attraction_text = ''
        
        self.username_input_box = TextInputBox(screen_width//11.5, screen_height//5, screen_width/2, screen_height/20, "Player Username:", DARK_GRAY, pygame)
        self.username_search_button = Button(screen_width//19, (screen_height//5) + (screen_height/8), (screen_width/2.1), (screen_height/13), "Search", WHITE, "search", pygame)
        self.back_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "settings", pygame)

        self.view_charisma_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5, screen_width/2.5, screen_height/15)
        self.view_intelligence_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10), screen_width/2.5, screen_height/15)
        self.view_attractiveness_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10)*2, screen_width/2.5, screen_height/15)
        self.view_level_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10)*3, screen_width/2.5, screen_height/15)
        self.view_attraction_rect = pygame.Rect(screen_width - screen_width//2.5, screen_height//4.5+(screen_height//10)*4, screen_width/2.5, screen_height/15)
        
    def draw_instructor_panel(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.draw_text("Instructor Panel", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.username_input_box.draw(screen)
        self.username_search_button.draw(screen)
        self.back_button.draw(screen)
        
        #draw charisma display box
        pygame.draw.rect(screen, WHITE, self.view_charisma_rect)
        charisma_label_surface = font.render("Charisma:", True, BLACK)
        charisma_label_rect = charisma_label_surface.get_rect(x = self.view_charisma_rect.x + 10, centery = self.view_charisma_rect.centery)
        screen.blit(charisma_label_surface, charisma_label_rect)
        charisma_text_surface = font.render(self.charisma_text, True, BLACK)
        charisma_text_rect = charisma_text_surface.get_rect(x = self.view_charisma_rect.right - 40,centery = self.view_charisma_rect.centery)
        screen.blit(charisma_text_surface, charisma_text_rect)
        
        #draw intelligence display box
        pygame.draw.rect(screen, WHITE, self.view_intelligence_rect)
        intelligence_label_surface = font.render("Intelligence:", True, BLACK)
        intelligence_label_rect = intelligence_label_surface.get_rect(x = self.view_intelligence_rect.x + 10, centery = self.view_intelligence_rect.centery)
        screen.blit(intelligence_label_surface, intelligence_label_rect)
        intelligence_text_surface = font.render(self.intelligence_text, True, BLACK)
        intelligence_text_rect = intelligence_text_surface.get_rect(x = self.view_intelligence_rect.right - 40 ,centery = self.view_intelligence_rect.centery)
        screen.blit(intelligence_text_surface, intelligence_text_rect)
        
        #draw attractiveness display box
        pygame.draw.rect(screen, WHITE, self.view_attractiveness_rect)
        attractiveness_label_surface = font.render("Attractiveness:", True, BLACK)
        attractiveness_label_rect = attractiveness_label_surface.get_rect(x = self.view_attractiveness_rect.x + 10, centery = self.view_attractiveness_rect.centery)
        screen.blit(attractiveness_label_surface, attractiveness_label_rect)
        attractiveness_text_surface = font.render(self.charisma_text, True, BLACK)
        attractiveness_text_rect = attractiveness_text_surface.get_rect(x = self.view_attractiveness_rect.right - 40,centery = self.view_attractiveness_rect.centery)
        screen.blit(attractiveness_text_surface, attractiveness_text_rect)
        
        #draw level display box
        pygame.draw.rect(screen, WHITE, self.view_level_rect)
        level_label_surface = font.render("Level:", True, BLACK)
        level_label_rect = level_label_surface.get_rect(x = self.view_level_rect.x + 10, centery = self.view_level_rect.centery)
        screen.blit(level_label_surface, level_label_rect)
        level_text_surface = font.render(self.level_text, True, BLACK)
        level_text_rect = level_text_surface.get_rect(x = self.view_level_rect.right - 40, centery = self.view_level_rect.centery)
        screen.blit(level_text_surface, level_text_rect)
        
        #draw attraction score display box
        pygame.draw.rect(screen, WHITE, self.view_attraction_rect)
        attraction_label_surface = font.render("Attraction score:", True, BLACK)
        attraction_label_rect = attraction_label_surface.get_rect(x = self.view_attraction_rect.x + 10, centery = self.view_attraction_rect.centery)
        screen.blit(attraction_label_surface, (attraction_label_rect))
        attraction_text_surface = font.render(self.attraction_text, True, BLACK)
        attraction_text_rect = attraction_text_surface.get_rect(x = self.view_attraction_rect.right - self.view_attraction_rect.width/4, centery = self.view_attraction_rect.centery)
        screen.blit(attraction_text_surface, attraction_text_rect)
        pygame.display.flip()
        
    def event_handler(self, screen) -> str:
        newgame_active = True
        while newgame_active:  
            #checks for the actions of the player
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
                        self.charisma_text = str(self.instructor.viewStats(self.username)["charisma"])
                        self.intelligence_text = str(self.instructor.viewStats(self.username)["intelligence"])
                        self.attractiveness_text = str(self.instructor.viewStats(self.username)["attraction"])                       
                        self.level_text = str(self.instructor.viewProgress(self.username)["level"])
                        self.attraction_text = str(self.instructor.viewProgress(self.username)["attractionScore"])
                        self.draw_instructor_panel(screen)

                    
                    if self.username_input_box.draw(screen):
                        click_sfx.play()
                        self.username_input_box.event_handler(screen)
                        self.username = self.username_input_box.user_text
                    
            self.draw_instructor_panel(screen)
            
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))