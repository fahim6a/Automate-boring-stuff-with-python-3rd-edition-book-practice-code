# write a program that take user input as string
# store that string in a variable named piklu
# give user also an option to interrupt the program 
# print all name right after the user input end as many time user want 

piklu = []

while True: 
    print('write down your cats name: ' + str(len(piklu)+1) + '(enter nothing to stop.):')
    cats = input('>>>')
    if cats == '':
        break
    piklu = piklu + [cats]

    print('cats names are: ')
    for cats in piklu:
        print(' '+cats)


# write down your cats name: 1(enter nothing to stop.):
# >>>bella
# cats names are: 
#  bella
# write down your cats name: 2(enter nothing to stop.):
# >>>don
# cats names are: 
#  bella
#  don
# write down your cats name: 3(enter nothing to stop.):