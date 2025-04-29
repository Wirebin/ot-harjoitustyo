from pygame import mouse

class OnePressInput:
    _prev_mouse_state = [0, 0, 0]
    _current_mouse_state = [0, 0, 0]

    @classmethod
    def is_mouse_clicked(cls, button_index: int):
        """
        Button index: 0 = left click,
                      1 = middle click,
                      2 = right click
        """

        # For left mouse button
        if button_index == 0:
            return cls._prev_mouse_state[0] and not cls._current_mouse_state[0]

        # For middle mouse button
        if button_index == 1:
            return cls._prev_mouse_state[1] and not cls._current_mouse_state[1]

        # For right mouse button
        if button_index == 2:
            return cls._prev_mouse_state[2] and not cls._current_mouse_state[2]


    @classmethod
    def update(cls):
        cls._prev_mouse_state = cls._current_mouse_state
        cls._current_mouse_state = mouse.get_pressed(3)
