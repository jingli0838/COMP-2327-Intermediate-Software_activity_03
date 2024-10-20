from patterns.observer.observer import Observer


class Dishwasher(Observer):
    """
    A class representing a dishwasher.
    Attrs:
        __name (str): The name of the dishwasher. 
    """
    def __init__(self, name: str):
        """
        Initializes the dishwasher class.
        Args:
            name (str): The name of the dishwasher. 
        """
        self.__name = name

    def __str__(self):
        """
        A string representation of a dishwasher's status.
        
        returns:
            string: A string representation of a dishwasher's status.
        """
        return f"Dishwasher: {self.__name} is currently on duty."
    
    def update(self, message:str) -> None:
        """
        Receives a message and processes it as an update to the dishwasher.

        Args:
            message (str): The message sent to the dishwasher.

        Returns:
            string(str): a string including the messge and the dishwasher to whom the message will be sent.
        """
        print(f'Message to dishwasher {self.__name}: {message}')