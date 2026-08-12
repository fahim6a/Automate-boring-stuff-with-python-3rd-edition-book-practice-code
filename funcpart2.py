# The call stack
# whenever the function call first among many function those
# function return first 
# for this case england() should return first followed by australia(),ind(), nz(), sa()
# lets run it 

#output 
# function a
# function b
# function e
# function c
# function d

def england():
    print('function a')
    australia()
    

def australia():
    print('function b')
    sa()

def ind():
    print('function c')
    nz()

def nz():
    print('function d')
    
    

def sa():
    print('function e')
    ind()
    
england()

