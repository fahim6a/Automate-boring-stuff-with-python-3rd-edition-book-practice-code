# use of range(len(list)) 

# cricket = ['eng','aus','ind','ban','nz','sa','sl','pak']
# for i in range(len(cricket)):
#     print('the total nations are: '+ i)


# the total nations are: 0
# the total nations are: 1
# the total nations are: 2
# the total nations are: 3
# the total nations are: 4
# the total nations are: 5
# the total nations are: 6
# the total nations are: 7

#in and not in operators

#The following program lets the user enter a pet name and then checks 
#whether the name is in a list of pets



my_pet = ['cats','crocodile','dog','lion','tiger','cow','goat']

while True:
         print("enter your pets name: ")
         name = input('>>>')
         if name in my_pet: 
          print('Your pets is found'+str(name))
         else: 
          print('pet not found:')

# enter your pets name: 
# >>>cow
# Your pets is found cow

#tuple unpacking. this have ability to assign multiple variable within a values 
tree = ['tall','brown','green']
size,color,leaf = tree #assign multiple variable 
print(tree)

# ['tall', 'brown', 'green']


#list item enumeration

# the main deference between range(len(list)) vs enumerate() is 
# range(len(list)) function only return index number of a list, 
#enumerate return index and value itself

for i in enumerate(cricket):
    print('the total nations are' +str(i))


# the total nations are(0, 'eng')
# the total nations are(1, 'aus')
# the total nations are(2, 'ind')
# the total nations are(3, 'ban')
# the total nations are(4, 'nz')
# the total nations are(5, 'sa')
# the total nations are(6, 'sl')
# the total nations are(7, 'pak')

#random selection and ordering
#random have couple of function that take argument in list such as 
# random.choice() function. 
# its randomly select values within a list
# lets try it 

import random
random.choice(cricket)

#ind 

# random.shuffle reorder items in a list
random.shuffle(cricket)
print(cricket)

#['sa', 'nz', 'eng', 'pak', 'aus', 'ban', 'sl', 'ind']

#augmented assignment operator
#+= 
# += this operator can do string and list concatenation


#method: just like function and always expected return values
#index() method always return the potion of a list
# if the value showing off more than one, always return the first position of a duplicate values


#adding values 
#append() and insert()

# the main difference between append() and insert() method is
# append() method always adding values end of the list 

#append()
cricket.append('zim')
print(cricket)

# ['sa', 'nz', 'eng', 'pak', 'aus', 'ban', 'sl', 'ind', 'zim'] zim added to the last

#index()

cricket.index('ireland') 
print(cricket)


# Traceback (most recent call last):
#   File "c:\Users\Fahim\.vscode\extensions\ms-python.python-2026.4.0-win32-x64\python_files\python_server.py", line 139, in exec_user_input
#     retval = callable_(user_input, user_globals)
#   File "<string>", line 1, in <module>
# ValueError: list.index(x): x not in list

#right way to insert() values in the list
# first tell the postion , comma then values 

cricket.insert(1,'ireland')
print(cricket)

# ['sa', 'ireland', 'nz', 'eng', 'pak', 'aus', 'ban', 'sl', 'ind', 'zim']
# append() and insert() are list method, can not use with string and integer

#remove()

cricket.remove('ind')
print(cricket)

#['sa', 'ireland', 'nz', 'eng', 'pak', 'aus', 'ban', 'sl', 'zim']

# with remove() method, the value not in the list to delete then give value error

# Traceback (most recent call last):
#   File "c:\Users\Fahim\.vscode\extensions\ms-python.python-2026.4.0-win32-x64\python_files\python_server.py", line 139, in exec_user_input
#     retval = callable_(user_input, user_globals)
#   File "<string>", line 1, in <module>
# ValueError: list.remove(x): x not in list

# if the value showing up multiple times, remove() methods delete only first position of the values 
# in this case del statement will be useful. it delete all the values on certain list 

#sort()
# can not use sort() when list have value and string

gabba=['brisbane','south australia','iconic ground','bowling pitch', 3,4,198.3,'aus','ashes','eng']
gabba.sort()

# Traceback (most recent call last):
#   File "c:\Users\Fahim\.vscode\extensions\ms-python.python-2026.4.0-win32-x64\python_files\python_server.py", line 139, in exec_user_input
#     retval = callable_(user_input, user_globals)
#   File "<string>", line 1, in <module>
# TypeError: '<' not supported between instances of 'int' and 'str'

#sort alphabetically 
lords = ['england', 'home of cricket', 'the hundred final done', 'won the test this summer', 'YEAH','ENGLAND','NEWZEALAND','ROOT']
lords.sort(key=str.upper)
print(lords)

# ['england', 'ENGLAND', 'home of cricket', 'NEWZEALAND', 'ROOT', 'the hundred final done', 'won the test this summer', 'YEAH']


#reverse()

lords.reverse()
print(lords)

# ['YEAH', 'won the test this summer', 'the hundred final done', 'ROOT', 'NEWZEALAND', 'home of cricket', 'ENGLAND', 'england']

