from sys import argv
from itertools import count


script_name,start_count = argv
for el in count(int(start_count)):
    if el > 40:
        break
    else:
        print(el)
