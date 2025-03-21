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


