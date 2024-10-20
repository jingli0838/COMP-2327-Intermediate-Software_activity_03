

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Observer: An abstract base class for defining the observer in the observer pattern.
    """
    @abstractmethod
    def update(self, message:str) ->None:
        """
        Receives a message from the subject and processes it.

        Args:
            message (str): The message sent from the subject.
        """
        pass
