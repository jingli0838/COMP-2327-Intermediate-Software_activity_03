
""

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PayementStrategy
from payee.payee import Payee


class PartialPaymentStrategy(PayementStrategy):
    """
    PartialPaymentStrategy: A concrete strategy that allows partial payments.
    Applies a payment to a specified BillingAccount and updates the balance.
    """

    def process_payment(self, account:BillingAccount, payee:Payee, amount:float) -> str:
        """
        Processes a partial payment for a specified account, payee, and amount.

        Args:
            account (BillingAccount): The billing account to be charged.
            payee (Payee): The payee to whom the payment is made.
            amount (float): The amount to be paid.

        Returns:
            str: A message indicating the result of the payment process.
        """
        # Apply a payment to the account
        account.deduct_balance(payee,amount)
        # uptade the balance of the account
        new_balance = account.get_balance(payee)

        if new_balance <= 0.0:
            return f'Processed payment of ${amount}. New balance: ${new_balance}.'
        else:
            return f'Partial payment of ${amount} accepted. New balance: ${new_balance}.'
        
        
       
