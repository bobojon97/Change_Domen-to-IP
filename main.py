import socket

target = input('Введите имя сайта и получите ip аддреса: ' '')

print(f"Ip аддрес сайта {target}: {socket.gethostbyname(target)}")
