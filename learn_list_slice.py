england = ['root','buttler','stokes','bethel','duckett','j smith']

#now call the show the index of stokes REPL
england[2]

# what is slice: index contain only one integer values
#but slice have multiple integer values
# we can specify the starting and ending point also
#[starting: ending]

# now show values in the list from bethel to rest of the list 

england[2:]

#['bethel', 'duckett', 'j smith']

# now show index 0 to 4 
england[0:4]
# ['root', 'buttler', 'stokes', 'bethel']

# there is no way we can skip certain part of list values 
# it shows continues values within range 
# what if we need to show two values only on different indexes 

print(england[0], england[4])

#root duckett

# now we can update our values 
# you may know ben stokes retired from test cricket this summer 2026
# now update this position with j.cox

england[2]='j. cox'
print(england)

# ['root', 'buttler', 'j. cox', 'bethel', 'duckett', 'j smith']

# also you can show negative number also 
# if you write -2 index , what happen? 

england[-2]

#duckett 


#concatenation and replication

# you can add two list with + operator and
# multiplication with * operators
# now create two new list called australia and bangladesh

Australia=['head','smith', 'starc','cummins','hazlewood','d.warner']


Bangladesh=['Tanzid','Shadman','Mominul','Mosfique','Das','Hasan','Taskin']

#Now we can concatenation with + operators

Australia [0:] + Bangladesh[0:]

#['head', 'smith', 'starc', 'cummins', 'hazlewood', 'd.warner', 'Tanzid', 'Shadman', 'Mominul', 'Mosfique', 'Das', 'Hasan', 'Taskin']

# you can multiply with certain number of integer as well 
Bangladesh[2:3]* 3
# ['Mominul', 'Mominul', 'Mominul']

# del statement deleted list values and all the values moved up the number of values deleted from the list 

del Bangladesh[2]
print(Bangladesh)

#['Tanzid', 'Shadman', 'Mosfique', 'Das', 'Hasan', 'Taskin']



