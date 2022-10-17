import pandas as pd

file = pd.read_excel('recalculated-nordic-system-price.xlsx')

dates = file.get('Date')
dates = [str(i) for i in dates]
dates = [str(i[0:10]) for i in dates]

# hours = file.get('Hours')
# hours = [str(i) for i in hours]
# hours = [int(i[0:3]) for i in hours]
hours = [i for i in range(0, 24)]

prices = file.get('System Price(Eur/MWh)')
prices = [int(i) for i in prices]

priceInfo = {}
for date in dates:
    if date not in priceInfo:
        priceInfo[date] = {}

    for hour in range(0, len(hours)):
        priceInfo[date][hours[hour]] = hours[hour]


for key, value in priceInfo.items():
    print(key, value)

dictionary = {
    '2021-11-10': {
        '0': prices[0],
        '1': prices[1],
        '2': prices[2],
    }
}
