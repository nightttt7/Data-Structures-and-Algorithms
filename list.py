# %%
# name the slice
items = list(range(1, 41))

a = slice(5, 10)

items[a]

# %%
# find the most common items
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
Counter(words).most_common(3)

# %%
