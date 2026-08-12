# scope rules

# code outside all function (global scope) can not use local variable
# a local variable in one function can not be use in another local variable (different function)
# code in local scope CAN access global variable (read only, not modify)
# local variable and global variable can have same name, they dont clash, treated separate

# for larger program, or medium size program should avoid the global variable
# because of bug, and difficult to modify or replace in production grade code 

def spam():
    egg = 'got from supermarket'
    burger()
    print(egg)

def burger():
    beef = 'got from farm'
    print(beef)
spam() # when call the spam() function, first it set a variable name egg and store
#massage on it. then call burger() function. inside the burger function 
# have beef variable which also store string value 

#when we run this program output as 
# got from farm
# got from supermarket


# code that in local space can use global variable 

def test_scope():
    print('from local variable')
egg = 'global variable'
test_scope()
print(egg)

#output 
# from local variable
# global variable

#Global scope rule 
# global variable outside all function is a global scope 
# a variable in a function with global statement is always global variable

def practice_global_scope():
    global cow # global variable
    cow = 'biriyani with beef'
    print('global variable cow')
def another_scope():
    goat = 'cooking biriyani' # local variable
    print(goat)

def cooking():
    print(cow)
cow = 'global biriyani'
practice_global_scope()
print(cow)
another_scope()

# output
# global variable
# global variable cow
# biriyani with beef
# cooking biriyani