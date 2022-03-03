import pygame, sys
import random

pygame.init()

FPS = 60
WIN_X, WIN_Y = 1080, 720
TILE_WIDTH, TILE_HEIGHT = 50, 65
active_position = ()


sc = pygame.display.set_mode([WIN_X, WIN_Y]) 
pygame.display.set_caption('')
clock = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.SysFont('Arial', 15)
running = True

#########################################################################

tiles_img = ["FourCircles.png", "ThreeCircles.png", "TwoCircles.png", "GreenCircle.png"]
tile = []
for i in range(35):
    for j in range(4):
        tile.append(i)    #do tile[] frajer nacte vsechny cisla desticek

patro1_width = 12
patro2_width = 6
patro3_width = 4
patro4_width = 2
patro1 = [["o" for i in range(patro1_width)] for j in range(8)]  #udela mrizku "o" pro kazdy patro
patro2 = [["o" for i in range(patro2_width)] for j in range(6)]   
patro3 = [["o" for i in range(patro3_width)] for j in range(4)]
patro4 = [["o" for i in range(patro4_width)] for j in range(2)]

dead_spots = [(0,1),(0,2),(0,5),(0,6),(1,1),(1,6),(10,1),(10,6),(11,1),(11,2),(11,5),(11,6)] #(nepravidelny rozlozeni hraci plochy)

for i in dead_spots:
    patro1[i[1]][i[0]] = "x"  #na dead spoty vypise "x"

def map_generation():
    for x in range(12):
        for y in range(8):
            if patro1[y][x] != "x":
                r = random.randint(0, len(tile) - 1) #nastavi nahodny cislo z cisel v tile[]
                patro1[y][x] = tile[r]               #prideli ho platnymu policku
                tile.pop(r)                          #a pak ho odebere z tile[]
    for x in range(6):
        for y in range(6):
            r = random.randint(0, len(tile) - 1)     # stejny akorat druhy patro atd...
            patro2[y][x] = tile[r] 
            tile.pop(r)
    for x in range(4):
        for y in range(4):
            r = random.randint(0, len(tile) - 1)
            patro3[y][x] = tile[r]
            tile.pop(r)
    for x in range(2):
        for y in range(2):
            r = random.randint(0, len(tile) - 1)
            patro4[y][x] = tile[r]
            tile.pop(r)

