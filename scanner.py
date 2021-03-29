
from pricing_rules import *
from checkout import *


rule1 = BuyOneGetOneFree()
rule2 = MoreThanThree()
pricing_rules = [rule1,rule2]

checkout = Checkout(pricing_rules)

item_code = input("Write code of a product: ")
checkout.scan(item_code)
print("The purchase price " + str(checkout.total()) + '$')


