#49 starting lines
import pygame as pygame
from UI.UI import Button, Text
# Imports values all files can use
from Items.Community_var import Value, List
from UI.Button_functions import click0, click1
from Items.Item_Dictionary import clickValue
from Items.Items import PPC
import sys

# --- Configuration ---
WIDTH = 1500
HEIGHT = 900
FPS = 60
TITLE = "My Pygame Game"

# --- Initialization ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
mousePos = pygame.mouse.get_pos()


# Game variables
score = Value(0)
items = List()
bttn_range = ((WIDTH/4), HEIGHT)


# Create UI elements
ui = []
buttons = []
texts = []

# UI 
ui.append(pygame.Rect(((WIDTH/4), 0), (10, HEIGHT)))

# Main button
buttons.append(Button((600, 300, 150, 125), (255, 25, 25), click0, (score, clickValue, bttn_range)))
buttons.append(Button((175, 300, 200, 125), (255, 10, 10), click1, (score, items), PPC, text=["Price:", PPC.price, "NONE"]))

texts.append(Text("Score:", score))


# --- Game Loop ---
running = True
while running:
    dt = clock.tick(60) / 1000.0
    mousePos = pygame.mouse.get_pos()
    # 1. Process Input (Events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # See if mouse left clicked
            if pygame.mouse.get_pressed()[0]:
                for button in buttons:
                    button.collide(mousePos)  
                    if button.hover == True:
                        button.click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Mouse is at:", mousePos)

    # 2. Update Game State
    # Add your game logic here (e.g., move sprites, check collisions)


    # 3. Draw (Render)
    screen.fill((175, 175, 175)) # Fill the screen with the background color
    # Add your drawing code here
    # Example: pygame.draw.rect(screen, WHITE, (10, 10, 50, 50))

    # Draw button and check if hovering it
    for button in buttons:
        button.collide(mousePos)
        button.draw(screen, "NONE", "NONE", score)

    # Draw all text on screen
    for text in texts:
        if text.value != "":
            text.update()
        screen.blit(text.surface, (100, 100))
    # Draw all other UI
    for rect in ui:
        pygame.draw.rect(screen, (0, 0, 0), rect)

    # *After* drawing everything, flip the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# --- Quit Pygame ---
pygame.quit()
sys.exit()