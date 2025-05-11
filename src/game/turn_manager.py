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
        self.winner = None

    def get_turn(self):
        """Gets the current player_turn value.

        Returns:
            bool: Returns the player_turn variable.
        """
        return self.player_turn

    def get_move(self):
        """Gets the current_move value.

        Returns:
            int: Returns the current_move variable.
        """
        return self.current_move

    def get_winner(self):
        """Gets the winner of the game

        Returns:
            bool: Returns the winner of the game.
        """
        return self.winner

    def update_turn(self, next_turn: bool):
        """Updates the player_turn variable to the next player.

        Args:
            next_turn (bool):
                The boolean which player_turn variable will be updated to.
        """
        self.player_turn = next_turn

    def update_move(self, next_move: int):
        """Updates the current_move variable to the provided integer.

        Args:
            next_move (int):
                The integer which current_move variable will be updated to.
        """
        self.current_move = next_move

    def set_winner(self, winner: bool):
        """Sets the winner of the game as boolean.

        Args:
            winner (bool): 
                The winner of the game. False for X/Cross and True for O/Circle.
        """
        self.winner = winner
