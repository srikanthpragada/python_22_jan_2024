data = ['ab123', 'xy456', 'pq2', 'de98']

for n in sorted(data, key=lambda v: v[2:]):
    print(n)
