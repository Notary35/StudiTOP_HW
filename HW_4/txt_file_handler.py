class TxtFileHandler:
    def write_file(self, file_path: str, data: str):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

    def append_file(self, file_path: str, data: str):
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(data)

    def read_file(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data