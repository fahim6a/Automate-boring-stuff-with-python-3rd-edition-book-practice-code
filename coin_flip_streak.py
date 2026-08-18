# Write a program to find out how often a streak of six heads or a streak 
# of six tails comes up in a randomly generated list of 100 heads and tails. 
# Your program should break up the experiment into two parts: the first part 
# generates a list of 100 randomly selected 'H' and 'T' values, and the sec
# ond part checks if there is a streak in it. Put all of this code in a loop that 
# repeats the experiment 10,000 times so that you can find out what percent
# age of the coin flips contains a streak of six heads or six tails in a row. As a 
# hint, the function call random.randint(0, 1) will return a 0 value 50 percent 
# of the time and a 1 value the other 50 percent of the time


import random

def coin_flip():
    number = random.randint(0, 1)
    if number == 0:
        return 'H'
    else:
        return 'T'

def generate_flips():
    flip = []
    for i in range(100):
        flip.append(coin_flip())
    return flip

def has_streak(flip):
    current_streak = 1
    for i in range(1, len(flip)):
        if flip[i] == flip[i - 1]:
            current_streak += 1
        else:
            current_streak = 1
        if current_streak >= 6:
            return True
    return False

streak_count = 0
for experiment in range(10000):
    flips = generate_flips()
    if has_streak(flips):
        streak_count += 1

percentage = (streak_count / 10000) * 100
print('Streak found in', streak_count, 'out of 10000 experiments')
print('Percentage:', percentage, '%')

# Streak found in 8028 out of 10000 experiments
# Percentage: 80.28 %


# flip = ['H','H','T','T','T']
# #        0   1   2   3   4

# At i = 2, flip[i] is flip[2] = 'T' — the current letter you're looking at.
# flip[i - 1] is flip[1] = 'H' — the letter directly before it.
