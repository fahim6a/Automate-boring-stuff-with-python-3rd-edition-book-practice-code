#write down a code where take input from users and match the value, 
# if users guess the right , show massage it is right 
# if guess wrong number then give them hint such as low, high 
# also count how many times need them to make it right 

import random
total_number = random.randint(1,50)
print('Guess the number in between 1 to 50')

#ask user guess 10 times 
for guess_taken in range(1,11):
    print('take a guess')
    guess =  int(input('>'))

    if guess < total_number:
        print('too low')
    elif guess > total_number:
        print('too high')
    else:
        break
    if guess == total_number:
        print('great job, you guess it right in' + str(guess_taken) + 'guess')
    else:
        print('the number was' + str(total_number))





