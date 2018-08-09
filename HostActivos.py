#-*- coding:utf-8 -*-
#******************************************************************************************
#*(  \/  )  /__\  (  _ \(_  _)(  _  )  / __)  /__\  ( \( )(  _ \ (  _  )( \/ )  /__\  (  )  
#* )    (  /(__)\  )   / _)(_  )(_)(   \__ \ /(__)\  )  (  )(_) ) )(_)(  \  /  /(__)\  )(__ 
#*(_/\/\_)(__)(__)(_)\_)(____)(_____)  (___/(__)(__)(_)\_)(____/ (_____)  \/  (__)(__)(____)
#*                                    *
#* Web: http://mariosandovalp3.com.ve *
#* Contacto: mariosandovalp3@gmail.com*
#******************************************************************************************
import os
import sys
import platform
import socket

ip = raw_input("Ingresa la IP de la red: ")
iplist = ip.split('.')

try:
    red = iplist[0]+'.'+iplist[1]+'.'+iplist[2]+'.'
    inicio = int(input("Inicio de la subred: "))
    fin = int(input("Fin de la subred para el barrido: "))
except:
    print("[!] Error")
    sys.exit(1)
 
if (platform.system()=="Windows"):
    ping = "ping -n 1"
else :
    ping = "ping -c 1"

print "\n"
print "******************** ESCANEO ********************"
print "[*] Escaneando desde la IP ",red+str(inicio),"hasta",red+str(fin)

for subred in range(inicio, fin+1):
    direccion = red+str(subred)
    response = os.popen(ping+" "+direccion)
    cont = 0
    for line in response.readlines():
        if ("ttl" in line.lower()):
            hostname = socket.gethostbyaddr(direccion)
            cont = cont + 1
            print "\n"
            print "******************** ACTIVO ********************"
            print "IP: ",direccion
            print "NOMBRE DEL HOST: ",hostname[0]
            print "\n"
            break
          
print("[*] Total de host activos %s"%cont)