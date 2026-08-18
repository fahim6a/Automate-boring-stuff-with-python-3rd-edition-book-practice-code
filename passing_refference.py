def english_cricket(test_summer): # argument
    test_summer.append('s.fleming') # argument pass the reference to the list variable
    test_summer.append('will join in sa tour')

headingley = ['test','pak','england','root','captain','coach'] # list
english_cricket(headingley) 
print(headingley)


# ['test', 'pak', 'england', 'root', 'captain', 'coach', 's.fleming', 'will join in sa tour']

#list vs tuple 
#tuple have used parenthesis bracket and show the tuple must use comma ,
# for example headingley = ['test','pak','england','root','captain','coach'] is a list 
# headingley = ('test','pak','england','root','captain','coach') tuple 

#now subtle change is followed
# if you type only 'list value', it will show string

type('test',)
# <class 'str'>

type(('test'),)
# also show <class 'str'>

#but comma inside parenthesis shows tuple
type(('test',))
#<class 'tuple'>

# list is a mutable, which means we can add, remove, change, modified.
# string is immutable, which can not be changed

# another metaphor is in python variable contain values
# but in python values does not contain in variable, it only reference
# modified string with only slicing and concatenation. 

#copy() and deepcopy() instead of passing argument to variable reference
import copy 
ben = copy.copy(headingley)
print(ben) 

# deepcopy copy the inner list as well
ben = copy.deepcopy(headingley)

