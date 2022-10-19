import pandas as pd

file = pd.read_excel('recalculated-nordic-system-price.xlsx')  # leser inn excel-fil

dates = file.get('Date')  # henter ut datoer fra excel filen
dates = [str(i) for i in dates]  # henter dato og konverteret til string
# linjen over henter dato fra excel filen, men datoen kommer ut som "2021-11-27 00:00:00"
dates = [str(i[0:10]) for i in dates]  # her fjerner jeg "00:00:00" fra datoen

hours = [i for i in range(0, 24)]  # lager en liste over timer i en dag

prices = file.get('System Price(Eur/MWh)')  # henter ut prisene fra excel filen
prices = [float(i) for i in prices]  # konverterer prisene til desimaltall

# priceAndDate = {}  # lager en tom dicitonary for å lagre pris til dato

# for date in dates:
#     if dates.index(date) != 0:  # finner startposisjonen til prisen så lenge det ikke er første datoen
#         endPos = dates.index(date) * 24  # sjekker hvilken posisjon i listen som datoen er på
#         starPos = endPos - dates.index(date) * 24
#     else:  # setter startPos til 0 og endPos til 24 om det er første dato
#         endPos = 24
#         starPos = 0

#     for hour in hours:  # looper for hver time i en dag og bruker starPos, endPos for å legge pris til time
#         priceAndDate[date][hour] = prices[starPos:endPos]

priceInfo = {}  # lager en tom dictionary som vil bli fylt med dato, tidspunkt og pris.
for date in dates:  # looper for hver dato i listen
    if date not in priceInfo:  # sjekker om datoen ikke er i dicitonary så det ikke blir duplikater
        priceInfo[date] = {}  # legger dato til i dictionary om den ikke allerede er der

    if dates.index(date) != 0:  # finner startposisjonen til prisen så lenge det ikke er første datoen
        endPos = dates.index(date) * 24  # sjekker hvilken posisjon i listen som datoen er på
        starPos = endPos - dates.index(date) * 24
    else:  # setter startPos til 0 og endPos til 24 om det er første dato
        endPos = 24
        starPos = 0
    hourPrices = prices[starPos:endPos]  # lager en liste over timesprisene for datoen
    for hour in hours:  # looper for hver time i en dag
        priceInfo[date][hour] = hourPrices[hour]  # legger time til dato, og pris til time i dictionary

# denne er kun for å sjekke at output av koden er rett
for key, value in priceInfo.items():  # looper for hver "key" og "value" i dictionary
    print(key, value)  # printer key og value

# dette er en model for hvordan dataen skal se ut i dictionary
priceInfo = {
    '2021-11-10': {
        '0': 12.78,
        '1': 14.54,
        '2': 13.60,
    }
}
