low = 0
high = 100

print 'Please think of a number between 0 and 100!'

while True:
    guess = (low+high)/2
    print
    print 'Is your number ' + str(guess) + '?'
    ans = raw_input("1. Enter 'h' to indicate the guess is too high.\n"
                    "2. Enter 'l' to indicate the guess is to low.\n"
                    "3. Enter 'c' to indicate I guessed correctly.\n"
                    "Your answer (h/l/c): ")
    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    elif ans == 'c':
        print 'Game over. Your secret number was: ' + str(guess)
        break
    else:
        print 'Sorry, I did not understand your input.'
