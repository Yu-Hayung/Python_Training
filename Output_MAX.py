a = [7, 2, 1, 8, 9, 10]
print(max(a))


maxValue = a[0]
for i in range(1, len(a)):
    if maxValue < a[i]:
        maxValue = a[i]
print(maxValue)


a = [34, 62, 79, 12, 0]
largest = a[0]
for i in a:
    if i > largest:
        largest = i

print(largest)

print('############################################')

import random

random.seed(123)
A = [(random.randint(100, 999), random.randint(100, 999)) for _ in range(80)]

max_num0 = max(t[0] for t in A)
print(max_num0)

max_num1 = max(t[1] for t in A)
print(max_num1)

