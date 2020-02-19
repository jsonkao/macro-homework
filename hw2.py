alpha = 0.3

yt_all = { 'US': 46405.25, 'CH': 3862.92 }

def find_a(country):
    yt = yt_all[country]
    kt = 2.5 * yt
    return yt / (kt ** alpha)

A = find_a('US')
print(f'A = {A}')

def find_kt(country):
    yt = yt_all[country]
    return (yt / A) ** (1 / alpha)

for c in yt_all.keys():
    print(f'kt^{c} = {find_kt(c):.02f}')


