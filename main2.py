import base64
import binascii
import re

def decode_cms_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        # Удаляем заголовок и окончание
        base64_data = ''.join(lines[1:-1])
        
        # Декодируем base64 данные
        decoded_data = base64.b64decode(base64_data)
        
        # Записываем декодированные данные в файл
        with open(output_filename, 'wb') as file:
            file.write(decoded_data)
        
        print(f"Данные успешно декодированы и сохранены в файл: {output_filename}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
name = 'test.pdf.03'
input_filename = f'{name}.sig'
output_filename = f'{name}.decoded.txt'  # Замените .pdf на соответствующее расширение вашего файла
decode_cms_file(input_filename, output_filename)


def read_sig_file(file_path):
    with open(file_path, 'rb') as f:
        sig_data = f.read()
    return sig_data

def find_strings(sig_data, min_length=4):
    result = []
    current_str = ""
    for byte in sig_data:
        if 32 <= byte < 127:  # ASCII printable characters range
            current_str += chr(byte)
            continue
        if len(current_str) >= min_length:
            result.append(current_str)
        current_str = ""
    if len(current_str) >= min_length:  # append the last found string if any
        result.append(current_str)
    return result

# Пример использования с одним файлом:
file_path = output_filename
sig_data = read_sig_file(file_path)

# Извлечение строк из бинарных данных
strings = find_strings(sig_data)
print(f'strings: {strings}\n')

# Регулярное выражение для email
email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
# Регулярное выражение для дат
date_pattern = re.compile(r'\d{2}\.\d{2}\.\d{4}')

email = None
date1 = None
date2 = None

for s in strings:
    if not email:
        email_match = email_pattern.search(s)
        if email_match:
            email = email_match.group(0)
    
    if not date1:
        date1_match = date_pattern.search(s)
        if date1_match:
            date1 = date1_match.group(0)
    
    elif not date2:
        date2_match = date_pattern.search(s)
        if date2_match:
            date2 = date2_match.group(0)

# Вывод результатов
print("email:", email)
print("date1:", date1)
print("date2:", date2)