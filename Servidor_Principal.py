import os
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 9999
s.bind(("localhost",port))
s.listen(5)
while True:
    sc,addr = s.accept()
    print("Cliente conectado: %s"%str(addr))
    msg = "Conectado c: "+"\r\n"
    #signo
    signo= sc.recv(1024).decode("ascii")
    n1= sc.recv(1024)
    n2= sc.recv(1024)
    print (signo)
    abrirServicio = ""
    if signo == '+':
     ope = "suma"
     port = 9998
     abrirServicio = "start Servidor_Suma.py"
     print("suma")
    else:
     if signo == '-':
      ope = "resta"
      port = 9997
      print(port)
      abrirServicio = "start Servidor_Resta.py"
     else:
      if signo == '/':
        ope = "div"
        port = 9996
        print(port)
        abrirServicio = "start Servidor_Division.py"
      else:
        if signo == '*':
         ope = "multi"
         port = 9995
         print(port)
         abrirServicio = "start Servidor_Multiplicacion.py"
        else:
         if signo == '%':
          ope = "modulo"
          port = 9994
          print(port)
          abrirServicio = "start Servidor_Modulo.py"
         else:
           ope = "potencia"
           port = 9993
           print(port)
           abrirServicio = "start Servidor_Potencia.py"

    os.system(abrirServicio)
    ss.connect(("localhost",port))
    print("Primer valor enviado..")
    ss.send(n1)
    print("Segundo valor enviado..")
    ss.send(n2)

    msg = ss.recv(1024).decode("ascii")
    sc.send(str(msg).encode("ascii")) 
    ss.close
       
