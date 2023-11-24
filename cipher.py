from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

#Генерация случайной соли
salt = get_random_bytes(16)

# Пароль для шифрования
password = "MYSECRETPHRASE"

# Генерация ключа из пароля с использованием PBKDF2
key = PBKDF2(password, salt, dkLen=32)

# Инициализация объекта AES с режимом шифрования CBC
cipher = AES.new(key, AES.MODE_CBC)

# Текст для шифрования
plaintext = "Hello, World!"

# Добавление отступа для дополнения до размера блока
padding_length = 16 - (len(plaintext) % 16)
plaintext += chr(padding_length) * padding_length

# Шифрование текста
ciphertext = cipher.encrypt(plaintext)

# Получение вектора инициализации
iv = b64encode(cipher.iv).decode('utf-8')

# Получение зашифрованного текста в формате base64
ciphertext = b64encode(ciphertext).decode('utf-8')

# Дешифрование текста
cipher = AES.new(key, AES.MODE_CBC, b64decode(iv))
decryptedtext = cipher.decrypt(b64decode(ciphertext))

# Удаление отступа
padding_length = ord(decryptedtext[-1])
decryptedtext = decryptedtext[:-padding_length]

# Вывод результатов
print("Зашифрованный текст:", ciphertext)
print("Дешифрованный текст:", decryptedtext.decode('utf-8'))
