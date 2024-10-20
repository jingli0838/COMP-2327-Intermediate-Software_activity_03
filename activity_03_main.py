""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Jing Li}
Date: {10/19/2024}
"""
from billing_account.billing_account import BillingAccount
from patterns.strategy.Interest_Payment_Strategy import InterestPaymentStrategy
from patterns.strategy.fixed_amount_penalty_strategy import FixedAmountPenaltyStrategy
from patterns.strategy.partial_payment_strategy import PartialPaymentStrategy
from patterns.strategy.penalty_strategy import PenaltyStrategy
from payee.payee import Payee
from payment.payment import Payment
from restaurant.busser import Busser
from restaurant.chef import Chef
from restaurant.dishwasher import Dishwasher
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
    print(penalty_payment.pay_bill(account, Payee.ELECTRICITY, 80.0))
    print("")
  
    # 1. Create a Payment object with a InterestePaymentStrategy payment strategy.
    try:
        interest_payment_strategy = Payment(InterestPaymentStrategy())
    except ValueError as e:
        print (e)
    # 2. Use the Payment object's pay_bill method to pay the INTERNET bill with 
    # an amount that does not pay off the entire balance shown above and the penalty should be calulated by the intereste rate
    # - print the result of the pay_bill method.


    print(interest_payment_strategy.pay_bill(account, Payee.INTERNET, 20.0))
    print("")

    # 1. Create a Payment object with a FixedAmountPenaltyStrategt payment strategy.
    try:
        fixed_amount_penalty_strategy = Payment(FixedAmountPenaltyStrategy())
    except ValueError as e:
        print (e)
    # 2. Use the Payment object's pay_bill method to pay the ELECTRICITY bill with 
    # an amount that does not pay off the entire balance shown above and the penalty should be calulated by the intereste rate
    # - print the result of the pay_bill method.

    print(fixed_amount_penalty_strategy.pay_bill(account, Payee.ELECTRICITY, 20.0))
    print("")



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

    #3. Create a Busser object and a dishwasher object with names of your choice.
    busser_01 = Busser("Joey")
    dishwasher_01 = Busser("Chandler")


    #4. Print each of the Chef and Waiter objects.
    print(chef_01)
    print(chef_02)
    print(waiter_01)
    print(waiter_02)
    print(busser_01)
    print(dishwasher_01)
    print("")

    #5. Attach one chef (of your choice) as a restaurant observer.
    restaurant.attach(chef_01)


    #6. Attach one waiter (of your choice) as a restaurant observer.
    restaurant.attach(waiter_02)

    #7. Add the following events:
    #   New dish added to the menu: Grilled Cheese Sandwich.
    #   Special promotion on desserts.
    #   We are out of tomatoes!
    # When the program executes, note who receives notification of the events
    # and who does not receive notification.
    restaurant.event("New dish added to the menu: Grilled Cheese Sandwich.")
    restaurant.event("Special promotion on desserts.")
    restaurant.event("We are out of tomatoes!")

    #   Add the following events:
    #   No more clean dishes.
    #   Table 03 need to be clean.
    print("")
    restaurant.detach(chef_01)
    restaurant.detach(waiter_02)
    restaurant.attach(dishwasher_01)
    restaurant.event("Get ready for additional dishes due to no more clean dishes.")
    
    restaurant.detach(dishwasher_01)
    restaurant.attach(busser_01)
    restaurant.event("Prepare for table 03 needs to be cleanup.")
    


if __name__ == "__main__":
    strategy()
    print("************************************")
    observer()