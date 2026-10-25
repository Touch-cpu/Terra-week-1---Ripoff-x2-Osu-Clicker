import pygame as pygame
import sys

class Value:
    def __init__(self, value):
        self.value = value

class List:
    def __init__(self, value=0):
        if value != 0:
            self.value = [value]
        else:
            self.value = []
    def add(self, value):
        self.value.append(value)