import cv2 as cv

url = 'http://192.168.18.8:4747/video'  # URL de la cámara IP
print(f"Intentando acceder a la cámara en: {url}")
captureVideo = cv.VideoCapture(url) # Esto es para cámaras IP

if not captureVideo.isOpened():
    print("No se encontró ninguna cámara")
    exit()
while True:
    typeCamara, frame = captureVideo.read() # Lee el frame de la cámara
    cv.imshow('Live', frame)

    if cv.waitKey(2) == ord('q'):
        break
captureVideo.release()
cv.destroyAllWindows()