def draw():
    sc.fill((255, 225, 175))
    for x in range(12):     #prvni patro
        for y in range(8):
            if patro1[y][x] != "x":
                pygame.draw.rect(sc, (255, 255, 255), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6, y * (TILE_HEIGHT + 2) + 50, TILE_WIDTH, TILE_HEIGHT), 0, 10)
                #na kazdy platny policko vykresli rect
                if active_position != (x, y, 1):
                    pygame.draw.rect(sc, (0, 0, 0), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6, y * (TILE_HEIGHT + 2) + 50, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud neni aktivni, obtazeno cernou
                elif active_position[2] == 1:
                    pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6, y * (TILE_HEIGHT + 2) + 50, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud je aktivni, obtazeno zelenou
                text = font1.render(str(patro1[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2, y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2))
    
    for x in range(6):     #druhe patro
        for y in range(6):
            if patro2[y][x] != "x":
                pygame.draw.rect(sc, (200, 200, 200), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 0, 10)
                #na kazdy platny policko vykresli rect
                if active_position != (x, y, 2):
                    pygame.draw.rect(sc, (0, 0, 0), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud neni aktivni, obtazeno cernou
                elif active_position[2] == 2:
                    pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud je aktivni, obtazeno zelenou
                text = font1.render(str(patro2[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2 + 3 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2 + 1 * (TILE_HEIGHT + 2)))
    for x in range(4):     #treti patro
        for y in range(4):
            if patro3[y][x] != "x":
                pygame.draw.rect(sc, (150, 150, 150), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 0, 10)
                #na kazdy platny policko vykresli rect
                if active_position != (x, y, 3):
                    pygame.draw.rect(sc, (0, 0, 0), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud neni aktivni, obtazeno cernou
                elif active_position[2] == 3:
                    pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud je aktivni, obtazeno zelenou
                text = font1.render(str(patro3[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2 + 4 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2 + 2 * (TILE_HEIGHT + 2)))
    for x in range(2):     #ctvrte patro
        for y in range(2):
            if patro4[y][x] != "x":
                pygame.draw.rect(sc, (100, 100, 100), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 0, 10)
                #na kazdy platny policko vykresli rect
                if active_position != (x, y, 4):
                    pygame.draw.rect(sc, (0, 0, 0), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud neni aktivni, obtazeno cernou
                elif active_position[2] == 4:
                    pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 5, 10)
                #pokud je aktivni, obtazeno zelenou
                text = font1.render(str(patro4[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2 + 5 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2 + 3 * (TILE_HEIGHT + 2)))
    
    pygame.display.flip()

map_generation()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            different_patro_interaction = False
            for x in range(2):
                for y in range(2):
                    if pygame.Rect(x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT).collidepoint(pygame.mouse.get_pos()):
                        #pokud kliknes mysi na policko
                        if patro4[y][x] != "x":
                            different_patro_interaction = True
                            if active_position == ():  #jesli neni aktivni
                                if x == 0 or x == patro4_width - 1 or patro4[y][x - 1] == "x" or patro4[y][x + 1] == "x": #pokud je odhaleny
                                    active_position = (x, y, 4)
                            #tady uz klikas druhy policko, jelikoz aktivni uz existuje
                            elif not (x == active_position[0] and y == active_position[1]): #pokud ses netrefil do aktivniho (sam sebe)...
                                if x == 0 or x == patro4_width - 1 or patro4[y][x - 1] == "x" or patro4[y][x + 1] == "x": #pokud je odhaleny
                                    if patro4[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                        patro4[y][x] = "x"
                                        globals()['patro%s' % active_position[2]][active_position[1]][active_position[0]] = "x"
                                    active_position = ()
                            else: active_position = ()  #netrefil ses, vypni aktivni policko
            if not different_patro_interaction:
                for x in range(4):
                    for y in range(4):
                        if pygame.Rect(x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT).collidepoint(pygame.mouse.get_pos()):
                            #pokud kliknes mysi na policko
                            if patro3[y][x] != "x":
                                different_patro_interaction = True
                                if active_position == ():  #jesli neni aktivni
                                    if x == 0 or x == patro3_width - 1 or patro3[y][x - 1] == "x" or patro3[y][x + 1] == "x": #pokud je odhaleny
                                        active_position = (x, y, 3)
                                #tady uz klikas druhy policko, jelikoz aktivni uz existuje
                                elif not (x == active_position[0] and y == active_position[1]): #pokud ses netrefil do aktivniho (sam sebe)...
                                    if x == 0 or x == patro3_width - 1 or patro3[y][x - 1] == "x" or patro3[y][x + 1] == "x": #pokud je odhaleny
                                        if patro3[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                            patro3[y][x] = "x"
                                            globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]] = "x"
                                        active_position = ()
                                else: active_position = ()  #netrefil ses, vypni aktivni policko
            if not different_patro_interaction:                
                for x in range(6):
                    for y in range(6):
                        if pygame.Rect(x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT).collidepoint(pygame.mouse.get_pos()):
                            #pokud kliknes mysi na policko
                            if patro2[y][x] != "x":
                                different_patro_interaction = True
                                if active_position == ():  #jesli neni aktivni
                                    if x == 0 or x == patro2_width - 1 or patro2[y][x - 1] == "x" or patro2[y][x + 1] == "x": #pokud je odhaleny
                                        active_position = (x, y, 2)
                                #tady uz klikas druhy policko, jelikoz aktivni uz existuje
                                elif not (x == active_position[0] and y == active_position[1]): #pokud ses netrefil do aktivniho (sam sebe)...
                                        if x == 0 or x == patro2_width - 1 or patro2[y][x - 1] == "x" or patro2[y][x + 1] == "x": #pokud je odhaleny
                                            if patro2[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                                patro2[y][x] = "x"
                                                globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]] = "x"
                                            active_position = ()
                                else: active_position = ()  #netrefil ses, vypni aktivni policko
            if not different_patro_interaction:
                for x in range(12):
                    for y in range(8):
                        if pygame.Rect(x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6, y * (TILE_HEIGHT + 2) + 50, TILE_WIDTH, TILE_HEIGHT).collidepoint(pygame.mouse.get_pos()):
                            #pokud kliknes mysi na policko
                            if patro1[y][x] != "x":
                                different_patro_interaction = True
                                if active_position == ():  #jesli neni aktivni
                                    if x == 0 or x == patro1_width - 1 or patro1[y][x - 1] == "x" or patro1[y][x + 1] == "x": #pokud je odhaleny
                                        active_position = (x, y, 1)
                                #tady uz klikas druhy policko, jelikoz aktivni uz existuje
                                elif not (x == active_position[0] and y == active_position[1]): #pokud ses netrefil do aktivniho (sam sebe)...
                                    if x == 0 or x == patro1_width - 1 or patro1[y][x - 1] == "x" or patro1[y][x + 1] == "x": #pokud je odhaleny
                                        if patro1[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                            patro1[y][x] = "x"
                                            globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]] = "x"
                                        active_position = ()
                            else: active_position = ()  #netrefil ses, vypni aktivni policko
                            
            


    draw()

pygame.quit()