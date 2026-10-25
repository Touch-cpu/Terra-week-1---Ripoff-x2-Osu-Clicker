import pygame as pygame
from UI.UI import Button, Text
# Imports values all files can use
from Items.Community_var import Value, List
from UI.Button_functions import click0, click1
from Items.Item_Functions import points_per_click
import sys
clickValue = Value(1)

"""
ITEM Dictionary outline

item = {
    "name": str ,
    "desc": str ,
    "price": int ,
    "owned": bool ,
    "unlck": bool ,

    # Basic function
    "func": function ,
    "args": arguments for the function ,

    # Multi buy and Looping affect
    "multibuy": bool ,
    "loop": bool ,
    "time": int ,

    # Price Increases
    "increase": int ,
    "getprice": lambda ,
    "amt": int ,
}

"""
PPC_def = {
    "name": "Points Per Click" ,
    "desc": "Points per click" ,
    "price": 10 ,
    "owned": False ,
    "unlck": True ,

    "func": points_per_click ,
    "args": (clickValue, 0) ,

    "multibuy": True ,
    "loop": False ,
    "getprice": lambda v, n: int(v * 15 * (1.15 ** n)) ,
    "amt": 0 ,
}