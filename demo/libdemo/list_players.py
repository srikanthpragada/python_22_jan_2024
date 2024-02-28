from datetime import *

with open("players.txt", "rt") as f:
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
            print(f"{name:20}  {years:2}")
        except:
            pass
