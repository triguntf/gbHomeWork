from itertools import cycle
from sys import argv


script_name,cirle_count,cirle_name = argv
c=0
for el in cycle(cirle_name):
    if c > int(cirle_count):
        break
    print(el)
    c += 1