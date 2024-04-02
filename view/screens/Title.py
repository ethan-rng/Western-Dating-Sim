import pygame

class SceneTitle:
    """
    Class representing a title scene in a game.

    Attributes:
    :screen: Pygame surface object representing the game screen.
    :text: String representing the title text.
    :font_size: Integer representing the font size of the title text.
    :bg_color: Tuple representing the background color of the scene.
    :text_color: Tuple representing the color of the title text.
    :box_color: Tuple representing the color of the rectangle box behind the text.
    :font: Pygame font object representing the font used for the title text.
    :text_surface: Pygame surface object representing the rendered title text.
    :text_rect: Pygame rect object representing the bounding rectangle of the title text.
    """

    def __init__(self, screen, text, font_size=74, bg_color=(0, 0, 0), text_color=(255, 255, 255), box_color=(0, 0, 0)):
        """
        Initialize a title scene.

        Parameters:
        :screen: Pygame surface object representing the game screen.
        :text: String representing the title text.
        :font_size: Integer representing the font size of the title text. Default is 74.
        :bg_color: Tuple representing the background color of the scene. Default is black.
        :text_color: Tuple representing the color of the title text. Default is white.
        :box_color: Tuple representing the color of the rectangle box behind the text. Default is black.
        """
        self.screen = screen
        self.text = text
        self.font_size = font_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.box_color = box_color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=(screen.get_width()//2, screen.get_height()//2))

    def draw(self):
        """
        Draw the title scene on the screen.
        """
        # Fill the screen with the background color
        self.screen.fill(self.bg_color)
        
        # Draw the rectangle behind the text
        box_rect = self.text_rect.inflate(20, 20)  # You can adjust the padding here
        box_rect.center = self.text_rect.center  # Ensure the text is centered in the box

        # Draw the rectangle onto the screen
        pygame.draw.rect(self.screen, self.box_color, box_rect)
        
        # Draw the text surface on the screen
        self.screen.blit(self.text_surface, self.text_rect)

