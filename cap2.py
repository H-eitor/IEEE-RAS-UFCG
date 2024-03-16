# Heitor de Souza Alves

# Importação da biblioteca
import cv2

# Modifica a entrada para uma imagem azul de mesma medida
# Mostra a imagem em uma nova janela com o nome "Imagem modificada"
def todo_azul(imagem):
    for y in range(0, imagem.shape[0]):
        for x in range(0, imagem.shape[1]):
            imagem[y, x] = (255,0,0)
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)

# Modifica a entrada para uma imagem que varia de verde para magenta
# A variação é feita através do resto da divisão das posições por 256
# Mostra a imagem em uma nova janela com o nome "Imagem modificada"
def gradiente(imagem):
    for y in range(0, imagem.shape[0]): 
        for x in range(0, imagem.shape[1]): 
            imagem[y, x] = (x%256,y%256,x%256)
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)

# Modifica a entrada para uma imagem verde com padrões em espiral
# Mostra a imagem em uma nova janela com o nome "Imagem modificada"
def visualizador_verde(imagem):
    for y in range(0, imagem.shape[0], 1): 
        for x in range(0, imagem.shape[1], 1): 
            imagem[y, x] = (0,(x*y)%256,0)
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)

# Modifica a entrada adicionando quadrados amarelos medindo 5 pixels cada lado
# Mostra a imagem em uma nova janela com o nome "Imagem modificada"
def pontos_amarelos(imagem):
    for y in range(0, imagem.shape[0], 10): 
        for x in range(0, imagem.shape[1], 10): 
            imagem[y:y+5, x:x+5] = (0,255,255)
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)

# Modifica a entrada adicionando uma linha preta a cada 10 pixels
# Mostra a imagem em uma nova janela com o nome "Imagem modificada"
def linhas_pretas(imagem):
    for y in range(0, imagem.shape[0], 10):
        for x in range(0, imagem.shape[1]):
            imagem[y, x] = (0,0,0)
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)

# Modifica a entrada para uma imagem que varia de ciano para vermelho
# A variação é feita através do resto da divisão das posições por 256
# Mostra a imagem em uma nova janela com o nome "Imagem modificada"
def gradiente2(imagem):
    for y in range(0, imagem.shape[0]):
        for x in range(0, imagem.shape[1]):
            imagem[y, x] = (x%256, x%256, y%256)
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)

# Modifica a entrada para uma imagem que varia de amarelo para azul
# A variação é feita através do resto da divisão das posições por 256
# Mostra a imagem em uma nova janela com o nome "Imagem modificada"
def gradiente3(imagem):
    for y in range(0, imagem.shape[0]):
        for x in range(0, imagem.shape[1]):
            imagem[y, x] = (y%256, x%256, x%256)
    cv2.imshow("Imagem modificada", imagem)
    cv2.waitKey(0)



imagem = cv2.imread('Capturas de tela\Captura de tela 2024-03-12 204909.png')
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

todo_azul(imagem)
linhas_pretas(imagem)
visualizador_verde(imagem)
pontos_amarelos(imagem)
gradiente(imagem)
gradiente2(imagem)
gradiente3(imagem)

