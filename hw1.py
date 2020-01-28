data = {
    'IR': [1775, 2736, 2824],
    'US': [2445, 5301, 6899],
    'AR': [1311, 3797, 4367],
}
years = [1870, 1913, 1929]
for c in data.keys():
    data[c] = { years[i]: value for i, value in enumerate(data[c]) }

def percent_diff(c1, c2, year):
    answer = data[c1][year] / data[c2][year]
    print(f'{answer:.3f}; {(answer - 1) * 100:.1f}%')
    return answer

percent_diff('IR', 'US', 1870)
percent_diff('IR', 'AR', 1870)

def avg_growth(c, year1, year2):
    return (data[c][year2] / data[c][year1]) ** (1 / (year2 - year1))

def forecast(c, y1, y2, y3):
    return data[c][y3] * avg_growth(c, y1, y2) ** (y3 - y2)

def pv(c, y1, y2):
    r = 0.03
    gn = avg_growth(c, y1, y2) - 1
    output = 0
    for t in range(0, y2 - y1 + 1):
        output += data[c][y1] * (((1 + gn) / (1 + r)) ** t)
    return output

for key in data:
    # print(f'{key}: {(avg_growth(key, 1870, 1913) - 1) * 100:.2f}%')
    # print(f'{key}: {(forecast(key, 1870, 1913, 1929)):.0f}')
    print(f'{key}: {(pv(key, 1870, 1913)):,.0f}')


