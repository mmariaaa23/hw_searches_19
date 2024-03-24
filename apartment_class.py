"""
   Класс Apartment представляет собой модель квартиры.

   Attributes:
       total_area (float): Общая площадь квартиры.
       house_number (int): Номер дома.
       apartment_number (int): Номер квартиры.
       owner_name (str): Имя владельца.
       residents_number (int): Количество жителей.
   """
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
        return self.owner_name > other.owner_name

    def __ge__(self, other):  # >=
        return self.owner_name >= other.owner_name

    def __lt__(self, other):  # <
        return self.owner_name < other.owner_name

    def __le__(self, other):  # <=
        return self.owner_name <= (other.owner_name)

