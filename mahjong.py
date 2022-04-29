import pygame, sys
import random

pygame.init()

FPS = 60
WIN_X, WIN_Y = 1080, 720
TILE_WIDTH, TILE_HEIGHT = 50, 65
BARVA_PATRO_1, BARVA_PATRO_2, BARVA_PATRO_3, BARVA_PATRO_4 = (222, 0, 0), (0, 8, 230), (172, 0, 181), (252, 186, 3)
SCENA = "menu"
active_position = ()

sc = pygame.display.set_mode([WIN_X, WIN_Y]) 
pygame.display.set_caption('')
clock = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.SysFont('Arial', 15)
font_shuffle = pygame.font.SysFont('Verdana', 25)
font_nadpis = pygame.font.SysFont('Verdana', 60)
font_hrat_znovu = pygame.font.SysFont('Verdana', 40)
jde_hrat_hodnota = True
vyhra_hodnota = False
running = True

posun = 6 # uhel pohledu hry

shuffle_button_pos = pygame.Rect((WIN_X - 150) / 2, 620, 150, 60)
hrat_btn_pos = (WIN_X/2 - 150, WIN_Y/2 + 100, 300, 100)

#########################################################################

tiles_img = ["FourCircles.png", "ThreeCircles.png", "TwoCircles.png", "GreenCircle.png"]

patro1_width = 12
patro2_width = 6
patro3_width = 4
patro4_width = 2

dead_spots = [(0,1),(0,2),(0,5),(0,6),(1,1),(1,6),(10,1),(10,6),(11,1),(11,2),(11,5),(11,6)] #(nepravidelny rozlozeni hraci plochy)

def map_generation():
    for x in range(12):
        for y in range(8):
            if patro1[y][x] != "x":
                num = random.choice(tile)
                patro1[y][x] = num               #prideli ho platnymu policku
                tile.remove(num)                          #a pak ho odebere z tile[]
    for x in range(6):
        for y in range(6):
            if patro2[y][x] != "x":
                num = random.choice(tile)
                patro2[y][x] = num               #prideli ho platnymu policku
                tile.remove(num)                        #a pak ho odebere z tile[]
    for x in range(4):
        for y in range(4):
            if patro3[y][x] != "x":
                num = random.choice(tile)
                patro3[y][x] = num               #prideli ho platnymu policku
                tile.remove(num)                          #a pak ho odebere z tile[]
    for x in range(2):
        for y in range(2):
            if patro4[y][x] != "x":
                num = random.choice(tile)
                patro4[y][x] = num               #prideli ho platnymu policku
                tile.remove(num)                        #a pak ho odebere z tile[]

    #if not jde_hrat(): shuffle()
    print(tile)

def nova_hra():
    global patro1, patro2, patro3, patro4, tile
    patro1 = [["o" for i in range(patro1_width)] for j in range(8)]  #udela mrizku "o" pro kazdy patro
    patro2 = [["o" for i in range(patro2_width)] for j in range(6)]   
    patro3 = [["o" for i in range(patro3_width)] for j in range(4)]
    patro4 = [["o" for i in range(patro4_width)] for j in range(2)]
    for i in dead_spots:
        patro1[i[1]][i[0]] = "x"  #na dead spoty vypise "x"
    tile = []
    for i in range(35):
        for y in range(4): # máme 152 políček - 12 dead policek
            tile.append(i)
    jde_hrat_hodnota = True
    vyhra_hodnota = False
    map_generation()

