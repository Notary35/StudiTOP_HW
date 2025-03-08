class TxtFileHandler:
    def write_file(self, file_path: str, data: str):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)