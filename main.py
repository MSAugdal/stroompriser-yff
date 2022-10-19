from time import sleep  # modul for å sette på vent
import pandas as pd  # modul for å importere og eksportere data
from termcolor import colored  # modul for å fargelegge tekst i terminalen
from rich.table import Table  # modul for å lage tabeller
from rich.console import Console  # modul for å printe tabeller til terminalen

file = pd.read_excel('recalculated-nordic-system-price.xlsx')  # leser inn excel-fil

dates = file.get('Date')  # henter ut datoer fra excel filen
dates = [str(i) for i in dates]  # henter dato og konverteret til string
# linjen over henter dato fra excel filen, men datoen kommer ut som "2021-11-27 00:00:00"
dates = [str(i[0:10]) for i in dates]  # her fjerner jeg "00:00:00" fra datoen

hours = [i for i in range(0, 24)]  # lager en liste over timer i en dag

prices = file.get('System Price(Eur/MWh)')  # henter ut prisene fra excel filen
prices = [float(i) for i in prices]  # konverterer prisene til desimaltall

priceInfo = {}  # lager en tom dictionary som vil bli fylt med dato, tidspunkt og pris.
# dette er en model for hvordan dataen skal se ut i denne dictionaryen
# priceInfo = {
#     '2021-11-10': {
#         '0': 12.78,
#         '1': 14.54,
#         '2': 13.60,
#     }
# }
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

keys = priceInfo.keys()  # lagrer alle keys i en variabel
console = Console()
while True:
    print("\n")
    print(colored("Dates:", "green"))
    for key in keys:
        print(key)
    print("\n")
    date = input(colored('Enter the date you want to see the price for (YYYY-MM-DD): ', "green"))  # spør bruker om hvilken dato de vil se pris for
    if date in keys:  # hvis datoen er i dictionary
        print(colored("\nPrice per hour:", "green"))  # print ut en overskrift
        table = Table(box=None)  # lager en tabell for billetter og priser
        table.add_column()  # legger til en kolonne for *
        table.add_column()  # legger til en kolonne for time
        table.add_column()  # legger til en kolonne for pris
        table.add_column()  # legger til en kolonne for øre
        for hour in priceInfo[date]:  # looper gjennom timene og legger til i tabellen
            table.add_row(colored("*", "yellow"), f"{hour}:00", colored(f"{round(priceInfo[date][hour] / 100 ,2)}", "green"), colored("Kr", "green"))
        console.print(table)  # printer tabellen til terminalen
        print("\n")
        exit()  # avslutt programmet
    else:
        print('The date you entered is not in the file')  # hvis datoen ikke er i dictionary
