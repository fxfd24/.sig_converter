# .sig_converter
 Скрипт для декодирования и парсинга данных на python.

Используются библиотеки binascii и re.

Для запуска необходимо клонировать репозиторий, установить необходимые библиотеки и запустить файл main.py.

Он использует тестовый .sig файл для демонстрации работоспособности скрипта. Чтобы использовать алгоритм на других файлах, поменяйте путь к файлу в переменной file_path.

# 17.07.2024
 Обновление в коде: 

Добавил файл main2.py, в котором реализована логика для .sig файлов, типа test.pdf.03.sig

Логикак такая, что мы сначала читаем sig, декодируем его при помощи base64.b64decode, затем применяем алгоритм по парсингу данных, как в файле main.py

В ходе работы main2.py создает txt файл с base64 данными, которые потом используются в main.py
