from random import sample

numbers = sample(range(1, 69), 5)
powerballNum = sample(range(1, 26), 1)
numbers.sort()

print(', '.join(map(str, numbers)))
print('Powerball Number: ', powerballNum)