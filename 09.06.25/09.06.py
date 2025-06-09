
# try:
#     myfile = open("helloworld.txt","w")
#     try:
#         print("Работает с файлом")
#     finally:
#         myfile.close()
# except Exception as ex:
#     print(ex)

# with open('python471', "w") as abc:
#     print("Работает с файлом pifon47")

# list = ["Ilya\n","Regina\n","Artem\n"]
# with open("python471") as file:
#     file.writelines(list)

# with open("python47","r") as file:
#     for line in file:
#         print(line)

# with open("python47","r") as file:
#     line = file.read()
#     print(line)

# with open("python471", "w", encoding="utf8") as file:
#     file.write("Русский язык читается")


def main():
    filename = "myfile.txt"
    while True:
        print("\nВыберите действие:")
        print("1. Записать в файл (заменить содержимое)")
        print("2. Дозаписать в файл")
        print("3. Прочитать файл")
        print("4. Вывести весь содержимое файла")
        print("5. Выйти")
        choice = input("Выбор действия: ")
        if choice == '1':
            text = input("Введите текст: ")
            with open(filename, 'w', encoding='utf8') as file:
                file.write(text)
            print("Данные введены")
        elif choice == '2':
            text = input("Введите текст для изменения: ")
            with open(filename, 'a', encoding='utf8') as file:
                file.write(text + '\n')
            print("Данные изменены.")

        elif choice == '3':
            try:
                with open(filename, 'r', encoding='utf8') as file:
                    content = file.read()
                print("\nСодержимое файла:\n")
                print(content)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == '4':
            try:
                with open(filename, 'r', encoding='utf8') as file:
                    for line in file:
                        print(line, end='')
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == '5':
            print("Выход из программы")
            break
if __name__ == "__main__":
    main()












        