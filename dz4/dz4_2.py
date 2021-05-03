first_list=[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [first_list[el+1] for el in range(len(first_list)-1) if first_list[el+1]> first_list[el]]

print(new_list)