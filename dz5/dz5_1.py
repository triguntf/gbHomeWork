def get_data():
    data_list = []
    while True:
        data = input("Введите данные: ")
        if not data:
            break
        else:
            data_list.append(data)
    return data_list


def make_txt():
    with open("dz5_1.txt", 'a') as text_file:
        for line in get_data():
            text_file.write(line +"\n")


make_txt()