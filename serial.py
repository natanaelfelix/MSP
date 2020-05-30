def serial(seri):
    serial = seri
    s = serial.replace(":", " ").split()
    seri = s[-1]
    serie = {'Numero de série:': seri}
    return serie
