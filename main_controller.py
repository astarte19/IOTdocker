import socket
import selectors
import logging


# Адрес и порт второго хоста
gateway_host = 'main_controller'
gateway_port = 30000

# Создание сокета для прослушивания входящих соединений
gateway_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gateway_socket.bind((gateway_host, gateway_port))
gateway_socket.listen()

print(f'Контроллер запущен на {gateway_host}:{gateway_port}. Ожидание подключения...',flush=True)

while True:
    # Принятие входящего соединения от первого хоста
    client_socket, address = gateway_socket.accept()
    print(f'Успешное подключение от {address}. Ожидание сообщения...',flush=True)

    # Получение данных от первого хоста
    data = client_socket.recv(1024)
    print(f'Получено от {address}: {data.decode()}',flush=True)

    # Закрытие соединений
    client_socket.close()
    

