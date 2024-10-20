""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Jing Li}
Date: {10/19/2024}
"""
from billing_account.billing_account import BillingAccount
from patterns.strategy.partial_payment_strategy import PartialPaymentStrategy
from patterns.strategy.penalty_strategy import PenaltyStrategy
from payee.payee import Payee
from payment.payment import Payment
from restaurant.chef import Chef
from restaurant.restaurant import Restaurant
from restaurant.waiter import Waiter

def strategy():
    print("STRATEGY PATTERN OUTPUT")

    # Given: Creates a BillingAccount object and 
    # adds the current balance owed for each utility.
    account = BillingAccount()
    account.add_balance(Payee.ELECTRICITY, 200.0)
    account.add_balance(Payee.INTERNET, 100.0)
    account.add_balance(Payee.TELEPHONE, 150.0)

    print("Initial Balances:")
    print(account, "\n")

    # 1. Create a Payment object with a PenaltyStrategy payment strategy.
    try:
        penalty_payment = Payment(PenaltyStrategy())
    except ValueError as e:
        print(e)

    # 2. Use the Payment object's pay_bill method to pay the ELECTRICITY bill with 
    # an amount that does not pay off the entire balance shown above - print the 
    # result of the pay_bill method.
    print(penalty_payment.pay_bill(account, Payee.ELECTRICITY, 180.0))

    


    # 3. Create a Payment object with a PartialPaymentStrategy payment strategy.
    try:
        partial_payment = Payment(PartialPaymentStrategy())
    except ValueError as e:
        print(e)

    # 4. Use the Payment object's pay_bill method to pay the TELEPHONE bill with 
    # an amount that does not pay off the entire balance shown above - print the 
    # result of the pay_bill method.
    print(partial_payment.pay_bill(account, Payee.TELEPHONE, 130.0))

    # 5. Using the Payment object created in step 3, make another payment for the 
    # TELEPHONE bill with an amount that pays off the remainder of the balance - print 
    # the result of the pay_bill method.
    print(partial_payment.pay_bill(account, Payee.TELEPHONE, 20.0))

    # 6. Print the BillingAccount object to show the updated balances for each of the payees.
    print("")
    print("Updated Balances:")
    print(account,"\n")

def observer():
    print("OBSERVER PATTERN OUTPUT")
    # 1. Create a Restaurant object.
    restaurant = Restaurant()

    #2. Create two Chef objects with names of your choice.
    chef_01 = Chef("Ross")
    chef_02 = Chef("Monica")
    
    #3. Create two Waiter objects with names of your choice.
    waiter_01 = Waiter("Rachel")
    waiter_02 = Waiter("Phebee")


    #4. Print each of the Chef and Waiter objects.
    print(chef_01)
    print(chef_02)
    print(waiter_01)
    print(waiter_02)
    

    #5. Attach one chef (of your choice) as a restaurant observer.
    chef_03 = Chef("Bob")
    restaurant.attach(chef_03)


    #6. Attach one waiter (of your choice) as a restaurant observer.
    waiter_03 = Waiter("Lucy")
    restaurant.attach(waiter_03)

    #7. Add the following events:
    #   New dish added to the menu: Grilled Cheese Sandwich.
    #   Special promotion on desserts.
    #   We are out of tomatoes!
    # When the program executes, note who receives notification of the events
    # and who does not receive notification.
    



if __name__ == "__main__":
    strategy()
    print("************************************")
    observer()