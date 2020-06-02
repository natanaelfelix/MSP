def host_name(hostes):
    hostname = hostes
    h = hostname.replace("-", " ").split()
    if len(h) == 4:
        pais = str(h[0][0] + h[0][1])
        estado = str(h[0][2] + h[0][3])
        tipo = str(h[1])
        predio = int(h[2][1] + h[2][2])
        rack = int(h[2][2] + h[2][3])
        posicao = int(h[3][0] + h[3][1])
        sw = {'Switch': {'name': hostname, 'location':{'Country': pais, 'State': estado}}}
        return sw
