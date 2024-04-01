from controller.constants import *


class Slider:
    def __init__(self, pos: tuple, size: tuple, label: str, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.label = label

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos + 9, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos + 9, 10,
                                       self.size[1])

        self.updateText()

    def moveSlider(self, mouse_pos):
        self.button_rect.centerx = mouse_pos[0]

    """Public methods that draws out the slider component onto the screen"""

    def draw(self, screen: pygame.Surface) -> None:
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

        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, "black", self.button_rect)

    def updateText(self):
        self.text = str(self.get_value())
        self.render = font.render(self.text, True, 'black')
        self.text_width = self.render.get_width()
        self.text_height = self.render.get_height()

    def getValue(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return round((button_val / val_range) * (self.max - self.min) + self.min)
