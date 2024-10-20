from patterns.observer.observer import Observer


class Chef(Observer):
    """
    A class representing a Chef.
    Attrs:
        __name (str): The name of the chef. 
    """
    def __init__(self, name: str):
        """
        Initializes the Chef class.
        Args:
            name (str): The name of the chef. 
        """
        self.__name = name

    def __str__(self):
        """
        Returns a string representation of a Chef instance.
        returns:
            string: A string representation of a Chef instance.
        """
        return f"Chef: {self.__name} is currently employed at the Restaurant."

    def update(self, message:str) ->None:
        """
        Receives a message from the subject and processes it.
        
        Args:
            message (str): The message sent from the subject.
        """
        print(f'Message to chef {self.__name}: {message}')