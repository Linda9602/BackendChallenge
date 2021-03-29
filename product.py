

class Product:

    def __init__(self,itemCode):
        self.__itemCode=itemCode
        if itemCode=="GR1":
            self.__price=3.11
            self.__name="Green Tea"
        elif itemCode=="SR1":
            self.__price = 5
            self.__name = "Strawberries"
        elif itemCode=="CF1":
            self.__price = 11.23
            self.__name = "Coffee"
        else:
            print("Invalid Code")

    def getNombre(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def updatePrice(self):
        self.__price = 4.5

    def getItemCode(self):
        return self.__itemCode
















