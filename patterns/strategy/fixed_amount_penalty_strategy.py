

from billing_account.billing_account import BillingAccount
from patterns.strategy.payment_strategy import PayementStrategy
from payee.payee import Payee


class FixedAmountPenaltyStrategy(PayementStrategy):

    def process_payment(self, account:BillingAccount, payee:Payee, amount:float) -> str:
        """
        Processes a payment for a specified account, payee, and amount.
        And Applies a fixed penalty to the remaining balance based on the payment amount.

        Args:
            account (BillingAccount): The billing account to be charged.
            payee (Payee): The payee to whom the payment is made.
            amount (float): The amount to be paid.

        Returns:
            str: A message indicating the result of the payment process and any penalty applied.
        """
        # Apply a payment to the account
        account.deduct_balance(payee,amount)

        # uptade the balance of the account
        new_balance = account.get_balance(payee)

        if new_balance <= 0.0:
            return f'Processed payment of ${amount:.2f}. New balance: ${new_balance:.2f}.'
        
        elif new_balance > 0.0 and new_balance <= 100.0:
        
           # add the penalty fee to new balance
           account.add_balance(payee,10.0)
           new_balance = account.get_balance(payee)
           return f'Insufficient payment. Added penalty fee of $10.0. New balance: ${new_balance:.2f}.'
        
        elif new_balance > 100.0:
            # add the penalty fee to new balance
           account.add_balance(payee,20.0)
           new_balance = account.get_balance(payee)
           return f'Insufficient payment. Added penalty fee of $20.0. New balance: ${new_balance:.2f}.'



