
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
    def attach(self, observer:Observer) -> None:
        """
        An abstract method attaching an observer to the subject.
        This method must be implemented by subclasses.
        
        Args:
            observer (Observer): The observer to attach.
        """
        pass

    @abstractmethod
    def detach(self, observer:Observer) -> None:
        """
        An abstract method detaching an observer from the subject.
        This method must be implemented by subclasses.

        Args:
            observer (Observer): The observer to detach.
        """
        pass

    @abstractmethod
    def notify(self, message:str) -> None:
        """
        An abstract method notifying all attached observers with a message.
        This method must be implemented by subclasses.
        
        Args:
            message (str): The message to send to all observers.
        """
        pass

