from datetime import *

with open("players.txt", "rt") as f:
    players = {}
    for line in f.readlines():
        if ',' not in line:
            continue  # ignore the line

        name, dobstr = line.strip().split(',')

        try:
            # convert string to datetime
            dob = datetime.strptime(dobstr, '%d-%m-%Y')
            # get timedelta between sysdate and dob
            period = datetime.today() - dob
            years = period.days // 365
            players[name] = years
        except:
            pass

for name, years in sorted(players.items(), key=lambda t: t[1]):
    print(f"{name:20}  {years:2}")
