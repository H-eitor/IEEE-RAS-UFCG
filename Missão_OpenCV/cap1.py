# Heitor de Souza Alves 

# Importação da biblioteca
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('Capturas de tela\Captura de tela 2024-03-12 204909.png')

# Imprime a largura da imagem
print('Largura em pixels: ', end='')
print(imagem.shape[1])

# Imprime a altura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0])

# Imprime a quantidade de canais da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

# Mostra a imagem com a função imshow em uma nova janela
cv2.imshow("Nome da janela", imagem)

# Fecha a janela aberta ao pressionar qualquer tecla
cv2.waitKey(0)

# Salva a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)
