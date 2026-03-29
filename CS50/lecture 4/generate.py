# import random 

#random,choice is used to select a random element from a list, tuple, or string.

# coin = random.choice(["heads", "tails"])
# print(coin)

#random.randint is used to generate a random integer between two specified values (inclusive).

# number = random.randint(1, 10)
# print(number)

#random.shuffle is used to randomly shuffle the elements of a list in place, meaning it modifies the original list.
# cards = ["jack", "queen", "king", "ace"]

# random.shuffle(cards)

# for card in cards:
#     print(card)

#Statistics library is used to perform statistical calculations on data, such as calculating the mean, median, mode, and standard deviation.


import statistics

marks = [100 ,90 , 80 , 70]

print(statistics.mean(marks)) # mean is the average of the numbers in the list


