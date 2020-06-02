def restarte (reset):
        rest = reset.replace(":", " ").split()
        if len(rest) == 11:
                year = int(rest[10])
                day = int(rest[9])
                month = (rest[8])
                second = int(rest[5])
                minute = int(rest[4])
                hour = int(rest[3])
                restarted = {'restart':{'hour': hour, 'minute': minute, 'seconds': second, 'month': month, 'day': day , 'year' : year}}
                return restarted

