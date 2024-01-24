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
import sys

# Aqui faço a inicialização da biblioteca Pygame
pygame.init()
pygame.mixer.init()

# Determinei 800x600 mas vc pode aplicar a resolução que achar melhor (porém, vou fazer uma atividade em sala de upgrade)
largura_tela = 800
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('IFMA Velozes e Estudiosos')
obstaculos_ultrapassados = 0
#Pontuação
nivel = 1
pontos = 0

#carregar sons
file_songs = 'songs/sonoro.wav'
file_batida = 'songs/acidente.mp3'
pygame.mixer.music.load(file_songs)
# pygame.mixer.music.play(-1)
efeito_colisao = pygame.mixer.Sound(file_batida)

 
#Colocando a imagem de fundo
imagem = pygame.image.load('img/asfalto.jpg')
imagem = pygame.transform.scale(imagem,(largura_tela,altura_tela))

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)

#Criando a janela de mensagem
fonte = pygame.font.SysFont('Comic Sans MS', 35)

# Aqui coloquei separado para ajustar as configurações do carro
carro_largura = 50
# pygame.mixer_music.load('songs/corrida.mp3')
# pygame.mixer_music.play(-1)
carro = pygame.image.load('img/carro.png')  
carro = pygame.transform.scale(carro, (carro_largura, 100))

# Posição inicial do carro
x = (largura_tela * 0.45)
y = (altura_tela * 0.8)

# Configurações dos obstáculos
obstaculo_largura = 50
obstaculo_altura = 100
obstaculo_cor = (255, 0, 255)  # Veja que é usado o padrão RGB, não preciso entrar em detalhes, certo?
obstaculo_velocidade = 7 # Falarei disso na sala (Será também uma implementação como Atividade)
obstaculo_x = random.randrange(0, largura_tela)
obstaculo_xx = random.randrange(0, largura_tela)
obstaculo_y = -600

# Desenhando os obstáculos [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def desenha_obstaculo(x, y, largura, altura, cor):
    pygame.draw.rect(tela, cor, [x, y, largura, altura])

#alternativa para colocar um carro como obstaculo
def carro_obstaculo(x, y, largura,):
    carro_vermelho = pygame.image.load('img/carroilustrativo1.png')
    carro_vermelho = pygame.transform.scale(carro_vermelho, (largura, 100))
    tela.blit(carro_vermelho, (x, y))
    
#alternativa para colocar gerar mais de um carro como obstaculo
def gerador_de_obstaculo_carro(x1, x2, y, largura,):
    carro_amarelo = pygame.image.load('img/carroilustrativo2.png')
    carro_vermelho = pygame.image.load('img/carroilustrativo1.png')
    carro_amarelo = pygame.transform.scale(carro_amarelo, (largura, 100))
    carro_vermelho = pygame.transform.scale(carro_vermelho, (largura, 100))
    tela.blit(carro_amarelo, (x1, y))
    tela.blit(carro_vermelho, (x2, y))
    
def colisao(carro_x, carro_y, carro_largura, carro_altura, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura):
    return (
        carro_x < obstaculo_x + obstaculo_largura and
        carro_x + carro_largura > obstaculo_x and
        carro_y < obstaculo_y + obstaculo_altura and
        carro_y + carro_altura > obstaculo_y
    )

def janela(mensagem, duracao):
    texto = fonte.render(mensagem, True, (255,255,0))
    tela.blit(texto, (largura_tela//2 - texto.get_width()//2, altura_tela//2 - texto.get_height()//2))
    pygame.display.update()
    tempo = pygame.time.get_ticks()

    while pygame.time.get_ticks() - tempo < duracao:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    tela.blit(imagem,(0,0))


# Redesenhando a tela [leiam a documentação para implementar aqui fiz apenas alguns esboços]
def redesenhar_tela():
    tela.blit(imagem,(0,0))
    tela.blit(carro, (x,y))
    gerador_de_obstaculo_carro(obstaculo_x, obstaculo_xx , obstaculo_y, 50)
    gerador_de_obstaculo_carro(obstaculo_x, obstaculo_xx , obstaculo_y, 50)
    # desenha_obstaculo(obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura, obstaculo_cor)
    # carro_obstaculo(obstaculo_x, obstaculo_y, 50)
    print('X: ' + str(x) + ' Y: ' + str(y))
    print('ObsX: ' + str(obstaculo_x) + ' ObsY: ' + str(obstaculo_y))
    fonte_pontos = pygame.font.SysFont('Comic Sans MS', 40)
    texto_pontos = fonte_pontos.render('Pontuação: '+ str(pontos), True, (255,255,0))
    print(pontos)
    tela.blit(texto_pontos, (10, 10))
    pygame.display.update()
    
# Parte principal do jogo (aqui executo a criação do loop)
jogo_ativo = True
clock = pygame.time.Clock()

pausado = False
jogo_pausado = "VOCÊ PERDEU!\n Pressione 'R' para reiniciar ou 'Q' para sair"

while jogo_ativo:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

    keys = pygame.key.get_pressed()
    
    if not pausado:

        if keys[pygame.K_LEFT]:
            if x == 0:
                x -= 0
            else:
                x -= 5
            
        if keys[pygame.K_RIGHT]:
            if x == (largura_tela - carro_largura):
                x -= 0
            else:
                x += 5
                
        if keys[pygame.K_UP]:#certo
            if y == 0:
                y
            else:
                y -= 5
                
        if keys[pygame.K_DOWN]:#condição de se y é igual a altura máxima da tela menos o tamanho do carro pra não travar metade do carro dentro e outra pra fora da tela
            if y == (altura_tela - carro_largura) :
                y
            else:
                y += 5

        obstaculo_y += obstaculo_velocidade
        if obstaculo_y > altura_tela:
            obstaculo_y = 0 - obstaculo_altura
            obstaculo_x = random.randrange(0, largura_tela)
            obstaculo_xx = random.randrange(0, largura_tela)
            obstaculos_ultrapassados += 1
            pontos += 100
            if obstaculo_velocidade < 10:
                if obstaculos_ultrapassados >= 10:
                    nivel += 1
                    obstaculo_velocidade += 1
                    if obstaculos_ultrapassados == 10:
                        janela('Nível: {} Aumentando a velocidade'.format(nivel), 2000)                    
                        obstaculos_ultrapassados = 0
        
        if colisao(x, y, carro_largura, 100, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura):
            # print("Colisão com obstáculo 1!")
            efeito_colisao.play()
            pausado = True

        if colisao(x, y, carro_largura, 100, obstaculo_xx, obstaculo_y, obstaculo_largura, obstaculo_altura):
            # print("Colisão com obstáculo 2!")
            efeito_colisao.play()
            pausado = True

    else:
        janela(jogo_pausado, 200)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            pausado = False
            # Reiniciar as variáveis do jogo
            pontos = 0
            nivel = 1
            obstaculo_velocidade = 7
            obstaculos_ultrapassados = 0
            obstaculo_x = random.randrange(0, largura_tela)
            obstaculo_xx = random.randrange(0, largura_tela)
            obstaculo_y = -600
            x = largura_tela * 0.45
            y = altura_tela * 0.8
            
        elif keys[pygame.K_q]:
            jogo_ativo = False

    redesenhar_tela()
    clock.tick(60)
pygame.quit()
