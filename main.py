import binascii
import re

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
file_path = 'report_8b2b5d47_3613_4247_b12c_8ba8159716d8_Other_2021_09_01_752526.sig'
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