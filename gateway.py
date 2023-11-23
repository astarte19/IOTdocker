import socket
import selectors
import logging


# Адрес и порт, на котором шлюз будет принимать сообщения
gateway_host = 'gateway'  # Прослушивание на всех доступных интерфейсах
gateway_port = 22000

# Адрес и порт второго хоста
destination_host = 'main_controller'
destination_port = 30000

# Создание сокета для прослушивания входящих соединений
gateway_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gateway_socket.bind((gateway_host, gateway_port))
gateway_socket.listen()

print(f'Шлюз запущен на {gateway_host}:{gateway_port}. Ожидание подключения...',flush=True)


while True:
    # Принятие входящего соединения от первого хоста
    client_socket, address = gateway_socket.accept()
    print(f'Успешное подключение от {address}. Ожидание сообщения...',flush=True)

    # Получение данных от первого хоста
    data = client_socket.recv(1024)
    print(f'Получено от {address}: {data.decode()}')

    #Создание сокета для подключения ко второму хосту
    destination_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Подключение к второму хосту
    destination_socket.connect((destination_host, destination_port))
    # Отправка данных второму хосту
    destination_socket.sendall(data)

    # Получение данных от второго хоста
    # response = destination_socket.recv(1024)
    # print(f'Получено от {destination_host}:{destination_port}: {response.decode()}')
    # Закрытие соединений
    client_socket.close()
    destination_socket.close()

