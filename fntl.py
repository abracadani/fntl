class Portfolio():
  def __init__(self, stocks=[]):
    self.stocks = stocks

  def Profit(start, end):
    start_val = sum([x for x in stocks])
    return start_val

class Stock():
  def __init__(self, name, date, price):
    self.name = name
    self.date = date
    self.price = price

  def Price():
    return self.price

p = Portfolio()

# Fake Stocks
def fake_stock():
  from random import randint, sample
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  name = "".join(sample(list(letters),randint(2,4)))
  price = randint(100,99999)/100
  return (name,price)

def fake_portfolio(n=10,start='20170101',end='20181231'):
  from datetime import date, datetime
  from workdays import workday
  import numpy as np
  from random import randint

  stocks = [fake_stock() for i in range (0, n)]
  dt = datetime.strptime(start, '%Y%m%d')
  result = dict()
  while dt <= datetime.strptime(end, '%Y%m%d'):
    price = [(value[0],round(list(np.random.normal(value[1],value[1]/randint(10,100),1))[0],2)) for key,value in enumerate(stocks)]
    dt = workday(dt,1)
    result[dt.strftime('%Y%m%d')] = price
  return result

port = fake_portfolio()
for k,v in enumerate(port):
  print(v)