def jde_hrat() -> bool:
    dvojce = []
    for x in range(12):     #prvni patro
        for y in range(8):
            if patro1[y][x] != "x" and ((x == 0 or patro1[y][x - 1] == "x") or (x == patro1_width - 1 or patro1[y][x + 1] == "x")):
                if patro1[y][x] in dvojce:
                    if y >= 1 and x >= 3 and y - 1 < 6 and x - 3 < 6:
                        if patro2[y-1][x-3] == "x":
                            return True
                    else: return True
                else:
                    if y >= 1 and x >= 3 and y - 1 < 6 and x - 3 < 6:
                        if patro2[y-1][x-3] == "x":
                            dvojce.append(patro1[y][x])
                    else: dvojce.append(patro1[y][x])

    for x in range(6):     #druhe patro
        for y in range(6):
            if patro2[y][x] != "x" and ((x == 0 or patro2[y][x - 1] == "x") or (x == 5 or patro2[y][x + 1] == "x")):
                if patro2[y][x] in dvojce:
                    if y >= 1 and x >= 1 and y - 1 < 4 and x - 1 < 4:
                        if patro3[y-1][x-1] == "x":
                            return True
                    else: return True
                else:
                    if y >= 1 and x >= 1 and y - 1 < 4 and x - 1 < 4:
                        if patro2[y-1][x-1] == "x":
                            dvojce.append(patro2[y][x])
                    else: dvojce.append(patro2[y][x])

    for x in range(4):     #treti patro
        for y in range(4):
            if patro3[y][x] != "x" and ((x == 0 or patro3[y][x - 1] == "x") or (x == 3 or patro3[y][x + 1] == "x")):
                if patro3[y][x] in dvojce:
                    if y >= 1 and x >= 1 and y - 1 < 2 and x - 1 < 2:
                        if patro4[y-1][x-1] == "x":
                            return True
                    else: return True
                else:
                    if y >= 1 and x >= 1 and y - 1 < 2 and x - 1 < 2:
                        if patro2[y-1][x-1] == "x":
                            dvojce.append(patro3[y][x])
                    else: dvojce.append(patro3[y][x])
    
    for x in range(2):     #ctvrte patro
        for y in range(2):
            if patro4[y][x] in dvojce and patro4[y][x] != "x":
                return True
            else: dvojce.append(patro4[y][x])

    return False

def shuffle():
    ##### VYBERU VŠECHNY POLICKA #####

    for x in range(12):     #prvni patro
        for y in range(8):
            if patro1[y][x] != "x":
                tile.append(patro1[y][x])
                patro1[y][x] = "o"
    
    for x in range(6):     #druhe patro
        for y in range(6):
            if patro2[y][x] != "x":
                tile.append(patro2[y][x])
                patro2[y][x] = "o"
            
    for x in range(4):     #treti patro
        for y in range(4):
            if patro3[y][x] != "x":
                tile.append(patro3[y][x])
                patro3[y][x] = "o"
    
    for x in range(2):     #ctvrte patro
        for y in range(2):
            if patro4[y][x] != "x":
                tile.append(patro4[y][x])
                patro4[y][x] = "o"

    ##### NASAZIME JE ZPÁTKY #####

    for x in range(12):     #prvni patro
        for y in range(8):
            if patro1[y][x] == "o":
                policko = random.choice(tile)
                patro1[y][x] = policko
                tile.remove(policko)
    
    for x in range(6):     #druhe patro
        for y in range(6):
            if patro2[y][x] == "o":
                policko = random.choice(tile)
                patro2[y][x] = policko
                tile.remove(policko)
            
    for x in range(4):     #treti patro
        for y in range(4):
            if patro3[y][x] == "o":
                policko = random.choice(tile)
                patro3[y][x] = policko
                tile.remove(policko)
    
    for x in range(2):     #ctvrte patro
        for y in range(2):
            if patro4[y][x] == "o":
                policko = random.choice(tile)
                patro4[y][x] = policko
                tile.remove(policko)
    
    if not jde_hrat(): shuffle() # REKURZEEEEEEEEEEEEEEEEEE
    else: jde_hrat_hodnota = True
    print("shuffle")

def vyhra():
    for x in range(12):     #prvni patro
        for y in range(8):
            if patro1[y][x] != "x":
                return False
    
    for x in range(6):     #druhe patro
        for y in range(6):
            if patro2[y][x] != "x":
                return False
            
    for x in range(4):     #treti patro
        for y in range(4):
            if patro3[y][x] != "x":
                return False
    
    for x in range(2):     #ctvrte patro
        for y in range(2):
            if patro4[y][x] != "x":
                return False
    return True

