

# class Stock():
#   def __init__(self, ):

# Fake Stocks
def fake_stock():
  from random import randint, sample
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  name = "".join(sample(list(letters),randint(2,4)))
  price = randint(100,99999)/100
  return (name,price)

def fake_portfolio(n=10,start='20181225',end='20181231'):
  from datetime import date, datetime
  from workdays import workday
  import numpy as np
  from random import randint

  stocks = [fake_stock() for i in range (0, n)]
  dt = datetime.strptime(start, '%Y%m%d')
  while dt <= datetime.strptime(end, '%Y%m%d'):
    price = [(value[0],round(list(np.random.normal(value[1],value[1]/randint(10,100),1))[0],2)) for key,value in enumerate(stocks)]
    print(price)
    dt = workday(dt,1)
    print(dt.strftime('%Y%m%d'))

  # for i in range(0,stocks):
  #   print(i)

fake_portfolio()