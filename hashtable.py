# для поиска хэш-таблицей
import matplotlib.pyplot as plt
import numpy as np

from apartment_class import Apartment
class HashTable:
    """
    Класс HashTable для реализации хеш-таблицы с линейным опробованием.

    Attributes:
        size (int): Размер хеш-таблицы.
        table (list): Список для хранения данных квартир.
        collisions (int): Количество коллизий при вставке.
    """
    def __init__(self, size=100):
        """
        Конструктор для HashTable.

        Args:
            size (int): Размер хеш-таблицы.
        """
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def hash_function(self, key):
        """
        Хеш-функция для преобразования ключа в индекс таблицы.

        Args:
            key (str): Ключ для генерации индекса.

        Returns:
            int: Индекс в хеш-таблице.
        """
        total = 0
        prime = 8709771  # Простое число для улучшения хеш-функции
        for char in key:
            total = (total * prime) + ord(char)
        return total % self.size

    def linear_probing(self, index):
        """
        Метод линейного опробования для решения коллизий в хеш-таблице.

        Args:
            index (int): Текущий индекс в таблице.

        Returns:
            int: Следующий индекс в таблице после решения коллизии.
        """
        return (index + 1) % self.size

    def insert(self, apartment):
        """
        Вставляет объект квартиры в хеш-таблицу.

        Args:
            apartment (Apartment): Объект квартиры для вставки.
        """
        key = apartment.owner_name
        index = self.hash_function(key)

        while self.table[index] is not None:
            self.collisions += 1
            index = self.linear_probing(index)

        self.table[index] = apartment

    def search(self, key):
        """
        Поиск квартиры по имени владельца.

        Args:
            key (str): Имя владельца квартиры.

        Returns:
            Apartment: Найденная квартира или None, если квартира не найдена.
        """
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index].owner_name == key:
                return self.table[index]
            index = self.linear_probing(index)

        return None
# Функция для тестирования
def test_hash_table(size):
    """
    Тестирует хеш-таблицу, вставляя квартиры и возвращая число коллизий.

    Args:
        size (int): Размер хеш-таблицы.

    Returns:
        int: Количество коллизий при вставке.
    """
    hash_table = HashTable(size)
    for i in range(size):
        apartment = Apartment(total_area=i, house_number=i, apartment_number=i,
                              owner_name=f"Owner{i}", residents_number=i)
        hash_table.insert(apartment)

    return hash_table.collisions

# Построение графика зависимости числа коллизий от размера массива
sizes = list(range(200, 1001, 200))
collisions = [test_hash_table(size) for size in sizes]

plt.plot(sizes, collisions, marker='o')
plt.title('Collisions vs. Array Size')
plt.xlabel('Array Size')
plt.ylabel('Number of Collisions')
plt.show()


