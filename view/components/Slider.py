from controller.constants import *


class Slider:
    """
    Represents a slider component for adjusting values within a range in a pygame application.

    Attributes:
        :pos (tuple): The position (x, y) of the slider.
        :size (tuple): The size (width, height) of the slider.
        :label (str): The label associated with the slider.
        :initial_val (float): The initial value of the slider.
        :min (int): The minimum value of the slider.
        :max (int): The maximum value of the slider.
        :container_rect (pygame.Rect): The rectangular area representing the slider container.
        :button_rect (pygame.Rect): The rectangular area representing the slider button.
        :text (str): The text value displayed on the slider.
        :render: The rendered text surface.
        :text_width (int): The width of the rendered text.
        :text_height (int): The height of the rendered text.
    """
    def __init__(self, pos: tuple, size: tuple, label: str, initial_val: float, min: int, max: int) -> None:
        """
        Initializes a Slider object.

        Parameters:
            :pos (tuple): The position (x, y) of the slider.
            :size (tuple): The size (width, height) of the slider.
            :label (str): The label associated with the slider.
            :initial_val (float): The initial value of the slider.
            :min (int): The minimum value of the slider.
            :max (int): The maximum value of the slider.
        """
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.label = label

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos + screen_width//160, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - screen_height//40, self.slider_top_pos + 9, 10,
                                       self.size[1])

        self.updateText()

    def moveSlider(self, mouse_pos):
        """
        Moves the slider button based on the mouse position.

        Parameters:
            :mouse_pos (tuple): The position of the mouse (x, y).
        """
        self.button_rect.centerx = mouse_pos[0]

    """Public methods that draws out the slider component onto the screen"""

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the slider component on the screen.

        Parameters:
            :screen (pygame.Surface): The pygame surface on which the slider will be drawn.
        """
        infoObject = pygame.display.Info()
        screen_width = infoObject.current_w
        screen_height = infoObject.current_h

        slider_rect = pygame.Rect(screen_width / 20, self.pos[1] - screen_width / 52, screen_width / 1.1,
                                  screen_height // 15)
        pygame.draw.rect(screen, WHITE, slider_rect)

        text_num_surface = self.render
        text_num_rect = text_num_surface.get_rect(
            center=(screen_width - screen_width / 13, self.pos[1] + screen_height // 100))
        screen.blit(text_num_surface, text_num_rect)

        text_label_surface = font.render(self.label, True, 'black')
        text_label_rect = text_label_surface.get_rect(center=(screen_width / 6, self.pos[1] + screen_height // 100))
        screen.blit(text_label_surface, text_label_rect)

        text_num_rect.centery = slider_rect.centery
        
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, "black", self.button_rect)

    def updateText(self):
        """Updates the text value displayed on the slider."""
        self.text = str(self.getValue())
        self.render = font.render(self.text, True, 'black')
        self.text_width = self.render.get_width()
        self.text_height = self.render.get_height()

    def getValue(self):
        """
        Gets the current value of the slider.

        """
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return round((button_val / val_range) * (self.max - self.min) + self.min)
