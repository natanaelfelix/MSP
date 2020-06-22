def serial(seri):
    serial = seri
    s = serial.replace(":", " ").split()
    seri = s[-1]
    serie = {'Sys_Serial_number': seri}
    return serie
