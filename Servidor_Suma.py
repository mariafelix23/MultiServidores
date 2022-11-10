import socket
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 9998
ss.bind(("localhost",port))
ss.listen(5)
print("Servidor Suma -> LISTO")
while True:
    cs,addr = ss.accept()
    print("Conexion lista con", str(addr))
    msg = "Conectado c: "+"\r\n"
    n1=cs.recv(1024).decode("ascii")
    n2=cs.recv(1024).decode("ascii")
    num1 = int(n1)
    num2 = int(n2)
    cs.send(str(num1+num2).encode("ascii"))
    cs.close()
ss.close()

    

