import random
import time
import logging
import sys
import socket
# Настройка логирования
#logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
time.sleep(40)
while True:
   water: int = random.randint(10, 100)
   message = f'Уровень влажности: {water}%'
#    time.sleep(40)

   with socket.socket() as s:
       s.connect(('gateway', 22000))
       s.sendall(bytes(message, 'UTF-8'))

   time.sleep(40)
   
