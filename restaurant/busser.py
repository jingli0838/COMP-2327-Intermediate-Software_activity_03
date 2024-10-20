from patterns.observer.observer import Observer


class Busser(Observer):
    """
    A class representing a busser.
    Attrs:
        __name (str): The name of the busser. 
    """
    def __init__(self, name: str):
        """
        Initializes the Busser class.
        Args:
            name (str): The name of the Busser. 
        """
        self.__name = name

    def __str__(self):
        """
        A string representation of a Busser's status.

        returns:
            string: A string representation of a Busser's status.
        """
        return f"Busser: {self.__name} is currently on duty."

    def update(self, message:str) ->None:
        """
        Receives a message and processes it as an update to the busser.

        Args:
            message (str): The message sent to the busser.

        Returns:
            string(str): a string including the messge and the busser to whom the message will be sent.
        """
        print(f'Message to busser {self.__name}: {message}') 
