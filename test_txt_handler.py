from txt_file_handler import TxtFileHandler

handler = TxtFileHandler()

# Тест записи в файл:

text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
"""

handler.write_file("test.txt", text)


