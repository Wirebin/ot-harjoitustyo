from states import GameStates

class StateManager:
    def __init__(self):
        self.current_state = GameStates.MENU
        self.state_amount = len(GameStates)

    def next_state(self):
        # If state value is over the limit, go back to the first one.
        if self.current_state.value >= self.state_amount:
            self.current_state = GameStates.MENU

        # Otherwise increase state by one / move to the next state.
        else:
            self.current_state = GameStates(self.current_state.value + 1)
