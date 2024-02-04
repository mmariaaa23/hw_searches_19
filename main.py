# 19) 19, б, в, е - вариант
# сортировки: пузырьком, вставкой, быстрая
# Массив данных квартир жилого комплекса: номер дома,  номер квартиры, количество комнат, общая площадь, ФИО  владельца, число проживающих
# правила сравнения: сравнение по полям – общая площадь (убыванию), номер дома, номер  квартиры, ФИО владельца


import pandas as pd
from faker import Faker
import time
import matplotlib.pyplot as plt

from bubbleSort import bubbleSort
from insertionSort import insertionSort
from quickSort import quickSort

fake = Faker("ru_RU")  # Single Faker instance with locale

df = pd.read_csv("/Users/avvemassha/PycharmProjects/pythonProject2/train.csv")

# names_list = [fake.name() for _ in range(10000)]
# df["owner_name"] = names_list
# df = df.drop(["Id", "LifeSquare", "KitchenSquare", "HouseYear", "Ecology_1", "Ecology_2", "Ecology_3", "Social_1", "HouseFloor", "Social_2", "Social_3", "Healthcare_1", "Helthcare_2", "Shops_2", "Price"], axis=1)
# df = df.rename(columns={'DistrictId': 'apartment_number', 'Square': 'total_area', 'Floor': 'house_number', 'Shops_1': 'residents_number'})
# df.to_csv("train.csv")


# @brief разделяю датасет на наборы для сортировки

df_1 = df[:500]  # 500
df_1 = df_1.drop(["Rooms"], axis=1)
df_1.to_csv("data_1.csv")

df_2 = df[500:1100]  # 600
df_2 = df_2.drop(["Rooms"], axis=1)
df_2.to_csv("data_2.csv")

df_3 = df[1100:1700]  # 700
df_3 = df_3.drop(["Rooms"], axis=1)
df_3.to_csv("data_3.csv")

df_4 = df[1700:2500]  # 800
df_4 = df_4.drop(["Rooms"], axis=1)
df_4.to_csv("data_4.csv")

df_5 = df[2500:3400]  # 900
df_5 = df_5.drop(["Rooms"], axis=1)
df_5.to_csv("data_5.csv")

df_6 = df[3400:4400]  # 1000
df_6 = df_6.drop(["Rooms"], axis=1)
df_6.to_csv("data_6.csv")

df_7 = df[4400:5500]  # 1100
df_7 = df_7.drop(["Rooms"], axis=1)
df_7.to_csv("data_7.csv")

# df_8 = df[4000:4500]
# df_8 = df_8.drop(["Rooms"], axis=1)
# df_8.to_csv("data_8.csv")


# @brief для перегрузки операторов сначала создаю класс объекта из датасета
class Apartment:
    def __init__(
        self,
        total_area: float,
        house_number: int,
        apartment_number: int,
        owner_name: str,
        residents_number: int,
    ):
        self.total_area = total_area
        self.house_number = house_number
        self.apartment_number = apartment_number
        self.owner_name = owner_name
        self.residents_number = residents_number

    def __gt__(self, other):  # >
        if self.total_area > other.total_area:
            return True
        elif self.total_area < other.total_area:
            return False
        else:
            if self.house_number > other.house_number:
                return True
            elif self.house_number < other.house_number:
                return False
            else:
                if self.apartment_number > other.apartment_number:
                    return True
                elif self.apartment_number < other.apartment_number:
                    return False
                else:
                    if self.owner_name > other.owner_name:
                        return True
                    else:
                        return False

    def __ge__(self, other):  # >=
        if self.total_area >= other.total_area:
            return True
        elif self.total_area < other.total_area:
            return False
        else:
            if self.house_number >= other.house_number:
                return True
            elif self.house_number < other.house_number:
                return False
            else:
                if self.apartment_number >= other.apartment_number:
                    return True
                elif self.apartment_number < other.apartment_number:
                    return False
                else:
                    if self.owner_name >= other.owner_name:
                        return True
                    else:
                        return False

    def __lt__(self, other):  # <
        if self.total_area < other.total_area:
            return True
        elif self.total_area > other.total_area:
            return False
        else:
            if self.house_number < other.house_number:
                return True
            elif self.house_number > other.house_number:
                return False
            else:
                if self.apartment_number < other.apartment_number:
                    return True
                elif self.apartment_number > other.apartment_number:
                    return False
                else:
                    if self.owner_name < other.owner_name:
                        return True
                    else:
                        return False

    def __le__(self, other):  # <
        if self.total_area <= other.total_area:
            return True
        elif self.total_area > other.total_area:
            return False
        else:
            if self.house_number <= other.house_number:
                return True
            elif self.house_number > other.house_number:
                return False
            else:
                if self.apartment_number <= other.apartment_number:
                    return True
                elif self.apartment_number > other.apartment_number:
                    return False
                else:
                    if self.owner_name <= other.owner_name:
                        return True
                    else:
                        return False


