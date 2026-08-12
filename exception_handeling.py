# divided by zero error 

# def count_number(number):
#     return 42 / number
# print(count_number(2))
# print(count_number(4))

# at this point output will be 
# 21.0
# 10.5

# now want to divided by zero 
# def count_number(number):
#     return 42 / number
# print(count_number(2))
# print(count_number(4))
# print(count_number(0))

#output
# count_number
#     return 42 / number
# ZeroDivisionError: division by zero , it shows we can not divided by zero error 

# Error can be handled with try and clause statement. 
# the potential error code put into the try statement

def count_number(number):
    try:
        return 50 / number
    except ZeroDivisionError:
        print("Error! Invalid argument, try any value except 0")
print(count_number(4))
print(count_number(10))
print(count_number(0))

#After run output as 
# 12.5
# 5.0
# Error! Invalid argument, try any value except 0
# None


