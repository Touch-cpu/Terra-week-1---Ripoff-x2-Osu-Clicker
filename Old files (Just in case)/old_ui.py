import pygame as pygame
import sys


def dim_color(color, factor=0.5):
    r, g, b = color[:3]
    return (int(r * factor), int(g * factor), int(b * factor))


class Button:
    def __init__(self, position, width, height, color, function, inputs, item = "NONE"):
        self.width = width
        self.height = height
        self.color = color
        self.hover = False

        x = position[0] - (width//2)
        y = position[1] - (height//2)
        self.rect = pygame.Rect((x, y), (width, height))

        self.function = function
        self.inputs = inputs

        self.item = item

    def draw(self, screen):
        if self.hover:
            color = dim_color(self.color, 0.5)
        else:
            color = self.color
        pygame.draw.rect(screen, color, self.rect)

    def drawXY(self, screen, x, y):
        self.rect.x = x
        self.rect.y = y
        if self.hover:
            color = dim_color(self.color, 0.25)
        else:
            color = self.color
        pygame.draw.rect(screen, color, self.rect)

    def collide(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
        else:
            self.hover = False

    def update(self, x,y):
        self.rect = pygame.Rect((x, y), (self.width, self.height))

    def click(self):
        self.function(self, *self.inputs)


class Text:
    def __init__(self, text, value="BLANK", t2="BLANK", size = 0):
        self.txt = text
        if value == "BLANK":
            self.text = text
            self.value = ""
        elif value != "BLANK":
            if t2 == "BLANK":
                self.text =  ", ".join(map(str, (text, value.value)))
                self.t2 = ""
            elif t2 != "BLANK":
                self.text = ", ".join(map(str, (text, value.value, t2)))
                self.t2 = t2
            self.value = value
        if size == 0:
            size = 48
        self.size = 48
        self.font = pygame.font.SysFont(None, self.size)
        self.surface = self.font.render(self.text, True, (255, 255, 255))


    def update(self, value="BLANK"):
        if self.t2 != "":
            self.text = ", ".join(map(str, (self.txt, self.value.value, self.t2)))
        else:
            self.text =  ", ".join(map(str, (self.txt, self.value.value)))

        self.text = self.text.replace(",", "")
        self.surface = self.font.render(self.text, True, (255, 255, 255))
        