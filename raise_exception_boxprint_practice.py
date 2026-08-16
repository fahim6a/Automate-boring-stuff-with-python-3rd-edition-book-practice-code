# logic: if symbol !=1, then print 'symbol must be single character string'
# if width <= 2, then print width must be greater than two 
# if height <= 2, then print height must be greater than two 
# during printing any massage, use raise exception 

def boxprint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception ('symbol must be a single character')
    if width <=2:
        raise Exception ('width must be greater than 2')
    if height <=2:
        raise Exception ('height must be greater than 2')
    
    print(symbol*width) 
    for i in range(height-2): # because we already have 2 times height that way we minus 2 row from original height
        print(symbol + (' '* (width-2))+ symbol) # same as height logic, already have 2 width
    print (symbol * width) 
try:
    boxprint('*',4,4) # star print, 4 time in a row and 4 times in total height
    boxprint('0',20,5)
    boxprint('x',1,3) # run the error here, because width is 1
    boxprint('zz',20,10) # double character so that show error

except Exception as err:
    print('An exception happened' + str(err))
try:
    boxprint('zz',20,10)
except Exception as err:
    print('An exception happened' + str(err)) # convert typeerror or any error to string and put it together



# #output
# ****
# *  *
# *  *
# ****
# 00000000000000000000
# 0                  0
# 0                  0
# 0                  0
# 00000000000000000000
# An exception happenedwidth must be greater than 2
# An exception happenedsymbol must be a single character

