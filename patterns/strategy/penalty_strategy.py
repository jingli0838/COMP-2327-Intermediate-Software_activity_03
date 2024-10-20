""
from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PayementStrategy
from payee.payee import Payee


class PenaltyStrategy(PayementStrategy):
    """
    PenaltyStrategy: A payment strategy that applies a penalty if the amount
    owing is not paid in full.
    """

    def process_payment(self, account:BillingAccount, payee:Payee, amount:float) -> str:
        """
        Processes a payment for a specified account, payee, and amount.
        If the payment is insufficient to cover the balance, a penalty of $10 is applied.

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
            return f'Processed payment of ${amount}. New balance: ${new_balance:.2f}.'
        else:
           # If balance is not paid in full, apply a penalty
           account.add_balance(payee,10.0)
           new_balance = account.get_balance(payee)
           return f'Insufficient payment. Added penalty fee of $10.00. New balance: ${new_balance:.2f}.'
        
        



