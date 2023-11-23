import random
import time
import logging
import sys
import socket
# Настройка логирования
#logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
time.sleep(40)
while True:
   temp: int = random.randint(22, 35)
   message = f'Температура в спальне: {temp} цельсий'
   # time.sleep(40)

   with socket.socket() as s:
       s.connect(('gateway', 22000))
       s.sendall(bytes(message, 'UTF-8'))

   #logging.info(message) 
   time.sleep(20)






