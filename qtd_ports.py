def qtd_ports(por):
    model = por
    portas = []
    for port in model:
        if port.isdigit():
            portas.append(port)
    qtd = int(portas[-2] + portas[-1])
    po = {'Ports': qtd}
    return po
