import pygame

class SceneTitle:
    def __init__(self, screen, text, font_size=74, bg_color=(0, 0, 0), text_color=(255, 255, 255), box_color=(0, 0, 0)):
        self.screen = screen
        self.text = text
        self.font_size = font_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.box_color = box_color  # Color for the rectangle box
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=(screen.get_width()//2, screen.get_height()//2))

    def draw(self):
        # Fill the screen with the background color
        self.screen.fill(self.bg_color)
        
        # Draw the rectangle behind the text
        # Calculate the box dimensions based on the text size

        box_rect = self.text_rect.inflate(20, 20)  # You can adjust the padding here
        box_rect.center = self.text_rect.center  # Ensure the text is centered in the box

        # Draw the rectangle onto the screen
        pygame.draw.rect(self.screen, self.box_color, box_rect)
        
        # Draw the text surface on the screen
        self.screen.blit(self.text_surface, self.text_rect)
