def paying_debt_bs(balance, annualInterestRate):
    """Calculate the minimum monthly payment rate

    This function calculates the minimum `monthlyPayment` rate
    using a bisection search method.

    For every while iteration, this function firstly calculates
    the `monthlyPayment` rate, which is given by:

    `monthlyPayment = (lowerBound + upperBound) / 2.0`

    , whose initial `lowerBound` and `upperBound` are defined before entering
    the while loop, as:

        - `lowerBound = balance / 12.0`; and,
        - `upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0`.

    And based on the `monthlyPayment` rate calculated at the beginning of each
    while iteration, this function updates the `yearlyUnpaidBalance` for
    every month for one year length using a for loop, and evaluates whether
    the resultant `yearlyUnpaidBalance` after the 12 for loop iterations is
    greater than 0.01 or less than -0.01.

    Concretely, if the resultant `yearlyUnpaidBalance` value is greater than
    0.01, then this means that there will still be the outstanding balance
    to be paid even after one year, indicating the previous `monthlyPayment`
    rate was not large enough to pay off the debt.
    Now the program continues to the next while iteration
    with the updated monthly payment `lowerBound`
    being the previous `monthlyPayment` rate.

    Conversely, if the resultant `yearlyUnpaidBalance` value is less than
    -0.01, then this means that there will be too much payment over one year
    as the `monthlyPayment` rate was too large.
    Now the program continues to the next while iteration
    with the updated monthly payment 'upperBound'
    being the previous `monthlyPayment` rate.

    The program continues until meeting the following condition
    such that, NEITHER:

        - `yearlyUnpaidBalance` is greater than 0.01; NOR
        - `yearlyUnpaidBalance` is less than -0.01.

    The `monthlyPayment` rate meeting the conditions above will be the minimum
    `monthlyPayment` rate to pay off the debt.

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
    epsilon = 0.01
    # guessCount = 0
    lowerBound = balance / 12.0
    upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
    yearlyUnpaidBalance = balance

    while yearlyUnpaidBalance > epsilon or yearlyUnpaidBalance < -epsilon:
        yearlyUnpaidBalance = balance
        monthlyPayment = (lowerBound + upperBound) / 2.0
        # guessCount += 1
        # print 'guessCount: %d' % guessCount
        # print 'lowerBound: %.2f, upperBound: %.2f, monthlyPayment: %.2f' % \
        #     (lowerBound, upperBound, monthlyPayment)
        for month in range(1, 13):
            monthlyUnpaidBalance = yearlyUnpaidBalance - monthlyPayment
            yearlyUnpaidBalance = monthlyUnpaidBalance + \
                (monthlyInterestRate * monthlyUnpaidBalance)
        if yearlyUnpaidBalance > epsilon:
            # print 'yearlyUnpaidBalance: %f -> Not enough payment!\n' % \
            #     yearlyUnpaidBalance
            lowerBound = monthlyPayment
        elif yearlyUnpaidBalance < -epsilon:
            # print 'yearlyUnpaidBalance: %f -> Too much payment!\n' % \
            #     yearlyUnpaidBalance
            upperBound = monthlyPayment
        # else:
        #     print 'yearlyUnpaidBalance: %f' % yearlyUnpaidBalance
        #     print 'Success! Now yearlyUnpaidBalance is neither:\n' \
        #         '- greater than 0.01; nor\n' \
        #         '- less than -0.01.\n'

    # print 'Total guessCount: %d' % guessCount
    print 'Lowest Payment: %.2f' % monthlyPayment


# Test cases:
# paying_debt_bs(balance, annualInterestRate)
paying_debt_bs(320000, 0.2)     # ==> Lowest Payment: 29157.09
paying_debt_bs(999999, 0.18)    # ==> Lowest Payment: 90325.03

###############################################################################

# NOTES: some maths required

# - Monthly interest rate = (Annual interest rate) / 12.0
# - Monthly payment lower bound = Balance / 12
# - Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) \
#       / 12.0
