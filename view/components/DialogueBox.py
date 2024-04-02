import pygame


class DialogueBox:
    """
    Represents a dialogue box for displaying text in a pygame application.

    Attributes:
        :screen: The pygame surface on which the dialogue box will be drawn.
        :font_path (str): The file path to the font file, or None for default system font.
        :font_size (int): The size of the font used for rendering text in the dialogue box.
        :box_height (int): The height of the dialogue box.
        :padding (int): The padding between the text and the edges of the dialogue box.
        :margin (int): The margin between the dialogue box and the edges of the screen.
        :background_color (tuple): The color of the dialogue box background.
        :text_color (tuple): The color of the text in the dialogue box.
        :font (pygame.font.Font): The font object used for rendering text.

    """
    def __init__(self, screen, font_path=None, font_size=24, box_height=130, padding=10, margin=20, background_color=(0, 0, 0, 128), text_color=(255, 255, 255)):
        """
        Initializes a DialogueBox object.

        Parameters:
            :screen: The pygame surface on which the dialogue box will be drawn.
            :font_path (str): The file path to the font file, or None for default system font.
            :font_size (int): The size of the font used for rendering text in the dialogue box.
            :box_height (int): The height of the dialogue box.
            :padding (int): The padding between the text and the edges of the dialogue box.
            :margin (int): The margin between the dialogue box and the edges of the screen.
            :background_color (tuple): The color of the dialogue box background.
            :text_color (tuple): The color of the text in the dialogue box.
        """
        self.screen = screen
        self.font_size = font_size
        self.box_height = box_height
        self.padding = padding
        self.margin = margin
        self.background_color = background_color
        self.text_color = text_color

        # Load the font
        self.font = pygame.font.Font(font_path, font_size) if font_path else pygame.font.Font(None, font_size)

        # Calculate box dimensions and position
        self.box_width = self.screen.get_width() - 2 * self.margin
        self.box_top = self.screen.get_height() - self.box_height - self.margin - 35

    def draw(self, text):
        """
        Draws the dialogue box with the given text.

        Parameters:
            :text (str): The text to be displayed in the dialogue box.
        """
        # Render the dialogue box background
        box_rect = pygame.Rect(self.margin, self.box_top, self.box_width, self.box_height)
        pygame.draw.rect(self.screen, self.background_color, box_rect)

        # Render the dialogue text
        words = text.split(' ')
        lines = []
        line = ''
        for word in words:
            test_line = f"{line} {word}" if line else word
            text_surface = self.font.render(test_line, True, self.text_color)
            if text_surface.get_width() > self.box_width - 2 * self.padding:
                lines.append(line)
                line = word
            else:
                line = test_line
        lines.append(line)  # Add the last line

        # Blit the text lines within the box
        y = self.box_top + self.padding
        for line in lines:
            text_surface = self.font.render(line, True, self.text_color)
            text_x = self.margin + self.padding  # Use padding for the x coordinate as well
            self.screen.blit(text_surface, (text_x, y))
            y += text_surface.get_height() + self.padding  # Added padding between lines if needed

