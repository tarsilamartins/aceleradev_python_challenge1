# -*- coding: utf-8 -*-
from datetime import datetime
from math import trunc, floor, ceil

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def taxes(initial, final):

    total_sec = final - initial #Total de segundos da ligação
    total_min = floor(total_sec/60) #Convertendo para minutos
        #print(f'{total_min:.0f}')
    
    #Convertendo para local time
    final = datetime.fromtimestamp(final) 
    initial = datetime.fromtimestamp(initial)
    #print(initial)
        
    if initial.hour > 22 or final.hour < 6:
    #Começar e terminar noturno 
        minute_tax = 0
    
    elif initial.hour >= 6 or initial.hour < 22:
    #Começar e terminar diurno
        minute_tax = 0.09
        
    total = 0.36 + total_min * minute_tax
    #print(f'{total:.2f}')
    return total


def classify_by_phone_number(records):
    results = []

    for record in records:
        i = 0
        price = taxes(record['start'], record['end'])

        for call in results:

            if call['source'] == record['source']:
                i = 1
                call['total'] = (call['total'] + price)
                break

        if i == 0:
            results.append({'source': record['source'], 'total': round(price, 2)})

    final_list = sorted(results, key=lambda i: i['total'], reverse=True)
    return final_list
    
print(classify_by_phone_number(records))