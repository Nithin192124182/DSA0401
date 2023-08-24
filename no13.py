from collections import Counter
import numpy as np


words_list = []
with open("C:\Users\KANTA\OneDrive\Documents\OneDrive\Screenshots\Documents\FODS\studentlist.txt", "r") as f:
    read = f.read()
    words_list = read.split()
    words_list = np.array(words_list)

counts = Counter(words_list)

print(counts)
