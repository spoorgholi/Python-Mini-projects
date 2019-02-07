#importing the libraries
import numpy as np
import random as rnd

#generate a list of numbers between 0 and 100
numbers = list(range(0, 101, 1))
miss = rnd.randint(0, 101)

#remove the miss from the numbers list 
numbers.remove(miss)

#create a duplicate list to check the numbers
initial_list = np.arange(0, 101, 1)

#loop through the list to find the random number 
for i in initial_list:
    if i in numbers:
        pass
    else:
        print('The missing number is \n', i)
    