from functools import reduce

numbers = [el for el in range(99,1001) if el%2==0]

def custom(first, second):
    return first * second

result = reduce(custom, numbers)
print(result)