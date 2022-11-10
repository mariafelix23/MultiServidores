import os
import socket
import time
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 9999
print("Opción a ejecutar")
print("[+] Suma")
print("[-] Resta")
print("[*] Multiplicación")
print("[/] División")
print("[%] Módulo")
print("[^] Potencia")
ss.connect(("localhost",port))
signo=input("Operación: ")
ss.send(signo.encode("ascii"))
n1=input("Primer valor: ")
ss.send(n1.encode("ascii"))
n2=input("Segundo valor: ")
ss.send(n2.encode("ascii"))

msg = ss.recv(1024).decode("ascii")
ss.close()

print("Resultado {} {} {} = {} ".format(n1,signo,n2,msg))
input("Enter para terminar...")
ss.close()
