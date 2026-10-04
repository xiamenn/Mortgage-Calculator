# CNET-142 – Lab 4 – Menu Function
# Name: Xianhang Meng
# This program allows users to calculate simple interest or mortgage
# payments using predefined formulas.
# It provides a menu-based interface for entering loan
# details and displays formatted results including monthly payments,
# total payment, and interest paid.

import datetime
import math

def print_me_first():
    """
    Function name: print_me_first
    Function description: Prints student name and current time
    @return: None
    """
    print("Name: Xianhang Meng")
    now = datetime.datetime.now()
    print("Run Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_simple_interest(principal, rate, time):
    """
    Function name: calculate_simple_interest
    Function description: Calculates simple interest
    @param principal: loan amount
    @param rate: annual interest rate in percent
    @param time: loan duration in years
    @return: simple interest
    """
    return (principal * rate * time) / 100

def calculate_mortgage(loan_amount, interest_rate, loan_term_years):
    """
    Function name: calculate_mortgage
    Function description: Calculates monthly payment, total payment, and interest paid
    @param loan_amount: total loan amount
    @param interest_rate: annual rate in percent
    @param loan_term_years: loan duration in years
    @return: monthly_payment, total_payment, interest_paid
    """
    monthly_rate = (interest_rate / 100) / 12
    num_payments = loan_term_years * 12
    monthly_payment = loan_amount * monthly_rate * pow((1 + monthly_rate), num_payments) / \
                      (pow((1 + monthly_rate), num_payments) - 1)
    total_payment = monthly_payment * num_payments
    interest_paid = total_payment - loan_amount
    return monthly_payment, total_payment, interest_paid

def main():
    print_me_first()

    while True:
        print("\n" + "-" * 30)
        print("1     Calculate Simple Interest")
        print("2     Calculate Mortgage Payment")
        print("99    Quit the program")
        print("-" * 30)
        selection = input("\nSelect one of the command number above: ")

        if selection == "1":
            principal = 1000
            rate = 5
            time = 3
            interest = calculate_simple_interest(principal, rate, time)
            print(f"\nFor a principal of ${principal:.2f} at {rate:.2f}% for {time} years:")
            print(f"The simple interest is: ${interest:.2f}\n")

        elif selection == "2":
            while True:
                print()
                loan_input = input("Enter the loan amount, 0 to quit: ")
                if loan_input == "0":
                    break
                if not loan_input.replace('.', '', 1).isdigit():
                    print("Invalid input. Please enter a number.")
                    continue
                loan_amount = float(loan_input)

                rate_input = input("Enter the loan interest rate % : ")
                if not rate_input.replace('.', '', 1).isdigit():
                    print("Invalid input. Please enter a number.")
                    continue
                interest_rate = float(rate_input)

                term_input = input("Enter the loan term (number of years): ")
                if not term_input.isdigit():
                    print("Invalid input. Please enter a whole number.")
                    continue
                loan_term = int(term_input)

                monthly, total, interest = calculate_mortgage(loan_amount, interest_rate, loan_term)
                print(f"\nFor the loan Amount of ${loan_amount:,.2f} for  {loan_term} years with interest rate of {interest_rate:.2f} %")
                print(f"The monthly payment is ${monthly:,.2f}")
                print(f"Total amount paid for this loan is ${total:,.2f}")
                print(f"Total interest paid for this loan is ${interest:,.2f}\n")

        elif selection == "99":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid menu selection. Please try again.")

if __name__ == "__main__":
    main()