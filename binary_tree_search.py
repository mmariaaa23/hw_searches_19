class BinaryTreeNode:
    """
    Узел для бинарного поискового дерева.

    Attributes:
        apartment (Apartment): Объект квартиры, хранящийся в узле.
        left (BinaryTreeNode): Ссылка на левого потомка узла.
        right (BinaryTreeNode): Ссылка на правого потомка узла.
    """
    def __init__(self, apartment):
        self.apartment = apartment
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, apartment):
        """
        Вставка новой квартиры в бинарное поисковое дерево.

        Args:
            apartment (Apartment): Объект квартиры для вставки.
        """
        if self.root is None:
            self.root = BinaryTreeNode(apartment)
        else:
            self._insert(self.root, apartment)

    def _insert(self, node, apartment):
        """
        Рекурсивный помощник для вставки новой квартиры в дерево.

        Args:
            node (BinaryTreeNode): Узел, с которого начинается поиск места для вставки.
            apartment (Apartment): Объект квартиры для вставки.
        """
        if apartment.owner_name < node.apartment.owner_name:
            if node.left is None:
                node.left = BinaryTreeNode(apartment)
            else:
                self._insert(node.left, apartment)
        elif apartment.owner_name > node.apartment.owner_name:
            if node.right is None:
                node.right = BinaryTreeNode(apartment)
            else:
                self._insert(node.right, apartment)

    def search(self, key):
        """
        Поиск квартиры по имени владельца.

        Args:
            key (str): Имя владельца квартиры для поиска.

        Returns:
            Apartment: Найденная квартира или None, если квартира не найдена.
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        """
        Рекурсивный помощник для поиска квартиры в дереве.

        Args:
            node (BinaryTreeNode): Узел, с которого начинается поиск.
            key (str): Имя владельца квартиры для поиска.

        Returns:
            Apartment: Найденная квартира или None, если квартира не найдена.
        """
        if node is None or key == node.apartment.owner_name:
            return node.apartment
        elif key < node.apartment.owner_name:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
