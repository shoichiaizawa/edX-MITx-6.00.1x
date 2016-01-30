def paying_the_minimum(balance, annualInterestRate, monthlyPaymentRate):
    """Calculate minimum monthly payment amount, remaining balance
       and total amount paid

    Calculate minimum monthly payment amount and remaining balance each month,
    and print to screen in the following format:

        ```
        Month: month
        Minimum monthly payment: monthlyPayment
        Remaining balance: balance
        ```

    And then, print out the total amount paid and the remaining balance at the
    end.

    Args:
        balance: the outstanding balance on the credit card
        annualInterestRate: annual interest rate as a decimal
        monthlyPaymentRate: minimum monthly payment rate as a decimal

    Returns:
        None

    Raises:
        TypeError: if balance is not a number
        TypeError: if annualInterestRate is not a number
        TypeError: if monthlyPaymentRate is not a number

    """
    monthlyInterestRate = annualInterestRate / 12.0
    totalPaid = 0
    for month in range(1, 13):
        monthlyPayment = monthlyPaymentRate * balance
        totalPaid += monthlyPayment
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + \
            monthlyInterestRate * monthlyUnpaidBalance
        print 'Month: ' + str(month)
        print 'Minimum monthly payment: %.2f' % monthlyPayment
        print 'Remaining balance: %.2f' % balance

    print 'Total paid: %.2f' % totalPaid
    print 'Remaining balance: %.2f' % balance


#  paying_the_minimum(balance, annualInterestRate, monthlyPaymentRate)
paying_the_minimum(4213, 0.2, 0.04)
paying_the_minimum(4842, 0.2, 0.04)


###############################################################################

#  NOTE: some maths to do

#  - Monthly interest rate = (Annual interest rate) / 12.0
#  - Minimum monthly payment = \
#        (Minimum monthly payment rate) x (Previous balance)
#  - Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#  - Updated balance each month = (Monthly unpaid balance) + \
#        (Monthly interest rate x Monthly unpaid balance)

########################################

# NOTE: round to n decimal place

#  round(value, 2) ==> e.g. round(813.4141998135, 2) corrected to 814.41
