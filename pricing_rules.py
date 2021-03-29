from abc import ABC, abstractmethod
from product import *


class PricingRules(ABC):
    @abstractmethod
    def apply(self, products):
        pass


class MoreThanThree(PricingRules):

    def apply(self, products):
        total = 0
        for product in products:
            if product.getItemCode() == 'SR1':
                total = total + 1
            if total >= 3:
                return True
        return False

class BuyOneGetOneFree(PricingRules):

    def apply(self, products):
        if len(products) > 1:
            return True
        return False
