# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import time
import csv

def get_meigara(code):

  url = 'https://kabutan.jp/stock/?code={}'.format(code)
  q = pq(url)

  if len(q.find('div.company_block')) == 0:
    return None

  try:

    name = q.find('div.company_block > h3').text()
    code_short_name =  q.find('#stockinfo_i1 > div.si_i1_1 > h2').text()
    short_name = code_short_name[code_short_name.find(" ") + 1:]
    market = q.find('span.market').text()
    unit_str = q.find('#kobetsu_left > table:nth-child(4) > tbody > tr:nth-child(6) > td').text()
    unit = int(unit_str.split()[0].replace(',', ''))
    sector = q.find('#stockinfo_i2 > div > a').text()

  except (ValueError, IndexError):
    return None

  return code, name, short_name, market, unit, sector


def meigara_generator(code_range):

  for code in code_range:
    meigara = get_meigara(code)
    if meigara:
      print(meigara)
      yield meigara
    time.sleep(1)

if __name__ == '__main__':

    with open('meigara.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(['code','name','short_name','market','unit','sector'])
        writer.writerow(meigara_generator(range(0000,9999)))
