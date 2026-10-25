import pygame as pygame
import random
import sys

"""
Button type list:
    0 - Main/Clicker
    1 - Buy


"""
# Main clicking button
def click0(button, score, add, range):
    # Add click value to the score
    score.value += add.value

    # Move button to a random locations
    x = random.randint(round((range[0]/5) * 3 + (button.rect.width)), round((range[0]*3) - button.rect.width))
    y = random.randint(round(button.rect.height), round(range[1] - button.rect.height))
    button.update(x, y)

# Shop button funtion
def click1(button, score, items):
    # Checking if you have enough money
    if score.value - button.item.price >= 0:
        # Take away money spent from score
        score.value  -= button.item.price
        # Update item's price, set it to being owned, and add to items list
        if button.item.multibuy:
            button.item.price_up()
        button.item.owned = True
        print("Bought!")
        items.add(button.item)
        # If item doesn't loop then don't loop it
        if not button.item.loop:
            button.item.func(*button.item.args)
        button.item.amt += 1
        button.txtVal = button.item.price