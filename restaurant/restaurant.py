
from patterns.observer.observer import Observer
from patterns.observer.subject import Subject


class Restaurant(Subject):
    """
    A class representing a Restaurant that acts as a subject in the observer pattern.
    
    Attributes:
        _observers (list): A list of attached observers (inherited).
        message (str): The message to be sent to observers.
    """

    def __init__(self):
        """
        Initializes the Restaurant class.
        Executes the __init__ of the superclass to initialize the observers list.
        Sets the message attribute to an empty string.
        """
        super().__init__()
        self.__message = ""
    
    def attach(self, observer:Observer):
        """
        Attaches an observer to the restaurant's observer list.
        
        Args:
            observer (Observer): The observer to be attached.
        """

        self._observers.append(observer)

    def detach(self, observer:Observer):
        """
        Detaches an observer from the restaurant's observer list.
        
        Args:
            observer (Observer): The observer to be detached.
        """
        
        self._observers.remove(observer)

    def notify(self, message:str) -> None:
        """
        Notifies all attached observers with a message.
        
        Args:
            message (str): The message to send to observers.
        """
        for observer in self._observers:
            observer.update(message)
    
    def event(self, message:str) -> None:
        """
         Updates the message attribute and notifies all observers of an event.
        
        Args:
            message (str): The event message to be set and sent to observers.
        """
        self.__message = message
        self.notify(self.__message)
