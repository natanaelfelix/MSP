def show_version(versio):
    show = versio
    a = show.replace(",", "").split()
    if len(a) == 12:
        minutes = int(a[10])
        hours = int(a[8])
        days = int(a[6])
        weeks = int(a[4])
        years = int(a[2])
        estados = {'uptime': {'years': years, 'weeks' : weeks, 'days': days, 'hours': hours, 'minutes': minutes}}

    elif len(a) == 10:
        minutes = int(a[8])
        hours = int(a[6])
        days = int(a[4])
        weeks = int(a[2])
        estados = {'uptime': { 'weeks' : weeks, 'days': days, 'hours': hours, 'minutes': minutes}}

    elif len(a) == 8:
        minutes = int(a[6])
        hours = int(a[4])
        days = int(a[2])
        estados = {'uptime': {'days': days, 'hours': hours, 'minutes': minutes}}

    elif len(a) == 6:
        minutes = int(a[4])
        hours = int(a[2])
        estados = {'uptime': {'hours': hours, 'minutes': minutes}}
    else:
        minutes = int(a[2])
        estados = {'uptime': {'minutes': minutes}}
    return estados
