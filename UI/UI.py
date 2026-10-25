import pygame as pygame
import sys


def dim_color(color, factor=0.5):
    r, g, b = color[:3]
    return (int(r * factor), int(g * factor), int(b * factor))

def text_init(self, txt, value, t2, sz=0, clr="NONE"):
        text = txt
        if value == "NONE":
            text = txt

        elif value != "NONE":
            if t2 == "NONE":
                if isinstance(value, int):
                    text =  ", ".join(map(str, (txt, value)))
                else:
                    text =  ", ".join(map(str, (txt, value.value)))
            elif t2 != "NONE":
                if isinstance(value, int):
                    text = ", ".join(map(str, (txt, value, t2)))
                else:
                    text =  ", ".join(map(str, (txt, value.value, t2)))

        if sz == 0:
            size = 48
        else:
            size = sz

        if clr == "NONE":
            color = (0, 0, 0)
        else:
            color = clr

        text = text.replace(",", "")
        
        font = pygame.font.SysFont(None, size)
        surface = font.render(text, True, color)
        return surface

class Button():
    def __init__(self, rect, color, function, inputs, item = "NONE", text=["NONE", "NONE", "NONE"]):
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
        self.color = color
        self.function = function
        self.inputs = inputs
        self.hover = False
        
        if item != "NONE":
            self.item = item
            self.hasItem = True
        else:
            self.hasItem = False

        # Text stuff
        if text[0] != "NONE":
            self.hasTxt = True
            self.txt = text[0]
            self.txtVal = text[1]
            self.txtT2 = text[2]
        else:
            self.hasTxt = False


    def draw(self, screen, x="NONE", y="NONE", gscore = "NONE"):
        color = self.color

        if self.hasItem:
            if gscore.value >= self.item.price:
                color = (15, 255, 15)

        if x != "NONE":
            self.rect.x = x
            self.rect.y = y
        if self.hover:
            color = dim_color(color, 0.75)

        pygame.draw.rect(screen, color, self.rect)

        #Text drawing (if on)
        if self.hasTxt == True:
            self.text = text_init(self, self.txt, self.txtVal, self.txtT2)
            if self.hasItem: 
                if self.hover:
                    self.text = text_init(self, self.txt, self.txtVal, self.txtT2)
                else:
                    self.text = text_init(self, self.item.name, "NONE", "NONE", 34)

            text_rect = self.text.get_rect(center=self.rect.center)
            screen.blit(self.text,(text_rect))
        # screen.blit(button.text, (button.rect.x, button.rect.y))

    def collide(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
        else:
            self.hover = False

    def update(self, x,y):
        self.rect = pygame.Rect((x, y), (self.rect.w, self.rect.h))
        if self.hasTxt:
            self.text = text_init(self, self.txt, self.txtVal, self.txtT2)
            screen.blit(self.text, (self.rect.x, self.rect.y))

    def click(self):
        self.function(self, *self.inputs)


class Text():
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


class Slider():
    def __init__(self, value, text=["NONE", "NONE", "NONE"]):
        self.value = value

        # Text stuff
        if text[0] != "NONE":
            self.hasTxt = True
            self.txt = text[0]
            self.txtVal = text[1]
            self.txtT2 = text[2]
        else:
            self.hasTxt = False
