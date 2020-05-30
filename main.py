import hostname
import qtd_ports
import serial
import show_version
import json
hostes = "BRSA-SWA-3511-01" #Verificar amanha as informações de hostname
por = 'Model number                    : WS-C3560-24PS-E' #sh version | inc Model num
seri = "System serial number            : CAT1037RJF7"
versio = "uptime is 74 years, 40 weeks, 1 day, 19 hours, 59 minutes"
hostnameResult = hostname.host_name(hostes)
portasResult = qtd_ports.qtd_ports(por)
serialResult = serial.serial(seri)
versionResult = show_version.show_version(versio)
up = {}
up.update(hostnameResult)
up.update(portasResult)
up.update(serialResult)
up.update(versionResult)
info = json.dumps(up,ensure_ascii=False)


