import random

from player import currentPlayer
from items import *

buyItemTypes = [string, cloth, fruit_dish]

#every item
allItemTypes = {
    "blueberry" : blueberry,
    "twig" : twig,
    "branch" : branch,
    "bark" : bark,
    "stone" : stone,
    "pebbles" : pebbles,
    "string" : string,
    "shijemi" : shijemi,
    "cloth" : cloth,
    "dirt" : dirt,
    "brick" : brick,
    "apple" : apple,
    "fruit_dish" : fruit_dish
}

class Shop(object):
    def __init__(self):
        pass

    @staticmethod
    def buyPrompt(player):
        global buyItemTypes
        itemForSale = Item(random.choice(buyItemTypes))
        print "Here's a cool item to buy: the %s!! Only %s gold!!!" % (itemForSale, itemForSale.buyPrice)
        purchase = raw_input(">")

        if not purchase in ["yes", "y"]:
            return False

        if player.money < itemForSale.buyPrice:
            print "You can't afford that. It costs %s gold and you only have %s." % (itemForSale.buyPrice, player.money)
            return

        player.money -= itemForSale.buyPrice
        player.inventory.add(itemForSale)
        print "You bought a shiny new %s for %s gold." % (itemForSale, itemForSale.buyPrice)


    @staticmethod 
    def sellPrompt(player):
        print "Here's what you can sell right now:"
        player.inventory.printSellable()
        playerInput = raw_input(">")

        if playerInput not in allItemTypes.keys():
            print "That's not a type of item."
            return

        itemType = allItemTypes[playerInput]
        if not itemType.sellable:
            print "Nobody wants to buy that."
            return

        if not player.inventory.containsType(itemType):
            print "You don't have one to sell."
            return

        itemToSell = player.inventory.findType(itemType)
        player.inventory.remove(itemToSell)
        player.money += itemToSell.sellPrice
        print "You sold your %s for %s gold." % (itemToSell, itemToSell.sellPrice)