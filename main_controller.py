import socket
import selectors
import logging
from Crypto.Cipher import AES
import binascii


# Адрес и порт второго хоста
gateway_host = 'main_controller'
gateway_port = 30000

# Создание сокета для прослушивания входящих соединений
gateway_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gateway_socket.bind((gateway_host, gateway_port))
gateway_socket.listen()

print(f'Контроллер запущен под адресом: {gateway_host}:{gateway_port}. Ожидание приема сообщений от gateway.',flush=True)

while True:
    # Принятие входящего соединения от первого хоста
    client_socket, address = gateway_socket.accept()
    print(f'Успешное подключение с {address}. Ожидание сообщения...',flush=True)

    # Получение данных от первого хоста
    data = client_socket.recv(1024)
    key = b'ASASASASASASASAS'
    # Расшифровываем текст
    decipher = AES.new(key, AES.MODE_ECB)

    # Дешифрование текста
    decryptedtext = decipher.decrypt(data)

    # Удаление отступа
    padding_length = decryptedtext[-1]
    decryptedtext = decryptedtext[:-padding_length]

    # Вывод дешифрованного текста
    result = decryptedtext.decode('utf-8')

    print(f'Получено от {address}. Дешифрованный текст: {result}',flush=True)

    # Закрытие соединений
    client_socket.close()
    