def draw():
    if SCENA == "menu":
        sc.fill((255, 225, 175))

        txt = font_nadpis.render("Mahjong Solitare", True, (0,0,0))
        txtRect = txt.get_rect()
        txtRect.center = (WIN_X/2, WIN_Y/2 - 200)
        sc.blit(txt, txtRect)

        if pygame.Rect(hrat_btn_pos).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(sc, (250,250,250), hrat_btn_pos, 0, 5)
        else: pygame.draw.rect(sc, (220,220,220), hrat_btn_pos, 0, 5)
        pygame.draw.rect(sc, (100,100,100), hrat_btn_pos, 5, 5)

        if vyhra_hodnota: txt = font_shuffle.render("Hrát znovu", True, (0,0,0))
        else: txt = font_shuffle.render("Hrát", True, (0,0,0))
        txtRect = txt.get_rect()
        txtRect.center = pygame.Rect(hrat_btn_pos).center
        sc.blit(txt, txtRect)

        if vyhra_hodnota:
            txt = font_hrat_znovu.render("Vyhrál jsi!", True, (0,0,0))
            txtRect = txt.get_rect()
            txtRect.center = (WIN_X/2, WIN_Y/2 + 70)
            sc.blit(txt, txtRect)

    elif SCENA == "hra":
        sc.fill((255, 225, 175))
        
        for x in range(12):     #prvni patro
            for y in range(8):
                if patro1[y][x] != "x":
                    pygame.draw.rect(sc, (255, 255, 255), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6, y * (TILE_HEIGHT + 2) + 50, TILE_WIDTH, TILE_HEIGHT), 0, 10)
                    #na kazdy platny policko vykresli rect
                    if active_position != (x, y, 1):
                        pygame.draw.rect(sc, BARVA_PATRO_1, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6, y * (TILE_HEIGHT + 2) + 50, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud neni aktivni, obtazeno defaultní barvou patra
                    elif active_position[2] == 1:
                        pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6, y * (TILE_HEIGHT + 2) + 50, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud je aktivni, obtazeno zelenou
                    text = font1.render(str(patro1[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                    sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2, y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2))
        
        for x in range(6):     #druhe patro
            for y in range(6):
                if patro2[y][x] != "x":
                    if patro1[y+1][x+3] != "x":
                        pygame.draw.rect(sc, (0, 0, 0), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2), y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2), TILE_WIDTH, TILE_HEIGHT), 0, 10)

                    pygame.draw.rect(sc, (255, 255, 255), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2) - posun, y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2) - posun, TILE_WIDTH, TILE_HEIGHT), 0, 10)
                    #na kazdy platny policko vykresli rect
                    if active_position != (x, y, 2):
                        pygame.draw.rect(sc, BARVA_PATRO_2, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2) - posun, y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2) - posun, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud neni aktivni, obtazeno defaultní barvou patra
                    elif active_position[2] == 2:
                        pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2) - posun, y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2) - posun, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud je aktivni, obtazeno zelenou
                    text = font1.render(str(patro2[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                    sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2 + 3 * (TILE_WIDTH + 2) - posun, y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2 + 1 * (TILE_HEIGHT + 2)  - posun))
        
        for x in range(4):     #treti patro
            for y in range(4):
                if patro3[y][x] != "x":
                    if patro2[y+1][x+1] != "x":
                        pygame.draw.rect(sc, (0, 0, 0), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2) - posun, y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2) - posun, TILE_WIDTH, TILE_HEIGHT), 0, 10)

                    pygame.draw.rect(sc, (255, 255, 255), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2) - posun*2, y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2) - posun*2, TILE_WIDTH, TILE_HEIGHT), 0, 10)
                    #na kazdy platny policko vykresli rect
                    if active_position != (x, y, 3):
                        pygame.draw.rect(sc, BARVA_PATRO_3, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2) - posun*2, y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2) - posun*2, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud neni aktivni, obtazeno defaultní barvou patra
                    elif active_position[2] == 3:
                        pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2) - posun*2, y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2) - posun*2, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud je aktivni, obtazeno zelenou
                    text = font1.render(str(patro3[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                    sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2 + 4 * (TILE_WIDTH + 2) - posun*2, y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2 + 2 * (TILE_HEIGHT + 2) - posun*2))
        
        for x in range(2):     #ctvrte patro
            for y in range(2):
                if patro4[y][x] != "x":
                    if patro2[y+1][x+1] != "x":
                        pygame.draw.rect(sc, (0, 0, 0), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2) - posun*2, y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2) - posun*2, TILE_WIDTH, TILE_HEIGHT), 0, 10)

                    pygame.draw.rect(sc, (255, 255, 255), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2) - posun*3, y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2) - posun*3, TILE_WIDTH, TILE_HEIGHT), 0, 10)
                    #na kazdy platny policko vykresli rect
                    if active_position != (x, y, 4):
                        pygame.draw.rect(sc, BARVA_PATRO_4, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2) - posun*3, y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2) - posun*3, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud neni aktivni, obtazeno defaultní barvou patra
                    elif active_position[2] == 4:
                        pygame.draw.rect(sc, (50, 220, 85), (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2) - posun*3, y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2) - posun*3, TILE_WIDTH, TILE_HEIGHT), 5, 10)
                    #pokud je aktivni, obtazeno zelenou
                    text = font1.render(str(patro4[y][x]), True, (0, 0, 0)) #na policko napise jeho cislo (docasny)
                    sc.blit(text, (x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + TILE_WIDTH / 2 + 5 * (TILE_WIDTH + 2) - posun*3, y * (TILE_HEIGHT + 2) + 50 + TILE_HEIGHT // 2 + 3 * (TILE_HEIGHT + 2) - posun*3))
        
        if not jde_hrat_hodnota:
            if shuffle_button_pos.collidepoint(pygame.mouse.get_pos()):
                button = pygame.draw.rect(sc, (255, 255, 255), shuffle_button_pos, 0, 5)
            else: button = pygame.draw.rect(sc, (220, 220, 220), shuffle_button_pos, 0, 5)
            pygame.draw.rect(sc, (0,0,0), shuffle_button_pos, 2, 5)
            txt = font_shuffle.render("Shuffle", True, (0,0,0))
            txtRect = txt.get_rect()
            txtRect.center = button.center
            sc.blit(txt, txtRect)

    pygame.display.flip()


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if SCENA == "hra":
                different_patro_interaction = False
                for x in range(2):
                    for y in range(2):
                        if pygame.Rect(x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 5 * (TILE_WIDTH + 2) - posun*3, y * (TILE_HEIGHT + 2) + 50 + 3 * (TILE_HEIGHT + 2) - posun*3, TILE_WIDTH + posun*3, TILE_HEIGHT+ posun*3).collidepoint(pygame.mouse.get_pos()):
                            #pokud kliknes mysi na policko
                            if patro4[y][x] != "x":
                                different_patro_interaction = True
                                if active_position == ():  #jesli neni aktivni
                                    if x == 0 or x == patro4_width - 1: #pokud je odhaleny
                                        active_position = (x, y, 4)
                                #tady uz klikas druhy policko, jelikoz aktivni uz existuje
                                elif not (x == active_position[0] and y == active_position[1] and active_position[2] == 4): #pokud ses netrefil do aktivniho (sam sebe)...
                                    if x == 0 or x == patro4_width - 1 or patro4[y][x - 1] == "x" or patro4[y][x + 1] == "x": #pokud je odhaleny
                                        if patro4[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                            patro4[y][x] = "x"
                                            globals()['patro%s' % active_position[2]][active_position[1]][active_position[0]] = "x"
                                            jde_hrat_hodnota = jde_hrat()
                                            vyhra_hodnota = vyhra()
                                        active_position = ()
                                else: active_position = ()  #netrefil ses, vypni aktivni policko
                if not different_patro_interaction:
                    for x in range(4):
                        for y in range(4):
                            if pygame.Rect(x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 4 * (TILE_WIDTH + 2) - posun*2, y * (TILE_HEIGHT + 2) + 50 + 2 * (TILE_HEIGHT + 2) - posun*2, TILE_WIDTH + posun*2, TILE_HEIGHT + posun*2).collidepoint(pygame.mouse.get_pos()):
                                #pokud kliknes mysi na policko
                                if patro3[y][x] != "x":
                                    different_patro_interaction = True
                                    if active_position == ():  #jesli neni aktivni
                                        if x == 0 or x == patro3_width - 1 or patro3[y][x - 1] == "x" or patro3[y][x + 1] == "x": #pokud je odhaleny
                                            active_position = (x, y, 3)
                                    #tady uz klikas druhy policko, jelikoz aktivni uz existuje
                                    elif not (x == active_position[0] and y == active_position[1] and active_position[2] == 3): #pokud ses netrefil do aktivniho (sam sebe)...
                                        if x == 0 or x == patro3_width - 1 or patro3[y][x - 1] == "x" or patro3[y][x + 1] == "x": #pokud je odhaleny
                                            if patro3[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                                patro3[y][x] = "x"
                                                globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]] = "x"
                                                jde_hrat_hodnota = jde_hrat()
                                                vyhra_hodnota = vyhra()
                                            active_position = ()
                                    else: active_position = ()  #netrefil ses, vypni aktivni policko
                if not different_patro_interaction:                
                    for x in range(6):
                        for y in range(6):
                            if pygame.Rect(x * (TILE_WIDTH + 2) + WIN_X / 2 - (TILE_WIDTH + 2) * 6 + 3 * (TILE_WIDTH + 2) - posun, y * (TILE_HEIGHT + 2) + 50 + 1 * (TILE_HEIGHT + 2)- posun, TILE_WIDTH + posun, TILE_HEIGHT + posun).collidepoint(pygame.mouse.get_pos()):
                                #pokud kliknes mysi na policko
                                if patro2[y][x] != "x":
                                    different_patro_interaction = True
                                    if active_position == ():  #jesli neni aktivni
                                        if x == 0 or x == patro2_width - 1 or patro2[y][x - 1] == "x" or patro2[y][x + 1] == "x": #pokud je odhaleny
                                            active_position = (x, y, 2)
                                    #tady uz klikas druhy policko, jelikoz aktivni uz existuje
                                    elif not (x == active_position[0] and y == active_position[1] and active_position[2] == 2): #pokud ses netrefil do aktivniho (sam sebe)...
                                            if x == 0 or x == patro2_width - 1 or patro2[y][x - 1] == "x" or patro2[y][x + 1] == "x": #pokud je odhaleny
                                                if patro2[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                                    patro2[y][x] = "x"
                                                    globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]] = "x"
                                                    jde_hrat_hodnota = jde_hrat()
                                                    vyhra_hodnota = vyhra()
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
                                    elif not (x == active_position[0] and y == active_position[1] and active_position[2] == 1): #pokud ses netrefil do aktivniho (sam sebe)...
                                        if x == 0 or x == patro1_width - 1 or patro1[y][x - 1] == "x" or patro1[y][x + 1] == "x": #pokud je odhaleny
                                            if patro1[y][x] == globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]]: #trefil ses spravne! obe policka smaz
                                                patro1[y][x] = "x"
                                                globals()[f"patro{active_position[2]}"][active_position[1]][active_position[0]] = "x"
                                                jde_hrat_hodnota = jde_hrat()
                                                vyhra_hodnota = vyhra()
                                            active_position = ()
                                    else: active_position = ()  #netrefil ses, vypni aktivni policko

            if not jde_hrat_hodnota and shuffle_button_pos.collidepoint(pygame.mouse.get_pos()):
                shuffle()
            
            if vyhra_hodnota: SCENA = "menu"
            
            elif SCENA == "menu":

                if pygame.Rect(hrat_btn_pos).collidepoint(pygame.mouse.get_pos()):
                    print("inunjuv")
                    SCENA = "hra"
                    nova_hra()

    draw()

pygame.quit()