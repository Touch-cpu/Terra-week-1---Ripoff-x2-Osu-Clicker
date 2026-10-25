# Imports
import pygame as pygame
from Items.Item_Dictionary import PPC_def
from Items.Item_Dictionary import clickValue
import sys

# Define the Item class
class Item:
    # Initialize
    def __init__(self, item):
        self.item = item
        for key, value in item.items():
            setattr(self, key, value)

    def use(self):
        # Call self's function with it's arguments
        self.function(self, *self.args)

    def price_up(self):
        # Update the item's price
        self.price = self.getprice(clickValue.value, self.amt)

# Items
PPC = Item(PPC_def)