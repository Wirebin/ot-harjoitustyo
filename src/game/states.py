from enum import Enum

class GameStates(Enum):
    """Different game states used by the game. 
    Can be switched when used with StateManager.

    Args:
        Enum (int): Specific game state.
    """
    MENU = 1
    GAME = 2
    RESULT = 3
