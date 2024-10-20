""
from abc import ABC, abstractmethod

from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PayementStrategy(ABC):
    """
    PaymentStrategy: An abstract base class for defining payment strategies.
    """

    @abstractmethod
    def process_payment(self, account:BillingAccount, payee:Payee, amount:float) -> str:
        """
        An abstractmethod to process a payment for a specified account, payee, and amount.
        This method must be implemented by subclasses.

        Args:
            account (BillingAccount): The billing account to be charged.
            payee (Payee): The payee to whom the payment is made.
            amount (float): The amount to be paid.

        Returns:
            str: A message indicating the result of the payment process.
        """
        pass;  

