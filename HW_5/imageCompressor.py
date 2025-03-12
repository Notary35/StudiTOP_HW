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
        
    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality = self.__quality)
            print(f"Сжато: {input_path} -> {output_path}")
            
    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)
    

    def main(self, input_path: str) -> None:
        """
        Основная функция программы. Обрабатывает входной путь и запускает сжатие изображений.
        """
        register_heif_opener()
        input_path = input_path.strip('"')
        
        if os.path.exists(input_path):
            if os.path.isfile(input_path):
                print(f"Обрабатываем файл: {input_path}")
                output_path = os.path.splitext(input_path)[0] + '.heic'
                self.compress_image(input_path, output_path)
            elif os.path.isdir(input_path):
                print(f"Обрабатываем директорию: {input_path}")
                self.process_directory(input_path)