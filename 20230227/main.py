# import numpy as np

# print(np.sqrt(9))

# import pandas as pd

# print(pd.Series([1, 2, 3, 4, 5, 6]))


# from random_word import RandomWords
# r = RandomWords()

# for range in range(5):
#     words = r.get_random_word().upper()


#     print(words)

import random_word
#import string

# Create a random_word instance
rw = random_word.RandomWords()

# Generate 5 random words
words = []
for i in range(5):
    word = rw.get_random_word().upper()
    words.append(word)

# Sort the words
words.sort()

# Print the words
for word in words:
    print(word)







