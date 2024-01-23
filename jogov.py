##### IFMA Velozes e Estudiosos #####
#Gênero: Corrida
#Subgênero: Corrida de esquiva ou obstáculos (Como queiram chamar!!)
#Faixa etaária: Livre
#Versão 0.1.0
#Direitos autorais: Jaelma Barbosa, Antonio Alécio, Kayo Vinícius, Narayane Chaves

#### Impletações - Parte 1 #### 
#1 - Nao permitir sair da Tela (Area Visivel);
#2 - Colisão com os obstáculos;
#3 - Implementar background (Deixo para alterações);

#Bonus# : Caso adicione 1(uma) funcionalidade fora da lista solicitada, que possua interatividade e dentro
# do escopo já estudado.  [ 1,5 pts ] 
import pygame
import random

#Colocando a imagem de fundo
imagem = pygame.image.load('C:/Users/narin/OneDrive/Documentos/Programas/jogo/Projeto-Jogo-de-Corrida-com-Python-main/img/tapete')
imagem = pygame.transform.scale(imagem,(800,700))

# Aqui faço a inicialização da biblioteca Pygame
pygame.init()

# Determinei 800x600 mas vc pode aplicar a resolução que achar melhor (porém, vou fazer uma atividade em sala de upgrade)
largura_tela = 800
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('IFMA Velozes e Estudiosos')

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Aqui coloquei separado para ajustar as configurações do carro
carro_largura = 150
# pygame.mixer_music.load('songs/corrida.mp3')
# pygame.mixer_music.play(-1)
carro = pygame.image.load('C:/Users/narin/OneDrive/Documentos/Programas/jogo/Projeto-Jogo-de-Corrida-com-Python-main/img/carro.png')  
carro = pygame.transform.scale(carro, (carro_largura, 220))

# Posição inicial do carro
x = (330)
y = (altura_tela * 0.65)

# Configurações dos obstáculos
obstaculo_largura = 50
obstaculo_altura = 100
obstaculo_cor = (255, 0, 255)  # Veja que é usado o padrão RGB, não preciso entrar em detalhes, certo?
obstaculo_velocidade = 7 # Falarei disso na sala (Será também uma implementação como Atividade)
obstaculo_x = random.randrange(0, largura_tela)
obstaculo_y = -600

# Desenhando os obstáculos [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def desenha_obstaculo(x, y, largura, altura, cor):
    # pygame.image.load('img/carroilustrativo2.png')
    pygame.draw.rect(tela, cor, [x, y, largura, altura])

# Redesenhando a tela [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def redesenhar_tela():
    tela.blit(imagem,(0,0))
    tela.blit(carro, (x,y))
    print('X: ' + str(x) + ' Y: ' + str(y))
    print('ObsX: ' + str(obstaculo_x) + ' ObsY: ' + str(obstaculo_y))
    desenha_obstaculo(obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura, obstaculo_cor)
    pygame.display.update()

# Parte principal do jogo (aqui executo a criação do loop)
jogo_ativo = True
clock = pygame.time.Clock()

while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x==(largura_tela -largura_tela):
            x-=0
        else:
            x -= 5
        
    if keys[pygame.K_RIGHT]:
        if x>=(largura_tela-150):
            x-=0
        else:
            x += 5
            
    if keys[pygame.K_UP]:#certo
        if y == (altura_tela - altura_tela):
            y
        else:
            y -= 5
            
    if keys[pygame.K_DOWN]:#certo
        if y == (altura_tela - 100) :
            y
        else:
            y += 5

    obstaculo_y += obstaculo_velocidade
    if obstaculo_y > altura_tela:
        obstaculo_y = 0 - obstaculo_altura
        obstaculo_x = random.randrange(0, largura_tela)
    
    if (
    x < obstaculo_x + obstaculo_largura and
    x + obstaculo_altura > obstaculo_x and
    y < obstaculo_y + obstaculo_altura and
    y + carro_largura > obstaculo_y
    ):
        jogo_ativo = False
        
    redesenhar_tela()
    clock.tick(60)

pygame.quit()
