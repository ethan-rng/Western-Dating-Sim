import pygame

class ChoicesScreen:
    def __init__(self, screen, choices):
        self.screen = screen
        self.choices = choices
        self.font = pygame.font.Font(None, 40)
        self.button_width = 300
        self.button_height = 50
        self.button_margin = 20
        self.button_color = (200, 200, 200, 128)  # Semi-transparent gray
        self.text_color = (0, 0, 0)
        self.buttons = []

    def draw_buttons(self):
        self.buttons.clear()
        screen_width, screen_height = self.screen.get_size()
        start_y = (screen_height - (self.button_height * len(self.choices) + self.button_margin * (len(self.choices) - 1))) // 2

        for i, choice in enumerate(self.choices):
            button_x = (screen_width - self.button_width) // 2
            button_y = start_y + (self.button_height + self.button_margin) * i
            button_rect = pygame.Rect(button_x, button_y, self.button_width, self.button_height)
            self.buttons.append(button_rect)

            # Create a transparent surface for the button
            button_surface = pygame.Surface((self.button_width, self.button_height), pygame.SRCALPHA)
            pygame.draw.rect(button_surface, self.button_color, (0, 0, self.button_width, self.button_height))

            text = self.font.render(choice, True, self.text_color)
            text_rect = text.get_rect(center=(self.button_width // 2, self.button_height // 2))

            button_surface.blit(text, text_rect)
            self.screen.blit(button_surface, button_rect.topleft)

    def display(self):
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
                            print(f"Button {self.choices[i]} clicked")
                            # Transition to next screen or action
                            running = False