import random

print('This is a guessing game!')
random_number = random.randint(1, 20)

attempts = 1

while attempts <= 3:
    guess = int(input('Guess a number between 1 and 20: '))
    if guess == random_number:
        print('Congratulations, You Got It!')
        break
    else:
        print('Oops wrong! Please try again!')
        attempts += 1

if attempts == 4:
    print('You are out of tries. The number was', random_number)