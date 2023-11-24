import random
import time
import logging
import sys
import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# Настройка логирования
#logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
time.sleep(40)
while True:
   water: int = random.randint(0, 10)
   message = f'Уровень воды в цветочнои горшке: {water}'
#    time.sleep(40)
   # Генерация случайного ключа
   key = b'ASASASASASASASAS'

   # Текст для шифрования
   plaintext = message.encode()

   # Добавление отступа для дополнения до размера блока
   padding_length = 16 - (len(plaintext) % 16)
   plaintext += bytes([padding_length]) * padding_length

   # Инициализация объекта AES с режимом шифрования ECB
   cipher = AES.new(key, AES.MODE_ECB)

   # Шифрование текста
   ciphertext = cipher.encrypt(plaintext)
   with socket.socket() as s:
       s.connect(('gateway', 22000))
       s.sendall(ciphertext)

   #logging.info(message) 
   time.sleep(20)