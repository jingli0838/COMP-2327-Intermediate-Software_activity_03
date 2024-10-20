
from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PayementStrategy
from payee.payee import Payee

class Payment():
    """
    Payment class that uses a specified PaymentStrategy to process payments.
    Attributes:
        __strategy(PayementStrategy): The strategy to be used for processing payments.
    """
    def __init__(self, strategy:PayementStrategy):
        """
        Initializes the Payment class with a given payment strategy.
        Args:
            strategy (PaymentStrategy): The strategy to be used for processing payments.
        Raises:
            ValueError: If the strategy is not an instance of PaymentStrategy.
        """
        if isinstance(strategy, PayementStrategy):
            self.__strategy = strategy
        else:
            raise ValueError("Invalid Strategy")

    def pay_bill(self, account: BillingAccount, payee: Payee, amount: float) ->str:
        """
        Uses the assigned strategy to process a payment.

        Args:
            account (BillingAccount): The billing account to be charged.
            payee (Payee): The payee to whom the payment is made.
            amount (float): The amount to be paid.

        Returns:
            str: The result of the payment process, as provided by the strategy.
        """
        return self.__strategy.process_payment(account,payee,amount)
    


        