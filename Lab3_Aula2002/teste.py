import cv2

#Quando trabalhamos com videos n usamos mtplot

# Iniciando a captura de vídeo
cap = cv2.VideoCapture(0) #(0) é o drive de video, aloca com a webcam do pc

while True: #um laço infinito para a captura de frames
    # Tenta fazer a Captura do frame
    ret, frame = cap.read() #read faz a captura do frame e retorna dois parâmetros. o retorno do read eu quebro em duas variáveis
    #o primeiro agurmento = boolean, volta true quando consegue capturar o frame
    # verifica se o frame foi capturado corretamente
    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break
    
    # processa o frame capturado
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converte brg pro cinza
    
    # Exibe o frame processado
    cv2.imshow('frame', gray) #exibe a imagem
    
    # Aguarda 1 ms e verifica se a tecla 'q' foi pressionada para sair, quando aperta q o código da um break e sai do while
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha todas as janelas
cap.release() #release fala pro SO que a câmera que estava em funcionamento agr está ocioso (ou seja, se algum outro app quiser usar a webcam pode que agr ta liberado. Se n der o release msm q feche a camera continua consumindo memoria)
cv2.destroyAllWindows()