from states import Game_States

class State_Manager:
    def __init__(self):
        self.current_state = Game_States.MENU
        self.state_amount = len(Game_States)

    def next_state(self):
        # If state value is over the limit, go back to the first one.
        if self.current_state.value >= self.state_amount:
            self.current_state = Game_States.MENU

        # Otherwise increase state by one / move to the next state.
        else:
            self.current_state = Game_States(self.current_state.value + 1)


    # def go_to_state(self, state: Game_States):
    #     # If specified state exists, set it as current.
    #     if state in Game_States:
    #         self.current_state = state

