"""
pip install pillow pillow-heif
"""
import os
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    """
    Класс для сжатия изображений.
    """
    supported_formats = ('.jpg', '.jpeg', '.png')  # Атрибут класса

    def __init__(self, quality: int) -> None:
        """
        Инициализация класса ImageCompressor.
        Args:
            quality (int): значение качества сжатия изображения от 1 до 100, где 1 - максимальное сжатие, 100 - максимальное качество
        Ничего не возвращает
        """
        self.__quality = quality
