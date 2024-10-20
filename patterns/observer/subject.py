
from abc import ABC, abstractmethod
from typing import List
from patterns.observer.observer import Observer


class Subject(ABC):
    """
    Subject: An abstract base class representing the subject in the observer pattern.
    Manages a list of observers and notifies them of any changes.
    Attribute : 
    _observers(Observer): A empty list of observers
    """

    def __init__(self):
        """
        Initializes the Subject with an empty list of observers.
        """
        self._observers: List[Observer] = []

    @abstractmethod
    def attach(self, observer:Observer):
        """
        Attaches an observer to the subject.

        Args:
            observer (Observer): The observer to attach.
        """
        pass

    @abstractmethod
    def detach(self, observer:Observer):
        """
        Detaches an observer from the subject.

        Args:
            observer (Observer): The observer to detach.
        """
        pass

    @abstractmethod
    def notify(self, message:str):
        """
        Notifies all attached observers with a message.

        Args:
            message (str): The message to send to all observers.
        """
        pass

