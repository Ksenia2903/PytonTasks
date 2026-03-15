class Shape:
    """
    Базовый класс для геометрических фигур.

    Attributes:
        name (str): Название фигуры.
    """

    def __init__(self, name: str) -> None:
        """
        Конструктор класса Shape.

        Args:
            name (str): Название фигуры.
        """
        self.name = name

    def area(self) -> float:
        """
        Метод вычисления площади фигуры.
        """
        pass

    def perimeter(self) -> float:
        """
        Метод вычисления периметра фигуры.
        """
        pass

    def __str__(self) -> str:
        """
        Строковое представление фигуры.
        """
        return f"Shape: {self.name}"

    def __repr__(self) -> str:
        """
        Техническое представление объекта.
        """
        return f"Shape(name='{self.name}')"


class Circle(Shape):
    """
    Класс, описывающий круг.

    Наследуется от класса Shape.
    """

    def __init__(self, radius: float) -> None:
        """
        Конструктор класса Circle.

        Расширяет базовый конструктор добавлением радиуса.

        Args:
            radius (float): Радиус круга.
        """
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        """
        Перегруженный метод вычисления площади.

        Причина перегрузки:
        Формула площади круга отличается от общей формулы,
        поэтому метод необходимо реализовать отдельно.
        """
        pass

    def perimeter(self) -> float:
        """
        Метод вычисления длины окружности.
        """
        pass

    def __str__(self) -> str:
        return f"Circle with radius {self.radius}"

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """
    Класс, описывающий треугольник.

    Наследуется от класса Shape.
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        """
        Конструктор класса Triangle.

        Args:
            a (float): Первая сторона.
            b (float): Вторая сторона.
            c (float): Третья сторона.
        """
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """
        Перегруженный метод вычисления площади.

        Причина перегрузки:
        Для треугольника используется отдельная формула (например, формула Герона),
        поэтому метод отличается от других фигур.
        """
        pass

    def perimeter(self) -> float:
        """
        Метод вычисления периметра треугольника.
        """
        pass

    def __str__(self) -> str:
        return f"Triangle with sides {self.a}, {self.b}, {self.c}"

    def __repr__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"