import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0) # Definindo a webcam como entrada de vídeo


hand = mp.solutions.hands # Atribui a solução de mãos do mediapipe à variável hand
Hand = hand.Hands(1) # Definindo o número máximo de mão por vez como 1 
mpDraw = mp.solutions.drawing_utils # Atribui a solução de desenho do mediapipe à variável mpDraw


# Loop que separa a entrada da webcam em frames
while True:
    check, frame = webcam.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Converte a ordem das cores da imagem de BGR para RGB
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    height, width, _ = frame.shape # Salva as coordenadas x e y da câmera nas variáveis width e height
    pontos = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(frame,points,hand.HAND_CONNECTIONS) # Desenha na câmera os pontos da mão e suas conexões
            for id,cord in enumerate(points.landmark):
                cx,cy = int(cord.x * width) , int(cord.y * height)
                pontos.append((cx,cy)) # Adiciona as coordenadas de cada ponto da mão na lista pontos
        
        contador = 0
        if points:
            
            # Verifica se o dedo mindinho está levantado e atribui a ele o valor de 16
            if pontos[20][1] < pontos[18][1]:
                contador += 2**4
            
            # Verifica se o dedo anelar está levantado e atribui a ele o valor de 8
            if pontos[16][1] < pontos[14][1]:
                contador += 2**3
            
            # Verifica se o dedo médio está levantado e atribui a ele o valor de 4    
            if pontos[12][1] < pontos[10][1]:
                contador += 2**2
            
            # Verifica se o dedo indicador está levantado e atribui a ele o valor de 2
            if pontos[8][1] < pontos[6][1]:
                contador += 2**1
            
            # Verifica se o polegar está levantado e atribui a ele o valor de 1
            if pontos[4][0] < pontos[2][0]:
                contador += 2**0
                    
        cv2.putText(frame, str(contador), (10,95), cv2.FONT_HERSHEY_COMPLEX, 4, (255,0,0), 5)
    
    cv2.imshow("Webcam", frame) # Cria uma janela nova com o nome Webcam a partir do frame gerado
    cv2.waitKey(1)
