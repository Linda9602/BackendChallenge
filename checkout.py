# -*- coding: utf-8 -*
from basket import *
from pricing_rules import *

class Checkout:
    def __init__(self,princing_rules):
        self.princing_rules = princing_rules
        self.basket = Basket()
        self.total_price = 0

    def scan(self, item_code):
        if item_code != "No":
            product = Product(item_code)
            self.basket.addProduct(product)
            self.total_price += product.getPrice()
            next_item_code = input("Write code of the next product or write No to finish the purchase:")
            self.scan(next_item_code)
        else:
            return

    def total(self):
        for rule in self.princing_rules:
            if type(rule) is MoreThanThree and rule.apply(self.basket.products):
                self.total_price = 0
                for product in self.basket.products:
                    if product.getItemCode() == 'SR1':
                        product.updatePrice()
                        self.total_price = self.total_price + product.getPrice()
                    else :
                        self.total_price = self.total_price + product.getPrice()

            if type(rule) is BuyOneGetOneFree and rule.apply(self.basket.products):
                self.total_price = self.total_price - 3.11

        return self.total_price

