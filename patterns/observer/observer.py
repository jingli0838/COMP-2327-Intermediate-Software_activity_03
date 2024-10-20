

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Observer: An abstract base class for defining the observer in the observer pattern.
    """
    @abstractmethod
    def update(self, message:str) ->None:
        """
        An abstract method receiving a message from the subject and processing it.
        This method must be implemented by subclasses.
        
        Args:
            message (str): The message sent from the subject.
        """
        pass
