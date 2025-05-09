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
        """Gets the current player_turn value.

        Returns:
            int: Returns the player_turn variable.
        """
        return self.player_turn

    def get_move(self):
        """Gets the current_move value.

        Returns:
            int: Returns the current_move variable.
        """
        return self.current_move

    def update_turn(self):
        """Updates the player_turn variable to the next player.
        """
        self.player_turn = not self.player_turn

    def update_move(self, next_move: int):
        """Updates the current_move variable to the provided integer.

        Args:
            next_move (int):
                The integer which current_move variable will be updated to.
        """
        self.current_move = next_move
