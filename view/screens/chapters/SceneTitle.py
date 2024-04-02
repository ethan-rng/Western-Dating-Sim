import pygame


class SceneTitle:
    """
    Represents a scene title to be displayed on a pygame surface.

    Attributes:
        :screen (pygame.Surface): The pygame surface where the title will be displayed.
        :text (str): The text content of the title.
        :font_size (int): The font size of the title text.
        :bg_color (tuple[int]): The background color of the title.
        :text_color (tuple[int]): The color of the title text.
        :box_color (tuple[int]): The color of the rectangle box behind the text.
    """
    def __init__(self, screen: pygame.Surface, text:str, font_size=74, bg_color=(0, 0, 0), text_color=(255, 255, 255), box_color=(0, 0, 0)):
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
        self.screen: pygame.Surface = screen
        self.text: str = text
        self.font_size: int = font_size
        self.bg_color: tuple[int] = bg_color
        self.text_color: tuple[int] = text_color
        self.box_color: tuple[int] = box_color  # Color for the rectangle box

        # GUI Items
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=(screen.get_width()//2, screen.get_height()//2))

    def draw(self):
        """
        Draws the SceneTitle onto the screen.
        """
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