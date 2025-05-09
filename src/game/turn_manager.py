class TurnManager():
    """Keeps track and updates the turns and moves made in the game.
    """
    def __init__(self, starting_player: bool):
        """The constructor for the TurnManager class. Creates player_turn and 
        current_move variables to keep track of the game.

        Args:
            starting_player (bool):
                The player that starts the game. Using a boolean, as this 
                is a 2 player game.
        """
        self.player_turn = starting_player
        self.current_move = None

    def get_turn(self):
        return self.player_turn

    def get_move(self):
        return self.current_move

    def update_turn(self):
        self.player_turn = not self.player_turn

    def update_move(self, next_move: int):
        self.current_move = next_move
