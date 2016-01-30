def paying_debt(balance, annualInterestRate):
    """Calculate the minimum monthly payment rate

    This function calculates the minimum monthly payment rate
    using an iterative method.

    For each while loop iteration, with a fixed monthly payment rate
    starting from 10, this function calculates the yearly unpaid balance
    every month for a year using a for loop.
    If the yearly unpaid balance stays positive at the end of
    each 12 month calculation, meaning there is still outstanding balance
    to be paid; hence, continue the while loop with the newly defined
    fixed monthly payment rate increased by 10 from the previous value.

    This continues until the yearly unpaid balance goes negative, meaning
    no more outstanding balance, the fixed monthly payment rate meets this
    condition will be the minimum monthly payment rate.

    Args:
        balance: the outstanding balance on the credit card
        annualInterestRate: annual interest rate as a decimal

    Returns:
        None

    Raises:
        TypeError: if balance is not a number
        TypeError: if annualInterestRate is not a number

    """
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPayment = 10
    step = 10
    paid = False

    while not paid:
        yearlyUnpaidBalance = balance
        for month in range(1, 13):
            monthlyUnpaidBalance = yearlyUnpaidBalance - monthlyPayment
            yearlyUnpaidBalance = monthlyUnpaidBalance + \
                (monthlyInterestRate * monthlyUnpaidBalance)
        if yearlyUnpaidBalance > 0:
            monthlyPayment += step
        else:
            paid = True

    print 'Lowest Payment: ' + str(monthlyPayment)


#  Test cases:
#  paying_debt(balance, annualInterestRate)
paying_debt(3329, 0.2)  # ==> Lowest Payment: 310
paying_debt(4773, 0.2)  # ==> Lowest Payment: 440
paying_debt(3926, 0.2)  # ==> Lowest Payment: 360


###############################################################################

#  NOTES: some maths required

#  - Monthly interest rate = (Annual interest rate) / 12.0
#  - Monthly unpaid balance = (Previous balance) - \
#        (Minimum fixed monthly payment)
#  - Updated balance each month = (Monthly unpaid balance) + \
#        (Monthly interest rate x Monthly unpaid balance)
