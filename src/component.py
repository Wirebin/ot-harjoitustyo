from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def update(self):
        # Handle updating of component
        pass

    @abstractmethod
    def draw(self, screen):
        # Handle drawing of component
        pass
