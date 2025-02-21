import cv2

# Iniciando a captura de vídeo
#cap = cv2.VideoCapture(0) #webcam
cap = cv2.VideoCapture("totoro.mp4") #video que foi salvo

while True:
    # Tenta fazer a Captura do frame
    ret, frame = cap.read()

    # verifica se o frame foi capturado corretamente
    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break
    
    # processa o frame capturado
    # normalFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Exibe o frame processado
    # cv2.imshow('frame', normalFrame)
    cv2.imshow('frame', frame)
    cv2.imshow('frame_processado', gray)

    # Aguarda 1 ms e verifica se a tecla 'q' foi pressionada para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()