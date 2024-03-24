class Node:
    """
    Узел для красно-черного дерева.

    Attributes:
        key: Ключ узла.
        data: Данные, хранящиеся в узле.
        color: Цвет узла, по умолчанию красный.
        parent: Родительский узел в дереве.
        left: Левый дочерний узел.
        right: Правый дочерний узел.
    """
    def __init__(self, key, data=None, color="RED"):
        self.key = key
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    """
    Класс для представления красно-черного дерева.

    Attributes:
        NIL: Специальный узел NIL, используемый для представления "пустых" листьев.
        root: Корень дерева.
    """
    def __init__(self):
        self.NIL = Node(None)
        self.root = self.NIL

    def insert(self, key, data=None):
        """
        Вставляет узел с ключом key и данными data в красно-черное дерево.

        Args:
            key: Ключ узла для вставки.
            data: Данные узла для вставки.

        Описание метода вставки...
        """
        node = Node(key, data, color="RED")
        node.parent = self.NIL
        node.left = self.NIL
        node.right = self.NIL

        current = self.root
        parent = None

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def _fix_insert(self, node):
        """
        Восстанавливает свойства красно-черного дерева после вставки нового узла.

        Args:
            node: Узел, начиная с которого требуется восстановление свойств.
        """
        while node.parent.color == "RED":
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = "BLACK"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def find_element(self, ptr, key):
        """
         Ищет элемент с ключом key, начиная с узла ptr.

         Args:
             ptr: Узел, с которого начинается поиск.
             key: Ключ искомого элемента.

         Returns:
             Данные найденного элемента или None, если элемент не найден.

         """
        if ptr is not None:
            if key == ptr.key:
                return ptr.data
            elif key < ptr.key:
                return self.find_element(ptr.left, key)
            else:
                return self.find_element(ptr.right, key)
        else:
            print()
            print(f"""Element {key} is {'not found'.upper()} in the tree""")
            return None

    def build_from_list(self, apartment_list):
        """
        Строит красно-черное дерево на основе списка квартир.

        Args:
            apartment_list: Список квартир для добавления в дерево.
        """
        for apartment in apartment_list:
            self.insert(apartment.owner_name, apartment)