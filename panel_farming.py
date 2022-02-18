import keyboard
import time
import serial

print("ouverture du port serie", end = "...")
arduino = serial.Serial(port = "COM7", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
print("OK")
 
print("test de comunication avec l'arduino va debuter, VEUILIER PAS TOUCHER AU BOUTON!!")
time.sleep(5)
for loop in range(10):
    print("test de comunication avec l'arduino(", end = "")
    print(loop+1, end = "")
    print(")", end = "...")
    
    arduino.write(b"ping")
    time.sleep(0.5)
    if(arduino.readline() == b'pong\r\n'): #on envoie "ping" est on verifie que on reçoit "pong"
        print("OK")
    else:
        print("ERREUR")
        exit("l'arduino de repond pas aux commands!")
print("PRET")


while(True): #boucle principale
    if(arduino.in_waiting > 0): #on attend un message entrant sur le port serie.
        incomingData = arduino.readline() #on lis des message entrant du port serie
        print("donnée reçu : ", end = "")
        print(incomingData)
        if(incomingData == b'Return\r\n'): #Return
            print("touche : *")
            keyboard.press_and_release('*') #on simule une pression de touche
        if(incomingData == b'Drive\r\n'): #Drive
            print("touche : $")
            keyboard.press_and_release('$')
        if(incomingData == b'speedmore\r\n'): #speed+
            print("touche : +")
            keyboard.press_and_release('+')
        if(incomingData == b'speedless\r\n'): #speed-
            print("touche : -")
            keyboard.press_and_release('-')


