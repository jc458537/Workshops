__author__ = 'jc458537'
from random import randint
num_of_picks = int(input('how many quick picks'))
pick_of_6_num=[]
num = 0
for i in range(0, num_of_picks):
    num = randint(1, 45)
    for j in range(0,6):
        while num is pick_of_6_num:
            num = randint(1, 45)
        pick_of_6_num.append(num)

    print(sorted(pick_of_6_num))
    pick_of_6_num =[]
