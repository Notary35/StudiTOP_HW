class TxtFileHandler:
    def write_file(self, file_path: str, data: str):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                if not isinstance(data, str):
                    raise TypeError("TXT файл должен содержать строку")
                file.write(data)
        except Exception as e:
            print(f"Произошла ошибка при записи файла: {e}")

    def append_file(self, file_path: str, data: str):
        try:
            with open(file_path, "a", encoding="utf-8") as file:
                if not isinstance(data, str):
                    raise TypeError("TXT файл должен содержать строку")
                file.write(data)
        except Exception as e:
            print(f"Произошла ошибка при дозаписи файла: {e}")

    def read_file(self, file_path: str) -> str:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()
            return data
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return ""
