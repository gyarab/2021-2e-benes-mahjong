import pygame, sys
import os

pygame.init()

FPS = 60
WIN_X, WIN_Y = 800, 500
CARD_WIDTH, CARD_HEIGHT = 100, 150
card_Rect = pygame.Rect(WIN_X / 2 - CARD_WIDTH / 2, WIN_Y / 2 - CARD_HEIGHT / 2, CARD_WIDTH, CARD_HEIGHT)

#karta = pygame.transform.scale(pygame.image.load(""),(100,150))
cards = ["2_of_clubs.png", "3_of_clubs.png", "4_of_clubs.png", "5_of_clubs.png", "6_of_clubs.png", "7_of_clubs.png", "8_of_clubs.png", "9_of_clubs.png", "10_of_clubs.png", "jack_of_clubs.png", "queen_of_clubs.png", "king_of_clubs.png", "ace_of_clubs.png", "2_of_hearts.png", "3_of_hearts.png", "4_of_hearts.png", "5_of_hearts.png", "6_of_hearts.png", "7_of_hearts.png", "8_of_hearts.png", "9_of_hearts.png", "10_of_hearts.png", "jack_of_hearts.png", "queen_of_hearts.png", "king_of_hearts.png", "ace_of_hearts.png", "2_of_diamonds.png", "3_of_diamonds.png", "4_of_diamonds.png", "5_of_diamonds.png", "6_of_diamonds.png", "7_of_diamonds.png", "8_of_diamonds.png", "9_of_diamonds.png", "10_of_diamonds.png", "jack_of_diamonds.png", "queen_of_diamonds.png", "king_of_diamonds.png", "ace_of_diamonds.png", "2_of_spades.png", "3_of_spades.png", "4_of_spades.png", "5_of_spades.png", "6_of_spades.png", "7_of_spades.png", "8_of_spades.png", "9_of_spades.png", "10_of_spades.png", "jack_of_spades.png", "queen_of_spades.png", "king_of_spades.png", "ace_of_spades.png"]
cards2 = []
for i in range(len(cards)):
    cards[i] = pygame.transform.scale(pygame.image.load("cards/" + cards[i]),(CARD_WIDTH, CARD_HEIGHT))
cards2.append(cards[0])
sc = pygame.display.set_mode([WIN_X, WIN_Y]) 
pygame.display.set_caption('karty')
clock = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.SysFont('Arial', 30)
running = True
cislo = 0

def vykreslibalik(pos_x, kterejbalik):
    if kterejbalik:
        sc.blit(kterejbalik[0], pygame.Rect(pos_x, WIN_Y / 2 - CARD_HEIGHT / 2, CARD_WIDTH, CARD_HEIGHT))


def txt(pos,text,size):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text = font.render(text, True, (255, 255, 255))
    txtRect = text.get_rect()
    txtRect.center = pos
    sc.blit(text,txtRect)

def draw():
    sc.fill((0,0,0))
    vykreslibalik(WIN_X / 3 - CARD_WIDTH / 2, cards)
    vykreslibalik((WIN_X / 3) * 2 - CARD_WIDTH / 2, cards2)

    pygame.display.update()



while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cislo += 1
                if cislo >= len(cards): cislo = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if card_Rect.collidepoint(pygame.mouse.get_pos()):
                if cards:
                    cards.pop(cislo)
                if cislo >= len(cards): cislo -= 1

    draw()
pygame.quit()