import random
import pygame

# Pygame inicializálása
pygame.init()

# Képernyő beállításai (Szélesség, Magasság)
SZEL = 800
MAG = 600
ablak = pygame.display.set_mode((SZEL, MAG))
pygame.display.set_caption("Első 2D Python Játékom")

# Színek (RGB kódok: Piros, Zöld, Kék)
FEHER = (255, 255, 255)
KEX = (30, 144, 255)
PIROS = (220, 20, 60)
FEKETE = (20, 20, 20)
ZOLD = (50, 205, 50)

# Játékos (kosár) adatai
kosar_szelesseg = 100
kosar_magassag = 20
kosar_x = SZEL // 2 - kosar_szelesseg // 2
kosar_y = MAG - 50
kosar_sebesseg = 8

# Potyogó tárgy (alma / akadály) adatai
targy_meret = 30
targy_x = random.randint(0, SZEL - targy_meret)
targy_y = 0
targy_sebesseg = 4

# Pontszám
pontszam = 0
betutipus = pygame.font.SysFont(None, 36)

# Fő Játék Ciklus (Game Loop)
fut = True
ora = pygame.time.Clock()

while fut:
    # 1. Események kezelése (pl. kilépés a ablak bezárásakor)
    for esemeny in pygame.event.get():
        if esemeny.type == pygame.QUIT:
            fut = False

    # 2. Billentyűzet lenyomások figyelése (Irányítás)
    billentyuk = pygame.key.get_pressed()
    if billentyuk[pygame.K_LEFT] and kosar_x > 0:
        kosar_x -= kosar_sebesseg
    if billentyuk[pygame.K_RIGHT] and kosar_x < SZEL - kosar_szelesseg:
        kosar_x += kosar_sebesseg

    # 3. Játék logika frissítése
    targy_y += targy_sebesseg

    # Ha a tárgy leesett alulra, dobjuk vissza a tetejére egy új X pozícióba
    if targy_y > MAG:
        targy_y = 0
        targy_x = random.randint(0, SZEL - targy_meret)
        pontszam -= 1  # Büntetés, ha leesett

    # Ütközésvizsgálat (Elkapta-e a kosár?)
    kosar_rekesz = pygame.Rect(kosar_x, kosar_y, kosar_szelesseg, kosar_magassag)
    targy_rekesz = pygame.Rect(targy_x, targy_y, targy_meret, targy_meret)

    if kosar_rekesz.colliderect(targy_rekesz):
        pontszam += 1
        targy_y = 0
        targy_x = random.randint(0, SZEL - targy_meret)
        targy_sebesseg += 0.2  # Egyre nehezedik!

    # 4. Képernyő újrarajzolása (Minden körben kitakarítunk és rajzolunk)
    ablak.fill(FEKETE)  # Háttér színre festése

    # Kosár kirajzolása (Kék téglalap)
    pygame.draw.rect(
        ablak,
KEX, (kosar_x, kosar_y, kosar_szelesseg, kosar_magassag)
    )

    # Potyogó tárgy kirajzolása (Piros kocka)
    pygame.draw.rect(ablak, PIROS, (targy_x, targy_y, targy_meret, targy_meret))

    # Pontszám kiírása a képernyőre
    szoveg_kep = betutipus.render(f"Pontszám: {pontszam}", True, ZOLD)
    ablak.blit(szoveg_kep, (20, 20))

    # Kép frissítése a monitoron
    pygame.display.flip()

    # FPS korlátozás (60 képkocka másodpercenként)
    ora.tick(120)

pygame.quit()