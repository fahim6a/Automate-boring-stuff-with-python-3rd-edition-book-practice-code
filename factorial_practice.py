# calculate the factorials of n 
# 1 factorials is 1*1 = 1
# 2 factorials is 2*1*2 = 4
# the purpose of choosing logging instead of print
# with logging, easily can filter out or silence the massage severity
# logging have few level such as INFO, CRITICAL, ERROR, WARNING
# we do not need write 50 times print or remove when needed 
# specify with level keywords 
# call method is logging.debug(level:which level we want)
# formatting placeholder such as %()s that sign is print style string formattig 


import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start the program')

def factorials(n):
     logging.debug('start the factorials(' + str(n) + ')')
     total = 1
     for i in range(1,n+1): # to reach right number it +1 is used with n, python data sequence 0,1,2...
      total *= i    #(multiply and assign value to total) #otherwise shows 1 factorials lower value than actual number input 
      logging.debug('i is ' + str(i)+ 'total is ' + str(total))
     logging.debug('end of factorials('  + str(n) + ')')
     return total
print(factorials(5))
logging.debug('end of the program')

# output if we use 0 as real value instead of 1. like factorials(n+1)
# 2026-08-16 15:21:11,294 - DEBUG - i is 0total is 0
# 2026-08-16 15:21:11,294 - DEBUG - i is 1total is 0
# 2026-08-16 15:21:11,294 - DEBUG - i is 2total is 0
# 2026-08-16 15:21:11,294 - DEBUG - i is 3total is 0
# 2026-08-16 15:21:11,294 - DEBUG - i is 4total is 0
# 2026-08-16 15:21:11,294 - DEBUG - i is 5total is 0
# 2026-08-16 15:21:11,294 - DEBUG - end of factorials(5)
# 0
# 2026-08-16 15:21:11,294 - DEBUG - end of the program

#output, make sure the number start with 1 and end with + 1 with given number
# such as factorials(1, n+1)

# 2026-08-16 15:22:45,957 - DEBUG - start the factorials(5)
# 2026-08-16 15:22:45,957 - DEBUG - i is 1total is 1
# 2026-08-16 15:22:45,957 - DEBUG - i is 2total is 2
# 2026-08-16 15:22:45,957 - DEBUG - i is 3total is 6
# 2026-08-16 15:22:45,957 - DEBUG - i is 4total is 24
# 2026-08-16 15:22:45,957 - DEBUG - i is 5total is 120
# 2026-08-16 15:22:45,957 - DEBUG - end of factorials(5)
# 120
# 2026-08-16 15:22:45,957 - DEBUG - end of the program