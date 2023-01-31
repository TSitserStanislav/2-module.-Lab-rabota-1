class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook (Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.name = name
        self.author = author
        if isinstance (pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError (f'Укажине корекктный номер страницы')
        else:
            raise AttributeError(f'Укажине корекктный номер страницы')


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author} Страниц: {self.pages}"


class AudioBook (Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0.0:
                self.duration = duration
            else:
                raise AttributeError (f'Укажите корректнкую продолжительность')
        else:
            raise AttributeError(f'Укажите корректнкую продолжительность')
        self.name = name
        self.author = author


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

BookTest = Book ("Путь на Амальтею", "Братья Стругацкие")
print(BookTest)
Test1 = PaperBook("Путь на Амальтею", "Братья Стругацкие", 63)
print(Test1)
Test2 = AudioBook ("Путь на Амальтею", "Братья Стругацкие", 152.5)
print(Test2)