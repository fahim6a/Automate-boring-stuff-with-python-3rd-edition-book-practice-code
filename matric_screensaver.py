import sys, time, random

#column width will 70
width = 70
# For each column, when the counter is 0, no stream is shown.
# Otherwise, it acts as a counter for how many times a 1 or 0
# should be displayed in that column.


try:
    column = [0] * width
    while True:
        for i in range(width):
            # Restart a stream counter on this column.
            if random.random()< 0.02:
                # The stream length is between 4 and 14 characters long.
                column[i]=random.randint(4,14)
        #print character on this column
            if column[i] == 0:
             print('',end='')
        else:
            print(random.choice([0,1]), end='')
            column[i]-= 1 #decrement the counter for this column
    print()
    time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()


        
                
                