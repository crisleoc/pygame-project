import pygame
import random
import time

puntos = 0


def main():
    def pescar(x, y):
        t = random.choice([3, 4, 5])
        tiempo_pesc = time.time()+t
        while time.time() < tiempo_pesc:
            ventana.blit(imagen_pescando, (220, 270))
            ventana.blit(barco_imagen, (x, y))
            pygame.display.update()
        boton()

    def punto(letra):
        tiemp = time.time()+3
        global puntos
        for event in pygame.event.get():
            if letra == ("a"):
                puntos += 1
                while time.time() < tiemp:
                    ventana.blit(img_a, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_a:
                            puntos = puntos+1
                    pygame.display.update()
            if letra == ("s"):
                puntos += 1
                ventana.blit(img_s, (270, 300))
                while time.time() < tiemp:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.type == pygame.K_s:
                                puntos = puntos+1
                    pygame.display.update()
            if letra == ("d"):
                puntos += 1
                while time.time() < tiemp:
                    ventana.blit(img_d, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        puntos = puntos+1
                    pygame.display.update()
            if letra == ("f"):
                puntos += 1
                while time.time() < tiemp:
                    ventana.blit(img_f, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_f:
                            puntos = puntos+1
                    pygame.display.update()
            if letra == ("g"):
                puntos += 1
                while time.time() < tiemp:
                    ventana.blit(img_g, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_g:
                            puntos = puntos+1
                    pygame.display.update()
            if letra == ("h"):
                puntos += 1
                while time.time() < tiemp:
                    ventana.blit(img_h, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_h:
                            puntos = puntos+1
                    pygame.display.update()
            if letra == ("j"):
                puntos += 1
                while time.time() < tiemp:
                    ventana.blit(img_j, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_j:
                            puntos = puntos+1
                    pygame.display.update()
            if letra == ("k"):
                puntos += 1
                while time.time() < tiemp:
                    ventana.blit(img_k, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_k:
                            puntos = puntos+1
                    pygame.display.update()
            if letra == ("l"):
                while time.time() < tiemp:
                    ventana.blit(img_l, (270, 300))
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.K_l:
                            puntos = puntos+1
                    pygame.display.update()
        pygame.display.update()

    def boton():
        segundos = random.choice([2, 3, 4, ])
        cosa = time.time()+segundos
        letra = random.choice(["a", "s", "d", "f", "g", "h", "j", "k", "l"])
        while time.time() < cosa:
            if letra == "a":
                punto(letra)
                pygame.display.update()
            if letra == "s":
                punto(letra)
                pygame.display.update()
            if letra == "d":
                punto(letra)
                pygame.display.update()
            if letra == "f":
                punto(letra)
                pygame.display.update()
            if letra == "g":
                punto(letra)
                pygame.display.update()
            if letra == "h":
                punto(letra)
                pygame.display.update()
            if letra == "j":
                punto(letra)
                pygame.display.update()
            if letra == "k":
                punto(letra)
                pygame.display.update()
            if letra == "l":
                punto(letra)
                pygame.display.update()

    def barco(x, y):
        if barcox <= 0:
            x = 0
        elif barcox >= 576:
            x = 576
        if barcoy <= 0:
            y = 0
        elif barcoy >= 576:
            y = 576
        ventana.blit(barco_imagen, (x, y))
        pygame.display.update()

    def pantalla_final():
        global puntos
        pantallaf = pygame.display.set_mode((400, 100))
        pantallaxd = True
        pantallaf.fill((250, 250, 250))
        xd = ("Tu puntaje fue:  ")
        puntos_tex = fuente.render(xd+str(puntos), False, (0, 0, 0))
        pantallaf.blit(puntos_tex, ((50, 20)))
        pygame.display.update()
        while pantallaxd:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pantallaxd = False
        pygame.quit()

    pygame.init()
    pygame.font.init()
    ventana = pygame.display.set_mode((640, 640))
    ventanaExiste = True
    fuente = pygame.font.SysFont('Garamond', 30)
    # puntos = 0
    DIR = "./games/Pescar/images/"

    pygame.display.set_caption("juego del pescao")
    imagen_pescao = pygame.image.load(f'{DIR}pescado.png')
    imagen_pescando = pygame.image.load(f"{DIR}true.pescando.png")
    pygame.display.set_icon(imagen_pescao)

    img_a = pygame.image.load(f'{DIR}a.png')
    img_s = pygame.image.load(f'{DIR}s.png')
    img_d = pygame.image.load(f'{DIR}d.png')
    img_f = pygame.image.load(f'{DIR}f.png')
    img_g = pygame.image.load(f'{DIR}g.png')
    img_h = pygame.image.load(f'{DIR}h.png')
    img_j = pygame.image.load(f'{DIR}j.png')
    img_k = pygame.image.load(f'{DIR}k.png')
    img_l = pygame.image.load(f'{DIR}l.png')

    barco_imagen = pygame.image.load(f"{DIR}barco.png")
    barcox = 0
    barcoy = 0
    if barcox <= 0:
        barcox = 0
    elif barcox >= 576:
        barcox = 576

    # puntos = 0

    while ventanaExiste:
        xd = ("veces que pescaste: ")
        puntos_tex = fuente.render(xd+str(puntos), False, (0, 0, 0))
        ventana.blit(puntos_tex, ((20, 0)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantalla_final()
                ventanaExiste = False
            ventana.fill((0, 128, 128))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and barcox < 575:
                    barcox += 34
                if event.key == pygame.K_a and barcox > 0:
                    barcox -= 34
                if event.key == pygame.K_s and barcoy < 575:
                    barcoy += 34
                if event.key == pygame.K_w and barcoy > 0:
                    barcoy -= 34
                if event.key == pygame.K_SPACE:
                    pescar(barcox, barcoy)
        barco(barcox, barcoy)
        pygame.display.update()
