import csv  # import CSV library
import pyfirmata  # import pyfirmata library
import time as wait  # import time library
import os # import os

board = pyfirmata.Arduino("/dev/ttyACM0")
it = pyfirmata.util.Iterator(board)
it.start()  # start iterator
PIR_pin = board.get_pin("d:13:i")  # connect PIR sensor to pin 13 as input
LED_pin = board.get_pin("d:2:o") # connect LED to pin 2 as output
#Capturing section
i=0
while i<5:
    PIR_Data = PIR_pin.read()
    if PIR_Data is True:
        print("Capturing image")
        LED_pin.write(1)
        i += 1
        os.system("fswebcam -r 320x240 --no-banner /home/pi/Desktop/Auto/image/hinh"+str(i)+".jpg")
        print ("Image captured")
        LED_pin.write(0)
        wait.sleep(5)
board.exit()
#OPEN HTML FILE TO SEE RESULT
wait.sleep(1)
os.system("python3 open-html.py")
#SYNC ALL THE CAPTURED IMAGED TO GOOGLE DRIVE
wait.sleep(1)
os.system("rclone sync /home/pi/Desktop/Auto/image Drive:images")
#OPEN COLAB PAGE TO USE PRE-TRAINED MODEL
wait.sleep(10)
os.system("chromium-browser "https://colab.research.google.com/drive/1Awyi2WmWnuOnVCPq5_PgF1sSbQr8HgNt")









 



