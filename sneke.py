import pygame as pg
from pygame.locals import *
from random import randint as Ri


# constantes
pixel = 20
tela = (30*pixel, 30*pixel)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
pontos = 0
pg.font.init()
fonte = pg.font.SysFont('arial', 30)
larg = 10*pixel
geracao = 0

# I.A
ia_jogando = True


# colisão
def colisao(pos1, pos2):
    return pos1 == pos2


def parede(pos):
    if 0 <= pos[0] < tela[0] and 0 <= pos[1] < tela[1]:
        return False
    else:
        return True


# randomização da maçã

def ramdom_apple():
    x = Ri(0, tela[0])
    y = Ri(0, tela[1])
    return x // pixel * pixel, y // pixel * pixel


pg.init()

screen = pg.display.set_mode(tela)
pg.display.set_caption('snake')

# snake
sp = [(10 * pixel, 10*10), (11*pixel, 10*pixel), (12*pixel, 10*pixel)]
ss = pg.Surface((pixel, pixel))
ss.fill(branco)
sd = K_LEFT

# apple
apple_surface = pg.Surface((pixel, pixel))
apple_surface.fill(vermelho)
ap = ramdom_apple()


# reiniciar

def reiniciar():
    global sp
    global ap
    global sd

    sp = [(10 * pixel, 10*10), (11*pixel, 10*pixel), (12*pixel, 10*pixel)]

    sd = K_LEFT
    ap = ramdom_apple()



while True:
    pg.time.Clock().tick(10)
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d]:
                sd = event.key
    screen.blit(apple_surface, ap)

    if colisao(ap, sp[0]):
        sp.append((-10, -10))
        ap = ramdom_apple()
        pontos += 1

    for pos in sp:
        screen.blit(ss, pos)

    for i in range(len(sp) - 1, 0, -1):
        if colisao(sp[0], sp[i]):
            reiniciar()
            pontos = 0
        sp[i] = sp[i - 1]
    if parede(sp[0]):
        reiniciar()
        pontos = 0
    texto = fonte.render(f'Pontuação: {pontos}', 1, branco)
    screen.blit(texto, (larg - 10 - texto.get_width(), 10))

    # controles

    if sd == K_UP or sd == K_w:

        sp[0] = (sp[0][0], sp[0][1] - pixel)
    elif sd == K_DOWN or sd == K_s:
        sp[0] = (sp[0][0], sp[0][1] + pixel)
    elif sd == K_LEFT or sd == K_a:
        sp[0] = (sp[0][0] - pixel, sp[0][1])
    elif sd == K_RIGHT or sd == K_d:
        sp[0] = (sp[0][0] + pixel, sp[0][1])

    pg.display.flip()
