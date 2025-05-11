import pygame
from ui.text import Text
from input.one_press_input import OnePressInput
from config.constants import BUTTON_COLOR_NORMAL, BUTTON_COLOR_HOVER, BLACK_COLOR

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
        self._location = location
        self._size = size

        self._button_rect = pygame.Rect(self._location[0],
                                       self._location[1],
                                       self._size[0],
                                       self._size[1])

        self._text = Text(self._button_rect.center,
                         self._button_rect.height - 10,
                         BLACK_COLOR,
                         button_text,
                         "center")
        self._on_click = on_click

    def update(self):
        """Used to update the button object logic.

        If mouse is clicked on top of the button, the update calls the _on_click() function
        """
        if self._button_rect.collidepoint(pygame.mouse.get_pos()) and \
            OnePressInput.is_mouse_clicked(0):
            self._on_click()

    def draw(self, canvas):
        """This function handles the drawing of the button on to the canvas.
        Changes color to indicate whether mouse is currently hovering over button.

        Args:
            canvas (pygame.Surface): 
                The display canvas used for pygame. Necessary in order
                to use the draw function of pygame.
        """
        if self._button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(canvas, BUTTON_COLOR_HOVER, self._button_rect)
        else:
            pygame.draw.rect(canvas, BUTTON_COLOR_NORMAL, self._button_rect)

        self._text.draw(canvas)
        