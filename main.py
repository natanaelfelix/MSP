import hostname
import qtd_ports
import serial
import show_version
import restart
import model
import json
dados = open("Dados.txt", 'w')
hostes = "BRSA-SWA-3511-01"
por = 'Model number                    : WS-C3560-24PS-E' #sh version | inc Model num
seri = "System serial number            : CAT1037RJF7"
versio = "uptime is 74 years, 40 weeks, 1 day, 19 hours, 59 minutes"
reset = "System restarted at 04:16:12 gmt Sat Feb 29 2020"
hostnameResult = hostname.host_name(hostes)
resetResult = restart.restarte(reset)
portasResult = qtd_ports.qtd_ports(por)
serialResult = serial.serial(seri)
versionResult = show_version.show_version(versio)
modelResult = model.mod(por)
up = {}
up.update(hostnameResult)
up.update(versionResult)
up.update(resetResult)
up.update(serialResult)
up.update(portasResult)
info = json.dumps(up, ensure_ascii=False) #indent=4
dados.write(info)
dados.close()
print(info)
