import random

class ItemType(object):
    #edible will affect eating food and cooking later
    def __init__(self, name, sellable, edible, baseBuy, baseSell):
        self.name = name
        self.sellable = sellable
        self.edible = edible
        self.baseBuy = baseBuy
        self.baseSell = baseSell

    def __str__(self):
        return self.name

class Item(object):
    #Star value will alter buy and sell price later
    def __init__(self, itemType, star=None):
        self.type = itemType

        if star:
            self.star = star
        else:
            self.star = random.randint(1,5)

    @property
    def buyPrice(self):
        return self.type.baseBuy * self.star

    @property
    def sellPrice(self):
        return self.type.baseSell * self.star

    @property
    def name(self):
        return self.type.name

    def __str__(self):
        return self.name


# (self, name, sellable, edible, buy, sell)
#raw food  = ItemType("", True, True, 4, 2)
blueberry = ItemType("blueberry", True, True, 2, 1)
shijemi = ItemType("shijemi", True, True, 3, 2)
apple = ItemType("apple", True, True, 4, 2)

#crafted food = ItemType("", True, True, 4, 2)
fruit_dish = ItemType("fruit_dish", True, True, 16, 12)

#base  = ItemType("", False, False, 1, 0)
twig = ItemType("twig", False, False, 1, 0)
branch = ItemType("branch", False, False, 3, 0)
bark = ItemType("bark", False, False, 1, 0)
stone = ItemType("stone", False, False, 2, 0)
pebbles = ItemType("pebbles", False, False, 1, 0)
dirt = ItemType("dirt", False, False, 1, 0)

#craft = ItemType("", False, False, 5, 0)
string = ItemType("string", False, False, 5, 0)
cloth = ItemType("cloth", True, False, 15, 11)
brick = ItemType("brick", True, False, 4, 2)
