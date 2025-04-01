from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def update():
        # Handle process of component
        pass

    @abstractmethod
    def draw():
        # Handle drawing of component
        pass