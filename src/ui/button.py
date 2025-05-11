import pygame
from input.one_press_input import OnePressInput
from config.constants import BUTTON_COLOR_NORMAL, BUTTON_COLOR_HOVER

class Button():
    """Class for creating a button object that includes a click event.
    """
    def __init__(self,
                 location: tuple,
                 size: tuple,
                 button_text: str,
                 on_click):
        """The constructor of the class. Creates an instance of a button.

        Args:
            location (tuple): 
                The location of the button's top left corner. Given as a tuple (x, y)
                where x is the x coordinate and y is the y coordinate in 2d space.
            size (tuple): 
                The size of the button as a tuple (x, y) where x is the width
                and y is the height of the button.
            button_text (str): 
                The text that is displayed on the button.
            on_click:
                The function that is called when the button is pressed. Without specifying
                a function here, the button won't work. 
        """
        self.location = location
        self.size = size

        self.button_rect = pygame.Rect(self.location[0],
                                       self.location[1],
                                       self.size[0],
                                       self.size[1])

        self.button_text = button_text
        font = pygame.font.Font(None, self.button_rect.height - 10)
        self.button_text_render = font.render(button_text, True, (0,0,0))
        self.button_text_rect = self.button_text_render.get_rect(center=self.button_rect.center)

        self.on_click = on_click

    def update(self):
        """Used to update the button object logic.

        If mouse is clicked on top of the button, the update calls the on_click() function
        """
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) and \
            OnePressInput.is_mouse_clicked(0):
            self.on_click()

    def draw(self, canvas):
        """This function handles the drawing of the button on to the canvas.
        Changes color to indicate whether mouse is currently hovering over button.

        Args:
            canvas (pygame.Surface): 
                The display canvas used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(canvas, BUTTON_COLOR_HOVER, self.button_rect)
        else:
            pygame.draw.rect(canvas, BUTTON_COLOR_NORMAL, self.button_rect)

        canvas.blit(self.button_text_render, self.button_text_rect)
        