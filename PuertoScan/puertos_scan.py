#!/usr/bin/env python
#-*- coding:utf-8 -*-
#******************************************************************************************
#*(  \/  )  /__\  (  _ \(_  _)(  _  )  / __)  /__\  ( \( )(  _ \ (  _  )( \/ )  /__\  (  )  
#* )    (  /(__)\  )   / _)(_  )(_)(   \__ \ /(__)\  )  (  )(_) ) )(_)(  \  /  /(__)\  )(__ 
#*(_/\/\_)(__)(__)(_)\_)(____)(_____)  (___/(__)(__)(_)\_)(____/ (_____)  \/  (__)(__)(____)
#*                                    *
#* Web: http://mariosandovalp3.com.ve *
#* Contacto: mariosandovalp3@gmail.com*
#******************************************************************************************
import socket
import subprocess
import sys
import platform
import csv


puertos = open("puertos.csv","r")
puertos_csv = csv.reader(puertos)

if (platform.system()=="Windows"):
	subprocess.call('cls',shell=True)
else:
	subprocess.call('clear',shell=True)

print '-' * 60

ip = raw_input('Ingrese Host/IP en especifico: ')
host_name = socket.gethostbyaddr(ip)

try:
    inicio = int(input("Ingrese el puerto de inicio: "))
    fin = int(input("Ingrese el puerto final: "))
except:
    print("[!] Error")
    sys.exit(1)


print '-' * 60
print 'Pro favor espere, escaneando host remoto', ip
print "Escaneando desde el puerto %s al %s" %(inicio,fin)
print '-' * 60
print "***************** "+host_name[0]+" *****************"
print "\n"
try:
	for port in range(inicio,fin+1):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((ip,port))		
		if result == 0:
			for puerto,vendor in puertos_csv:
				if int(puerto)==port:
					v = vendor					
					print "*** [+]: {}".format(port)+" "+" Abierto",vendor
					break
		else:
			print "*** [X]: {}".format(port)+" Cerrado"
			
		sock.close
except KeyboardInterrupt:
	print 'Presione Ctrl+C para interrunpir el escaneo'
	sys.exit()
except socket.gaierror:
	print 'IP no pudo ser resuelto. Saliendo'
	sys.exit()
print "\n"
print 'Escaneo completo'