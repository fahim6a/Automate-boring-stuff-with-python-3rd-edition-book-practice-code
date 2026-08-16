#Assertion check the code behave like we want or not 

# age =[15,85,45,32,54,75,69,11,40]
# age.sort()
# print(age)
# assert age[0]<=age[1] # first age is less than or equal to last age

#output
# [11, 15, 32, 40, 45, 54, 69, 75, 85]

#what if we use reverse() function instead of sort() function

age =[15,85,45,32,54,75,69,11,40]
age.reverse()
print(age)
assert age[0]<=age[1] # first age is less than or equal to last age

#output 
# [40, 11, 69, 75, 54, 32, 45, 85, 15]
# Traceback (most recent call last):
#   File "i:\Coding Skill\Python\Chapter 1 Fundamentals\Assertions.py", line 16, in <module>
#     assert age[0]<=age[1] # first age is less than or equal to last age
# AssertionError

# this type of error user will never seen that
# because we dont handle exception so that it crushed
