from pprint import pprint as pp
from itertools import chain, combinations
class  Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + (self.name) + ', ' + str(self.value)  + ', ' + str(self.weight) + '>'
        return result
def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0/item.getWeight()
def density(item):
    return item.getValue()/item.getWeight()
def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if(totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return(result, totalValue)
def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    #values = [175, 90, 20, 50, 10, 200]
    values = [23, 4, 112, 66, 186, 56]
    #weights = [10, 9, 4, 2, 1, 20]
    weights = [10, 1, 15, 13, 17, 12]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print("Total value of this taken is = ", val)#toplam para değerini yazdırıyoruz
    print("Total value of this taken is = ", val)
    for item in taken:
        print('  ', item)
