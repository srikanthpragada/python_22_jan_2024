sales = {2019: 100, 2020: 40, 2021: 120, 2022: 200}

for k in sales.keys():
    print(f"{k} - {sales[k]}")

for k, v in sales.items():
    print(k, v)
