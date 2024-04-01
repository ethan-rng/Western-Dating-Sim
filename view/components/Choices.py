import pygame


class ChoicesScreen:
    def __init__(self, screen, choices):
        self.screen = screen
        self.choices = choices
        self.font = pygame.font.Font(None, 40)
        self.button_width = 300
        self.button_height = 50
        self.button_margin = 20
        self.button_color = (0, 0, 0)  # black button
        self.text_color = (255, 255, 255)  # white text
        self.buttons = []
        self.selected_choice_index = 0

        # Calculate max button width based on the longest choice
        self.button_width = max(self.font.size(choice)[0] for choice in choices) + 2 * self.button_margin
        self.button_height = self.font.get_height() + 2 * self.button_margin

    def draw_buttons(self):
        self.buttons.clear()
        screen_width, screen_height = self.screen.get_size()
        start_y = (screen_height - (
                self.button_height * len(self.choices) + self.button_margin * (len(self.choices) - 1))) // 2

        for i, choice in enumerate(self.choices):
            text_surface = self.font.render(choice, True, self.text_color)
            text_size = text_surface.get_size()
            button_x = (screen_width - self.button_width) // 2
            button_y = start_y + (self.button_height + self.button_margin) * i
            button_rect = pygame.Rect(button_x, button_y, self.button_width, self.button_height)
            self.buttons.append(button_rect)

            # Create a transparent surface for the button
            button_surface = pygame.Surface((self.button_width, self.button_height), pygame.SRCALPHA)
            pygame.draw.rect(button_surface, self.button_color, (0, 0, self.button_width, self.button_height))

            text = self.font.render(choice, True, self.text_color)
            text_rect = text.get_rect(center=(self.button_width // 2, self.button_height // 2))

            # Blit the text onto the button surface, centered
            button_surface.blit(text_surface, text_surface.get_rect(center=button_surface.get_rect().center))

            self.screen.blit(button_surface, button_rect.topleft)

    def display(self) -> int:
        self.selected_choice_index = None  # Reset the selected choice index each time the display is called
        running = True
        
        while running:
            self.draw_buttons()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, button in enumerate(self.buttons):
                        if button.collidepoint(event.pos):
                            self.selected_choice_index = i  # Save the selected choice index
                            running = False  # Exit the loop
                            break  # No need to check other buttons

        return self.selected_choice_index
