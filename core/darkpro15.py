
import matplotlib.pyplot as plt
%matplotlib inline
# import matplotlib.pylab as plt
# import numpy as np
import random
random.seed()
people = []
for i in range(0, 50):
    people.append(100)

for beshkan in range(0, 1000):
    for person1 in range(0, 50):
        person2 = random.randrange(0, 50)
        people[person1] = people[person1] - 1
        people[person2] = people[person2]+1

plt.bar(range(0, 50), people)

