def collatz(nunber):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

try:
    user_input = input('Enter any number')
    number = int(user_input)

    while number != 1:
        number = collatz(number)
except ValueError:
    print('you must enter integer number like 1,2,3')


#output 
# Enter any number 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
