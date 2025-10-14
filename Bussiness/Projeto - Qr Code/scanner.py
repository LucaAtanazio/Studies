import cv2
from pyzbar.pyzbar import decode
import time
import numpy as np # Importar numpy é uma boa prática com cv2

# --- Inicialização da Câmera ---
# 0 geralmente é a câmera padrão (webcam). Se não funcionar, tente 1 ou -1.
cam = cv2.VideoCapture(0)

# Configurando a resolução. As resoluções 5 e 6 são aliases para CV_CAP_PROP_FRAME_WIDTH e HEIGHT.
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Flag para controlar o loop da câmera
camera_aberta = True

print("Aguardando a detecção de um QR Code...")

# --- Loop Principal de Captura ---
while camera_aberta:
    # 1. Leitura do Frame
    success, frame = cam.read()
    
    # Verifica se a leitura foi bem-sucedida (frame não está vazio)
    if not success:
        print("Erro ao capturar o frame da câmera. Verifique se a câmera está em uso por outro programa.")
        break
    
    # 2. Decodificação do QR Code
    decoded_objects = decode(frame)

    if decoded_objects:
        for obj in decoded_objects:
            # Dados do QR Code
            tipo = obj.type
            dados = obj.data.decode('utf-8')
            
            # Desenhar um retângulo ao redor do QR Code
            (x, y, w, h) = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) # Verde para detecção

            # Adicionar texto para feedback visual
            cv2.putText(frame, f"Tipo: {tipo}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.putText(frame, "LIDO! PAUSADO POR 5s", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            # Imprimir a chave no console (simulando a extração para o arquivo CSV)
            print("-" * 50)
            print(f"Tipo: {tipo}")
            print(f"Dados (Link Completo): {dados}")
            
            # *** Aqui você integraria a função 'extrair_chave_do_link' e 'verificar_e_salvar_chave' da aula anterior! ***
            
            # Pausa a captura para que a pessoa possa retirar o cupom ou visualizar
            # NOTE: O time.sleep deve ser curto para não travar a GUI do OpenCV
            time.sleep(10) 
            
            # Após a pausa, limpa o console para facilitar a visualização
            print("-" * 50)
            print("Câmera retomada. Aguardando próximo QR Code...")

    # 3. Exibição do Frame
    # O comando cv2.imshow() é o que abre a janela
    cv2.imshow("Leitor de QR Code Fiscal", frame)
    
    # 4. Controle de Loop (A Chave do OpenCV!)
    # cv2.waitKey(1) espera 1 milissegundo por uma tecla.
    # Se a tecla 'q' for pressionada (ord('q') = código ASCII de 'q'), o loop é encerrado.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera_aberta = False
        
# --- Limpeza ---
cam.release() # Libera o hardware da câmera
cv2.destroyAllWindows() # Fecha todas as janelas do OpenCV

print("Leitor de QR Code encerrado.")