#create a function and pass the three time fahim
# def fahim():
#     print('fahim 1')
#     print('fahim 2')
#     print('fahim 3')

# fahim()
# fahim()
# fahim()

#arguments and parameters

# def add_name(name): # arguments are value that pass in the function
#     print('bethel'+ name)
#     print('root' + name)
#     print('brook' + name)

# add_name('ben stokes') # parameters are variable where store the program
# add_name('Morgan')

# return value and return statements

# write a program that define a function and return a different string
# depending the number it pass 
# 
# if number 1 pass then return random string , so we need random function
# 

import random

def random_number_game(number):
 if number == 1:
  return 'Australia ranked number 1 team in test'
 elif number == 2:
  return 'England is not qualify for WTC final'
 elif number == 3:
  return 'Nz won the test series in england tour 2026 after two decade'
 elif number == 4:
  return 'Buzz and stokes have called of their test duty'

print('please select number in between 1 to 4')
store = input('>')

random_number = random.randint(1,4)
user_select = random_number_game(random_number)
print(user_select)

# None value define with capital N, None. it is helpful when value
# could not confused with real value. 
# Name parameters
 


