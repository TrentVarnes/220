"""
Name: Trent
File: Interest.py
I certify that this is all my work
"""

#compute monthly interest charge on credit card account
#acquire input from information provided
#calculate and output monthly interest charge
#only monthly interest charge should be output


def main():
    annual_interest_rate = eval(input("enter annual interest rate here: "))
    number_of_days_in_billing_cycle = eval(input("enter number of days in billing cycle here: "))
    previous_net_balance = eval(input("enter net balance here: "))
    payment_amount = eval(input("enter payment amount here: "))
    day_payment_was_made = eval(input("enter day payment received here: "))
    step_1 = previous_net_balance * number_of_days_in_billing_cycle
    step_2 = payment_amount * (number_of_days_in_billing_cycle - day_payment_was_made)
    step_3 = step_1 - step_2
    step_4 = step_3 / number_of_days_in_billing_cycle
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_interest_charge = step_4 * monthly_interest_rate
    answer = round(monthly_interest_charge, 2)
    print(answer)


if __name__ == 'main':
    main()
