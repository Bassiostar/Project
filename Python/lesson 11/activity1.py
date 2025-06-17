class Computer:
    def __init__(self):
        self._maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self._maxprice))

    def set_max_price(self, price):
        self._maxprice = price
# hello
c = Computer()
c.sell()

c._maxprice = 1000
c.sell()

c.set_max_price(1000)
c.sell()