
from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PayementStrategy
from payee.payee import Payee


class InterestPaymentStrategy(PayementStrategy):
    """
    Applies interest to the remaining balance if the payment is not made in full.
    """
     
    def process_payment(self, account:BillingAccount, payee:Payee, amount:float) -> str:
        """
        Processes a payment for a specified account, payee, and amount.
        And applies interest if the balance is not paid in full.

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
           interest_rate = 0.1
           penalty_fee = interest_rate * new_balance
           # add the penalty fee to new balance
           account.add_balance(payee,penalty_fee)
           # uptade the balance of the account
           new_balance = account.get_balance(payee)
           return f'Insufficient payment. Added penalty fee of ${penalty_fee:.2f}. New balance: ${new_balance:.2f}.'



