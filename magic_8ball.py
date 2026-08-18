import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print('Ask a yes or no question:')
input('>')
print(messages[random.randint(0, len(messages) - 1)]) # total massage of the length is 9
# but python index start with 0, so total 9 massage 0-8, but len function return 9.
# which is out of index. thats why we -1 for this to stay in 0-8. 
#this is called zero-based indexing
