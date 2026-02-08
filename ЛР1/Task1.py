# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

# 1. Университет

class University:
    def __init__(self, name: str, students_count: int, is_public: bool):
        """
        Создание и подготовка к работе объекта "Университет".

        :param name: Название университета
        :param students_count: Количество студентов
        :param is_public: Государственный ли университет

        Примеры:
        >>> uni = University("MIT", 11000, True)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not name:
            raise ValueError("Название не может быть пустым")
        self.name = name

        if not isinstance(students_count, int):
            raise TypeError("Количество студентов должно быть int")
        if students_count < 0:
            raise ValueError("Количество студентов не может быть отрицательным")
        self.students_count = students_count

        if not isinstance(is_public, bool):
            raise TypeError("Флаг должен быть bool")
        self.is_public = is_public

    def enroll_student(self, student_name: str) -> int:
        """
        Зачисление студента.

        :param student_name: Имя студента
        :return: Новое количество студентов

        Примеры:
        >>> uni = University("MIT", 11000, True)
        >>> uni.enroll_student("Alex")
        """
        if not isinstance(student_name, str):
            raise TypeError("Имя должно быть строкой")
        if not student_name:
            raise ValueError("Имя не может быть пустым")
        ...

    def expel_student(self, student_name: str) -> int:
        """
        Отчисление студента.

        :param student_name: Имя студента
        :return: Новое количество студентов

        Примеры:
        >>> uni = University("MIT", 11000, True)
        >>> uni.expel_student("Alex")
        """
        if not isinstance(student_name, str):
            raise TypeError("Имя должно быть строкой")
        if not student_name:
            raise ValueError("Имя не может быть пустым")
        ...

    def open_faculty(self, faculty_name: str) -> None:
        """
        Открытие факультета.

        :param faculty_name: Название факультета
        :return: None

        Примеры:
        >>> uni = University("MIT", 11000, True)
        >>> uni.open_faculty("Computer Science")
        """
        if not isinstance(faculty_name, str):
            raise TypeError("Название факультета должно быть строкой")
        if not faculty_name:
            raise ValueError("Название факультета не может быть пустым")
        ...


# 2. Компьютерная игра

class ComputerGame:
    def __init__(self, title: str, genre: str, players_online: int):
        """
        Создание и подготовка к работе объекта "Компьютерная игра".

        :param title: Название игры
        :param genre: Жанр
        :param players_online: Игроков онлайн

        Примеры:
        >>> game = ComputerGame("WarZone", "Shooter", 5000)
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not title:
            raise ValueError("Название не может быть пустым")
        self.title = title

        if not isinstance(genre, str):
            raise TypeError("Жанр должен быть строкой")
        if not genre:
            raise ValueError("Жанр не может быть пустым")
        self.genre = genre

        if not isinstance(players_online, int):
            raise TypeError("Игроки онлайн должны быть int")
        if players_online < 0:
            raise ValueError("Игроки онлайн не могут быть отрицательными")
        self.players_online = players_online

    def start_match(self, players: int) -> bool:
        """
        Начать матч.

        :param players: Количество игроков
        :return: Успешность запуска

        Примеры:
        >>> game = ComputerGame("WarZone", "Shooter", 5000)
        >>> game.start_match(10)
        """
        if not isinstance(players, int):
            raise TypeError("Количество игроков должно быть int")
        if players <= 0:
            raise ValueError("Количество игроков должно быть положительным")
        ...

    def end_match(self) -> None:
        """
        Завершить матч.

        :return: None

        Примеры:
        >>> game = ComputerGame("WarZone", "Shooter", 5000)
        >>> game.end_match()
        """
        ...

    def add_player(self, nickname: str) -> int:
        """
        Добавить игрока онлайн.

        :param nickname: Ник игрока
        :return: Новое количество игроков онлайн

        Примеры:
        >>> game = ComputerGame("WarZone", "Shooter", 5000)
        >>> game.add_player("Player1")
        """
        if not isinstance(nickname, str):
            raise TypeError("Ник должен быть строкой")
        if not nickname:
            raise ValueError("Ник не может быть пустым")
        ...


# 3. Метеостанция

class WeatherStation:
    def __init__(self, location: str, temperature: float, humidity: float):
        """
        Создание и подготовка к работе объекта "Метеостанция".

        :param location: Локация
        :param temperature: Температура (°C)
        :param humidity: Влажность (%)

        Примеры:
        >>> ws = WeatherStation("Berlin", 20.5, 60)
        """
        if not isinstance(location, str):
            raise TypeError("Локация должна быть строкой")
        if not location:
            raise ValueError("Локация не может быть пустой")
        self.location = location

        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть int или float")
        self.temperature = float(temperature)

        if not isinstance(humidity, (int, float)):
            raise TypeError("Влажность должна быть int или float")
        if not 0 <= humidity <= 100:
            raise ValueError("Влажность должна быть 0–100%")
        self.humidity = float(humidity)

    def measure_temperature(self) -> float:
        """
        Измерить температуру.

        :return: Температура

        Примеры:
        >>> ws = WeatherStation("Berlin", 20.5, 60)
        >>> ws.measure_temperature()
        """
        ...

    def measure_humidity(self) -> float:
        """
        Измерить влажность.

        :return: Влажность

        Примеры:
        >>> ws = WeatherStation("Berlin", 20.5, 60)
        >>> ws.measure_humidity()
        """
        ...

    def update_data(self, temperature: float, humidity: float) -> None:
        """
        Обновить погодные данные.

        :param temperature: Новая температура
        :param humidity: Новая влажность
        :return: None

        Примеры:
        >>> ws = WeatherStation("Berlin", 20.5, 60)
        >>> ws.update_data(18.0, 70)
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть int или float")

        if not isinstance(humidity, (int, float)):
            raise TypeError("Влажность должна быть int или float")
        if not 0 <= humidity <= 100:
            raise ValueError("Влажность должна быть 0–100%")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
