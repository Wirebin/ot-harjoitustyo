from game.states import GameStates

class StateManager:
    """Class that manages the current game state and allows for switching
    between different game states.
    """
    def __init__(self):
        """The constructor for the StateManager. 
        """
        self.current_state = GameStates.MENU
        self.state_amount = len(GameStates)

    def next_state(self):
        """Switches a state to the next one by iterating the 
        current_state by one. Checks if current_state is over
        the state amount and prevents overflow.
        """
        if self.current_state.value >= self.state_amount:
            self.current_state = GameStates.MENU

        else:
            self.current_state = GameStates(self.current_state.value + 1)

    def go_to_state(self, state: GameStates):
        """Switches the current state to a specified state.
        If current_state is already in given state, do nothing.

        Args:
            state (GameStates): The state to be switched to.
        """
        if self.current_state == state:
            return
        self.current_state = state
