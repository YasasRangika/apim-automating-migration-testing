import socket
from time import sleep


def wait():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('127.0.0.1', 9443))
    while result != 0:
        result = s.connect_ex(('127.0.0.1', 9443))
    sleep(5)
