import pygame as pg
import random as rd
# gera numeros aleatórios
pg.init()

x = 1280
y = 720

screen = pg.display.set_mode((x,y))
pg.display.set_caption("Meu novo jogo em python")

# carregar a imagem para ficar no fundo(converter para alpha para pode alterar o tamanho)
bg = pg.image.load("imagens/cenario.jpeg").convert_alpha()

# mudar  background para codernada x, y (tamanho da imagem)
bg = pg.transform.scale(bg, (x, y))


alien = pg.image.load("imagens/Alien.png").convert_alpha()
alien = pg.transform.scale(alien,(100,100))

nave = pg.image.load("imagens/nave.png").convert_alpha()
nave = pg.transform.scale(nave, (100,100))

missel = pg.image.load("imagens/OIP.jpeg").convert_alpha()
missel = pg.transform.scale(missel, (25,25))
# missel = pg.transform.rotate(missel, -45) >>>>> muda o angulo da imagem 




posicao_alien_x = 500
posicao_alien_y = 360

posicao_nave_x = 200
posicao_nave_y = 300

vel_x_missel = 0
posicao_missel_x = 220
posicao_missel_y = 320


pontos = 10 

acionado = False

rodando = True 

font = pg.font.SysFont(None, 50)

# tranformando as imagens em objetos, para pode fazer a interção entre as imagens
nave_objeto = nave.get_rect()
alien_objeto = alien.get_rect()
missel_objeto = missel.get_rect()

# ------------------funções--------------------------------

# função pro alien voltar, porque se não ele some kkkkk
def volta_alien():
    # o alien voltara na posicção do eixo x = 1350
    x = 1350
    # rd.randint(1, 640 ) vai gerar um numero aleatório entre 1, 640 e atribuir na variavél y
    y = rd.randint(1, 640 )
    return [x, y]


# função para o missel voltar para o lugar de posição da nave 
def respaunar_missel():
    acionado = False
    respaunar_missel_x = posicao_nave_x
    respaunar_missel_y = posicao_nave_y 
    vel_x_missel = 0
    return [respaunar_missel_x, respaunar_missel_y, acionado, vel_x_missel]

def colisoes():
    global pontos
    if nave_objeto.colliderect(alien_objeto) or alien_objeto.x == 60:
        pontos -=1
        return True
    elif missel_objeto.colliderect(alien_objeto):
        pontos += 1
        return True
    else:
        return False
    



while rodando:
    # evento para verificar quais teclas estou apertando
    for event in pg.event.get():

        # se a tecla for o x da janela o rodando vai ser falso, loop vai quebra e o jogo vai fechar
        if event.type == pg.QUIT:
            rodando = False

   # criar um fundo com inicio na posição 0, 0
    screen.blit(bg, (0,0))

    # mopstando o carosel
    # bg.get_rect().width >>>> vai descobri o tamanho da largura da tela de fundo
    relativo_x = x % bg.get_rect().width  # ralitovo_x é o reto da divisão do x pela largura do bg
   # (relativo_x - bg.get_rect().width, 0): É a posição onde você quer colocar a imagem na tela.
   #  o sinal de menos é basicamente pra mover  tela para esquedar
    screen.blit(bg, (relativo_x - bg.get_rect().width, 0))

    # criara outra imagem e atualizara (vindo junto para a esquerda com a primeira imagem )
    if relativo_x < 1280:
        screen.blit(bg, (relativo_x, 0))


    #--------------------------TECLAS DE COMANDO------------------------
    

    tecla = pg.key.get_pressed()

    # se a tecla pra cima for apertada e posicao da nave for maior que um 1 ela vai subir  
    if tecla[pg.K_UP] and posicao_nave_y > 1:
        posicao_nave_y -= 1
        
        if not acionado:  
            posicao_missel_y -=1

     # se a tecla pra baixo for apertada e posicao da nave for menor que 665  a nave vai descer
    if tecla[pg.K_DOWN] and posicao_nave_y < 665:
       posicao_nave_y += 1
       
       if not acionado:
           posicao_missel_y +=1

    if tecla[pg.K_SPACE]:
        acionado = True
        vel_x_missel = 5
    
    if pontos <= -1:
        rodando = False

     # se  o alien estiver na  posição 50 é a borda da tela 
    if posicao_alien_x == 50:
        
        posicao_alien_x = volta_alien()[0]
        posicao_alien_y = volta_alien()[1]
    
    if posicao_missel_x == 1300:
        posicao_missel_x, posicao_missel_y, acionado, vel_x_missel = respaunar_missel()

    if posicao_alien_x == 50 or colisoes():
        posicao_alien_x = volta_alien()[0]
        posicao_alien_y = volta_alien()[1]
        
    #   posicção dos rect 
    nave_objeto.x = posicao_nave_x
    nave_objeto.y = posicao_nave_y

    missel_objeto.x = posicao_missel_x
    missel_objeto.y = posicao_missel_y

    alien_objeto.x = posicao_alien_x
    alien_objeto.y = posicao_alien_y
   
    

    

   # -------------------------FIM DAS TECLAS DE COMANDO------------------------------------------------   

# ================== MOVIMENTOS =====================

  #altera o valor de x, além de ajudar ordernar a velocidade do carrasoel
    x-=0.70
# para o alien se movimentar para a esquerda 
    posicao_alien_x-= 1
    posicao_missel_x += vel_x_missel

#  funcionam como bordas para verificar se as imagensa viraram ojetos
    # pg.draw.rect(screen, (255, 0 ,0 ), nave_objeto, 4)
    # pg.draw.rect(screen, (255, 0 ,0 ), missel_objeto, 4)
    # pg.draw.rect(screen, (255, 0 ,0 ), alien_objeto, 4)

    score = font.render(f"pontos: {int(pontos)}", True, (0,0,0))
    screen.blit(score, (50,50))


# ======================= FIM DOS MOVIEMNETOS =======
    # criei as imagens dos alines e nave dentro da janela 
    screen.blit(alien, (posicao_alien_x, posicao_alien_y))
    screen.blit(missel, (posicao_missel_x, posicao_missel_y))
    screen.blit(nave, (posicao_nave_x, posicao_nave_y))
  
 

    print(pontos)
    # para ficar atualizando a tela 
    pg.display.update() 