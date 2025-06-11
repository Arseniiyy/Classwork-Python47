
# FILENAME = "forest.png"
# NEWFILENAME = "forest_new.png"

# image_data = []

# with open(FILENAME,"rb") as file:
#     image_data = file.read()

# with open(NEWFILENAME,"wb") as file:
#     file.write(image_data)
#     print(f"Файл {FILENAME} скопирован в {NEWFILENAME}")

# import pickle

# FILENAME = "user.dat"

# name = "Ilya"
# age = 620

# with open(FILENAME,"wb")as file:
#     pickle.dump(name,file)
#     pickle.dump(age,file)

# with open(FILENAME,"rb")as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
# print("name","age")



# import shelve

# d = shelve.open("python471")
# d.close()


class FileHandler:
    def __init__(self, tekst):
        self.tekst = tekst

    def read(self):
        with open(self.tekst, "r", encoding="utf-8") as file:
            return file.readlines()

    def write(self, text):
        with open(self.tekst, "w", encoding="utf-8") as file:
            file.write(text)

    def edit_line(self, num, new_tekst):
        line = self.read()
        line[num - 1] = new_tekst 
        self.write("".join(line))

    def search(self, word):
        return [line.strip() for line in self.read() if word in line]

        

    

file = FileHandler("test.txt")
file.write("Arsenii\penkoi\n76\n")
print(file.read())
file.edit_line(2, "Yanchik\n")
print(file.read())
print(file.search("8"))           
   

import secrets
import string
 
characters = string.ascii_letters + string.digits
password = "".join(secrets.choice(characters) for i in range(6))

print(password)


