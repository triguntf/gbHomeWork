import re


def make_dict():
    data_dict = {}
    with open("dz5_6.txt") as data_file:
        for data in data_file:
            key = re.match(r'\w*', data)
            val = re.findall(r'\d+', data)
            data_dict.setdefault(key.group(0))
            val_dict = sum([int(el) for el in val])
            data_dict[key.group(0)] = val_dict
    print(data_dict)


make_dict()