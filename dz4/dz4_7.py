from itertools import count

n = int(input("Факториал до какого числа вычислить?: "))
index = 1


def fact(value):
    yield 1
    if value > 1:
        # Рекурсия через субгенератор
        yield from (el1 * el2 for el1, el2 in zip(fact(value - 1), count(2)))


for el in fact(n):
    print(f"{index}! = {el}")
    index += 1