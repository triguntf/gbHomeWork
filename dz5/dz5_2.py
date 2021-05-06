def get_txt_info():
    try:
        with open("dz5_1.txt") as data_file:
            lines_count = sum(line.count("\n") for line in data_file.read())
            print(f"Количество строк в тексте: {lines_count}")
            data_file.seek(0)
            for index, line in enumerate(data_file.readlines(), start=1):
                words_per_line_count = (index, len(line.split()))
                print(f"В строке {words_per_line_count[0]} количество слов: {words_per_line_count[1]}")
    except FileNotFoundError:
        print("Запустите первое домашнее задание, для создания файла.")


get_txt_info()