# apartment1 = Apartment(100, 10, 1, "Иванов", 2)
# apartment2 = Apartment(80, 12, 2, "Петров", 3)
# print(apartment1 > apartment2)
# print(apartment1 < apartment2)
# print(apartment1 >= apartment2)
# print(apartment1 <= apartment2)


# @brief функции сортировок написаны для массивов, => формирую из датасетов правильный формат
df_1 = pd.read_csv("data_1.csv")
mas_1 = []
for i in range(len(df_1)):
    mas_1.append(
        Apartment(
            df_1["total_area"][i],
            df_1["house_number"][i],
            df_1["apartment_number"][i],
            df_1["owner_name"][i],
            df_1["residents_number"][i],
        )
    )
# print(mas_1[1])

df_2 = pd.read_csv("data_2.csv")
mas_2 = []
for i in range(len(df_2)):
    mas_2.append(
        Apartment(
            df_2["total_area"][i],
            df_2["house_number"][i],
            df_2["apartment_number"][i],
            df_2["owner_name"][i],
            df_2["residents_number"][i],
        )
    )

df_3 = pd.read_csv("data_3.csv")
mas_3 = []
for i in range(len(df_3)):
    mas_3.append(
        Apartment(
            df_3["total_area"][i],
            df_3["house_number"][i],
            df_3["apartment_number"][i],
            df_3["owner_name"][i],
            df_3["residents_number"][i],
        )
    )

df_4 = pd.read_csv("data_4.csv")
mas_4 = []
for i in range(len(df_4)):
    mas_4.append(
        Apartment(
            df_4["total_area"][i],
            df_4["house_number"][i],
            df_4["apartment_number"][i],
            df_4["owner_name"][i],
            df_4["residents_number"][i],
        )
    )
# print(mas_1[1])

df_5 = pd.read_csv("data_5.csv")
mas_5 = []
for i in range(len(df_5)):
    mas_5.append(
        Apartment(
            df_5["total_area"][i],
            df_5["house_number"][i],
            df_5["apartment_number"][i],
            df_5["owner_name"][i],
            df_5["residents_number"][i],
        )
    )

df_6 = pd.read_csv("data_6.csv")
mas_6 = []
for i in range(len(df_6)):
    mas_6.append(
        Apartment(
            df_6["total_area"][i],
            df_6["house_number"][i],
            df_6["apartment_number"][i],
            df_6["owner_name"][i],
            df_6["residents_number"][i],
        )
    )

df_7 = pd.read_csv("data_7.csv")
mas_7 = []
for i in range(len(df_7)):
    mas_7.append(
        Apartment(
            df_7["total_area"][i],
            df_7["house_number"][i],
            df_7["apartment_number"][i],
            df_7["owner_name"][i],
            df_7["residents_number"][i],
        )
    )

mass = [mas_1, mas_2, mas_3, mas_4, mas_5, mas_6, mas_7]

x = []
for i in mass:
    x.append(len(i))
print(x)

# @brief сортировка пузырьком
bubble_times = []
for i, mas in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    bubbleSort(tmp)
    bubble_times.append(time.time() - start)
    with open(f"bubble_{i + 1}.txt", "w") as f:
        for elem in tmp:
            f.write(
                f"{elem.total_area} {elem.house_number} {elem.apartment_number} {elem.owner_name} {elem.residents_number}\n"
            )
print(bubble_times)
plt.plot(x, bubble_times)

# сортировка вставкой
insertion_times = []
for i, mas in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    insertionSort(tmp)
    insertion_times.append(time.time() - start)
    with open(f"insertion_{i+1}.txt", "w") as f:
        for elem in tmp:
            f.write(
                f"{elem.total_area} {elem.house_number} {elem.apartment_number} {elem.owner_name} {elem.residents_number}\n"
            )
print(insertion_times)
plt.plot(x, insertion_times)

# @brief быстрая сортировка
quick_times = []
for i, mas in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    tmp = quickSort(tmp)
    quick_times.append(time.time() - start)
    with open(f"quick_{i+1}.txt", "w") as f:
        for elem in tmp:
            f.write(
                f"{elem.total_area} {elem.house_number} {elem.apartment_number} {elem.owner_name} {elem.residents_number}\n"
            )
print(quick_times)
plt.plot(x, quick_times)


# @brief отрисовка графиков
plt.legend(("bubble", "insertion", "quick"))
plt.show()
