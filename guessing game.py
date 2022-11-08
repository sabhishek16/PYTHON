import random as r

num = r.randrange(50)
guess = 4

while guess >= 0:
    your_guess = int(input("enter your guess:"))

    def check(x):
        if your_guess == x:
            print('You Won')
        elif your_guess > x:
            print('you are close,keep trying lower')
        else:
            print('you are close keeep trying higher')

    if guess >1:
        check(num)
    elif guess ==1:
        check (num)
        print("This is your last chance!")
    else:
        print("you lost")

    guess = guess - 1
