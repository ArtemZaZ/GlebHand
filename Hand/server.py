import subprocess
from xmlrpc.server import SimpleXMLRPCServer
from Hand.config import *

cmd = 'hostname -I | cut -d\' \' -f1'
selfIP = subprocess.check_output(cmd, shell=True)     # получаем IP
selfIP.rstrip().decode("utf-8")     # удаляем \n, переводим в текст

server = SimpleXMLRPCServer((selfIP, PORT), logRequests=False)

server.register_function(bendFinger)

server.serve_forever()

