# 19) 19, б, в, е - вариант
# сортировки: пузырьком, вставкой, быстрая
# Массив данных квартир жилого комплекса: номер дома,  номер квартиры, количество комнат, общая площадь, ФИО  владельца, число проживающих
# правила сравнения: сравнение по полям – общая площадь (убыванию), номер дома, номер  квартиры, ФИО владельца


import pandas as pd
# from faker import Faker
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import random


from apartment_class import Apartment
from hashtable import HashTable
from binary_tree_search import BinarySearchTree
from red_black_tree import RedBlackTree

# fake = Faker("ru_RU")  Single Faker instance with locale

df = pd.read_csv("/Users/avvemassha/PycharmProjects/pythonProject2/train_extended.csv")

# names_list = [fake.name() for _ in range(10000)]
# df["owner_name"] = names_list
# df = df.drop(["Id", "LifeSquare", "KitchenSquare", "HouseYear", "Ecology_1", "Ecology_2", "Ecology_3", "Social_1", "HouseFloor", "Social_2", "Social_3", "Healthcare_1", "Helthcare_2", "Shops_2", "Price"], axis=1)
# df = df.rename(columns={'DistrictId': 'apartment_number', 'Square': 'total_area', 'Floor': 'house_number', 'Shops_1': 'residents_number'})
# df.to_csv("train.csv")


"""создание датасетов"""
df_1 = df[:500]  # 500
df_1 = df_1.drop(["Rooms"], axis=1)
df_1.to_csv("data_1.csv")

df_2 = df[:5000]  # 600
df_2 = df_2.drop(["Rooms"], axis=1)
df_2.to_csv("data_2.csv")

df_3 = df[:10000]  # 700
df_3 = df_3.drop(["Rooms"], axis=1)
df_3.to_csv("data_3.csv")

df_4 = df[:20000]  # 800
df_4 = df_4.drop(["Rooms"], axis=1)
df_4.to_csv("data_4.csv")

df_5 = df[:40000]  # 900
df_5 = df_5.drop(["Rooms"], axis=1)
df_5.to_csv("data_5.csv")

df_6 = df[:80000]  # 1000
df_6 = df_6.drop(["Rooms"], axis=1)
df_6.to_csv("data_6.csv")

df_7 = df[:100000]  # 1100
df_7 = df_7.drop(["Rooms"], axis=1)
df_7.to_csv("data_7.csv")



"""
функции сортировок написаны для массивов, => формирую из датасетов правильный формат
"""
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

# Размеры массивов для тестирования
array_sizes = [len(mas_1), len(mas_2), len(mas_3), len(mas_4), len(mas_5), len(mas_6), len(mas_7)]

num_repeats = 10
search_times = {'Binary Search': [], 'Hash Table Search': [], 'Multimap Search': [], 'RBS':[]}

for size in array_sizes:
    print(f"Testing for size: {size}")

    test_array = mas_1[:size]  # Просто берем первый массив в mass

    # 1. Бинарное дерево поиска
    bst = BinarySearchTree()
    for apartment in test_array:
        bst.insert(apartment)


    start_time = time.time()
    for _ in range(num_repeats):
        key = test_array[0].owner_name  # Просто берем первый элемент
        result = bst.search(key)
    search_time = (time.time() - start_time) / num_repeats
    search_times['Binary Search'].append(search_time)

    # 2. Хэш-таблица
    hash_table = HashTable(size)
    for apartment in test_array:
        hash_table.insert(apartment)

    start_time = time.time()
    for _ in range(num_repeats):
        key = test_array[0].owner_name  # Просто берем первый элемент
        result = hash_table.search(key)
    search_time = (time.time() - start_time) / num_repeats
    search_times['Hash Table Search'].append(search_time)

    # 3. Multimap
    multimap = defaultdict(list)
    for apartment in test_array:
        multimap[apartment.owner_name].append(apartment)

    start_time = time.time()
    for _ in range(num_repeats):
        key = test_array[0].owner_name  # Просто берем первый элемент
        result = multimap[key]
    search_time = (time.time() - start_time) / num_repeats
    search_times['Multimap Search'].append(search_time)

    # 4. Red-Black Tree Search
    red_black = RedBlackTree()
    red_black.build_from_list(test_array)
    start_time = time.time()

    for _ in range(num_repeats):
        key_1 = random.choice(test_array)
        key = key_1.owner_name
        result = red_black.find_element(red_black.root, key)
    end_time = time.time()

    search_time = (end_time - start_time) / num_repeats
    search_times['RBS'].append(search_time)

for method, times in search_times.items():
    plt.plot(array_sizes, times, label=method)


plt.title('Search Time vs. Array Size')
plt.xlabel('Array Size')
plt.ylabel('Search Time')
plt.yscale('log')
plt.legend()
plt.show()

#  сортировка пузырьком
# bubble_times = []
# for i, mas in enumerate(mass):
#     tmp = mas[:]
#     start = time.time()
#     bubbleSort(tmp)
#     bubble_times.append(time.time() - start)
#     with open(f"bubble_{i + 1}.txt", "w") as f:
#         for elem in tmp:
#             f.write(
#                 f"{elem.total_area} {elem.house_number} {elem.apartment_number} {elem.owner_name} {elem.residents_number}\n"
#             )
# print(bubble_times)
# plt.plot(x, bubble_times)
#
# # сортировка вставкой
# insertion_times = []
# for i, mas in enumerate(mass):
#     tmp = mas[:]
#     start = time.time()
#     insertionSort(tmp)
#     insertion_times.append(time.time() - start)
#     with open(f"insertion_{i+1}.txt", "w") as f:
#         for elem in tmp:
#             f.write(
#                 f"{elem.total_area} {elem.house_number} {elem.apartment_number} {elem.owner_name} {elem.residents_number}\n"
#             )
# print(insertion_times)
# plt.plot(x, insertion_times)
#
#  быстрая сортировка
# quick_times = []
# for i, mas in enumerate(mass):
#     tmp = mas[:]
#     start = time.time()
#     tmp = quickSort(tmp)
#     quick_times.append(time.time() - start)
#     with open(f"quick_{i+1}.txt", "w") as f:
#         for elem in tmp:
#             f.write(
#                 f"{elem.total_area} {elem.house_number} {elem.apartment_number} {elem.owner_name} {elem.residents_number}\n"
#             )
# print(quick_times)
# plt.plot(x, quick_times)
#
#
#  отрисовка графиков
# plt.legend(("bubble", "insertion", "quick"))
# plt.show()
