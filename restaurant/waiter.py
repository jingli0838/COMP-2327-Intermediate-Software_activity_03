from patterns.observer.observer import Observer


class Waiter(Observer):
    """
    A class representing a Waiter.
    Attrs:
        __name (str): The name of the waiter. 
    """
    def __init__(self, name: str):
        """
        Initializes the Waiter class.
        Args:
            name (str): The name of the waiter. 
        """
        self.__name = name

    def __str__(self):
        """
        Returns a string representation of a Waiter instance.
        returns:
            string: A string representation of a Waiter instance.
        """
        return f"Waiter: {self.__name} is currently on duty."
    
    def update(self, message:str):
        """
        Receives a message and processes it as an update to the waiter.

        Args:
            message (str): The message sent to the waiter.

        Returns:
            string(str): a string including the messge and the waiter to whom the message will be sent.
        """
        print('Message to waiter {self.__name}: {message}')