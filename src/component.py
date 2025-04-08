from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def update():
        # Handle updating of component
        pass

    @abstractmethod
    def draw():
        # Handle drawing of component
        pass