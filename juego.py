from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Primer juego")

# corregido: scale debe encerrar todo dentro de la función
background = transform.scale(image.load("space_1.jpg"), (700, 500))

# parámetros del objeto (cuadrado)
height = 60
width = 40
x = 5
y = 500 - height - 5
speed = 5

# parámetros del objeto de la imagen
x2 = 100
y2 = 395

# imagen del personaje
img1 = transform.scale(image.load('mokey_018.png'), (100, 100))

# ciclo de juego
run = True
while run:
    time.delay(50)

    # fondo corregido
    window.blit(background, (0, 0))

    # eventos
    for e in event.get():
        if e.type == QUIT:
            run = False
        
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                x -= speed
            elif e.key == K_RIGHT:
                x += speed
            elif e.key == K_UP:
                y -= speed
            elif e.key == K_DOWN:
                y += speed

    # dibujar rectángulo
    draw.rect(window, (0, 0, 255), (x, y, width, height))

    # personaje 2
    window.blit(img1, (x2, y2))

    # movimiento continuo
    keys = key.get_pressed()
    if keys[K_LEFT] and x2 > 5:
        x2 -= speed
    if keys[K_RIGHT] and x2 < 595:
        x2 += speed
    if keys[K_UP] and y2 > 5:
        y2 -= speed
    if keys[K_DOWN] and y2 < 395:
        y2 += speed

    display.update()
