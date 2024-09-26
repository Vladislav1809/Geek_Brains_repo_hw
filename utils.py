import requests
from decimal import *
from datetime import datetime

getcontext().prec = 4


def currency_rates(curr):
    curr = curr.upper()
    reply = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if curr not in reply:
        return None

    ruble = reply[(reply.find('<Value>', reply.find(curr)) + len('<Value>')):reply.find('</Value>', reply.find(curr))]
    upd_time = reply[reply.find('Date="') + len('Data="'):reply.find('"', reply.find('Date="') + len('Data="'))].split('.')
    day, month, year = map(int, upd_time)
    return f'{Decimal(ruble.replace(",","."))}, {datetime(day=day, month=month, year=year)}'


# print(currency_rates('RUB'))
# print(currency_rates('USD'))
