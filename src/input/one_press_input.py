from pygame import mouse

class OnePressInput:
    """Class responsible for detecting singular mouse inputs.
    It is used as a static class that is shared across all other classes.
    """
    _prev_mouse_state = [0, 0, 0]
    _current_mouse_state = [0, 0, 0]

    @classmethod
    def is_mouse_clicked(cls, button_index: int):
        """Used to check whether the mouse is pressed by comparing the 
        previous mouse state with the current mouse state and seeing if they 
        are different.

        Button indexes are as follows:
            0 = left click
            1 = middle click
            2 = right click

        Args:
            button_index (int): The index used to differentiate between mouse buttons.

        Returns:
            bool: Returns True, if previous mouse state and current mouse state 
            are different. 
        """
        if button_index == 0:
            return cls._prev_mouse_state[0] and not cls._current_mouse_state[0]

        if button_index == 1:
            return cls._prev_mouse_state[1] and not cls._current_mouse_state[1]

        if button_index == 2:
            return cls._prev_mouse_state[2] and not cls._current_mouse_state[2]


    @classmethod
    def update(cls):
        """Changes the _prev_mouse_state to the _current_mouse_state and
        updates the _current_mouse_state to a new state.

        This keeps _prev_mouse_state one frame behind _current_mouse_state.
        """
        cls._prev_mouse_state = cls._current_mouse_state
        cls._current_mouse_state = mouse.get_pressed(3)
