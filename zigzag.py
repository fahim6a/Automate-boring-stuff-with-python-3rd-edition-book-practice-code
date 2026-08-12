# *********** print this star 
# there is no space (indent)
# space increase or not 

import sys, time
indent = 0
indentIncreasing = True
try:
    while True:
     print(' ', indent, end='')
     print('********')
     time.sleep(0.1) 

     if indentIncreasing:
        indent = indent + 1
     elif indent == 20:
        indentIncreasing = False
    else:
     indent = input - 1
     if indent == 0:
        indentIncreasing = True
except KeyboardInterrupt:
   sys.exit()
   


