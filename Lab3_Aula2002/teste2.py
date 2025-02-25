import cv2

# # Iniciando a captura de vídeo
# cap = cv2.VideoCapture(0) #webcam
# cap2 = cv2.VideoCapture("Lab3_Aula2002/totoro.mp4") #video que foi salvo

# while True:
#     # Tenta fazer a Captura do frame
#     ret, frame = cap.read()
#     ret, frame2 = cap2.read()

#     # verifica se o frame foi capturado corretamente
#     if not ret:
#         print("Erro: Não foi possível capturar o frame.")
#         break
    
#     # processa o frame capturado
#     normalFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
#     # Exibe o frame processado
#     cv2.imshow('camera', frame)
#     cv2.imshow('camera_processado', normalFrame)
#     cv2.imshow('frame', frame2)
#     cv2.imshow('frame_processado', gray)

#     # Aguarda 1 ms e verifica se a tecla 'q' foi pressionada para sair
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Libera a captura e fecha todas as janelas
# cap.release()
# cv2.destroyAllWindows()

import matplotlib.pyplot as plt

video_path = "Lab3_Aula2002/video.mp4"
video = cv2.VideoCapture(video_path)

fig, ax = plt.subplots()

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converte para RGB
    ax.clear()
    ax.imshow(frame)
    plt.pause(0.03)  # Pequena pausa para atualização

video.release()
plt.close()
