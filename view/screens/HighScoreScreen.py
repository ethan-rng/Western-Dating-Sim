import pygame, sys, json
from controller.constants import *
from view.components.Button import Button
from models.exceptions import *
from controller.constants import *
from models.HighScoreTable import HighScoreTable
from view.components.TableInput import TableInput


class HighScoreScreen:
    def __init__(self) -> None:
        self.counter = 0
        self.game_state = "highscores"
        self.high_score_table :HighScoreTable = HighScoreTable()
        self.back_highscore_button = Button(screen_width/2.48, (screen_height/3) + (screen_height/6)*3, (screen_width/4), (screen_height/13), "Back", WHITE, "main", pygame)
        
        self.backdrop_rect = pygame.Rect(screen_width/9, screen_height//4.5, screen_width/1.2, screen_height/2)
        self.player_name_rect = pygame.Rect(screen_width/9, screen_height//4.5, screen_width/2.5, screen_height/15)
        self.player_score_rect = pygame.Rect(screen_width - screen_width/2.19, screen_height//4.5, screen_width/2.5, screen_height/15)
              
    def draw_high_score_screen(self, screen: pygame.Surface) -> None:
        screen.fill(DARK_GRAY)
        self.draw_text("High Scores", title_font, BLACK, screen_width/20, screen_height/16, screen)
        self.draw_text("View all high scores from all players", font, BLACK, screen_width/20, screen_height/16 + screen_height/12, screen)
        pygame.draw.rect(screen,WHITE, self.backdrop_rect)
        pygame.draw.rect(screen, WHITE, self.player_name_rect)
        self.label_surface = font.render("Username", True, BLACK)
        self.label_rect = self.label_surface.get_rect(x = self.player_name_rect.x + 10, centery = self.player_name_rect.centery)
        screen.blit(self.label_surface, self.label_rect)
        pygame.draw.rect(screen, WHITE, self.player_score_rect)
        self.score_surface = font.render("score", True, BLACK)
        self.score_rect = self.label_surface.get_rect(x = self.player_score_rect.x + 10, centery = self.player_score_rect.centery)
        screen.blit(self.score_surface, self.score_rect)
        with open(os.path.join('models', 'data', 'UserGameStates.json'), "r") as file:
            counter = 0
            scores_list = json.load(file)
            for score in scores_list:
                if counter < 5:
                    input = TableInput(screen_width/9, screen_height/3+(screen_height/14)*counter, screen_width/1.2, screen_height/15, self.high_score_table.getRankScore(counter+1)[0], self.high_score_table.getRankScore(counter+1)[1])
                    counter += 1
                    input.draw(screen)
        self.back_highscore_button.draw(screen)
        pygame.display.flip()

    def event_handler(self, screen: pygame.Surface) -> None:
        newgame_active = True

        while newgame_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        newgame_active = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_highscore_button.draw(screen):
                        click_sfx.play()
                        self.game_state = self.back_highscore_button.draw(screen)
                        return self.game_state
                    
            self.draw_high_score_screen(screen)
    
    """ Helper function to draw text on the screen """
    def draw_text(self, text: str, font: pygame.font.Font, text_col: tuple, x: float, y: float, screen: pygame.Surface):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))
