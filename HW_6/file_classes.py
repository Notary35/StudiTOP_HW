from abc import ABC, abstractmethod
import json
import csv


class AbstractFile(ABC):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @abstractmethod
    def read_file(self):
        # Абстрактный метод для чтения данных из файла.
        pass

    @abstractmethod
    def write_file(self, data):
        # Абстрактный метод для записи данных в файл.
        pass

    @abstractmethod
    def append_file(self, data):
        # Абстрактный метод для дозаписи данных в файл.
        pass


class TxtFile(AbstractFile):

    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def write_file(self, data: str, encoding: str = "utf-8"):
        """
        Метод для записи данных в TXT файл.
        Записывает строку
        """
        try:
            with open(self.file_path, "w", encoding=encoding) as file:
                if not isinstance(data, str):
                    raise TypeError("TXT файл должен содержать строку")
                file.write(data)
        except Exception as e:
            print(f"Произошла ошибка при записи файла: {e}")

    def append_file(self, data: str, encoding: str = "utf-8"):
        """
        Метод для дозаписи данных в TXT файл.
        Дозаписывает строку
        """
        try:
            with open(self.file_path, "a", encoding=encoding) as file:
                if not isinstance(data, str):
                    raise TypeError("TXT файл должен содержать строку")
                file.write(data)
        except Exception as e:
            print(f"Произошла ошибка при записи файла: {e}")

    def read_file(self, encoding="utf-8"):
        """
        Метод для чтения данных из TXT файла.
        """
        try:
            with open(self.file_path, "r", encoding=encoding) as file:
                data = file.read()
            return data
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return ""