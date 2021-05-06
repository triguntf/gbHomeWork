russian_dict = {1: "Один",
                2: "Два",
                3: "Три",
                4: "Четыре"
                }


def make_translate():
    for data in get_data():
        if int(data.split()[2]) in russian_dict.keys():
            data_list = data.split()
            data_list[0] = russian_dict.get(int(data_list[2]))
            with open("dz5_4_result.txt", "a") as result:
                result.write(f"{data_list[0]} {data_list[1]} {data_list[2]}\n")


def get_data():
    try:
        with open("dz5_4.txt") as user_data:
            yield from (line.strip() for line in user_data.readlines())
    except FileNotFoundError:
        print("Файл 'dz5_4.txt' не найден")
        return
    finally:
        user_data.close()


make_translate()