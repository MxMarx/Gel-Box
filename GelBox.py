from time import sleep
import os
from fractions import Fraction
import RPi.GPIO as GPIO
import datetime
import ftplib
from subprocess import call

GPIO.setmode(GPIO.BCM)  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
sleep(1)




while 1:
    print("Ready")
    GPIO.output(21,GPIO.HIGH)
    GPIO.wait_for_edge(24,GPIO.RISING,bouncetime=500)
    GPIO.output(21,GPIO.LOW)

    print("Starting")

    fname = '{0:%Y-%m-%d_%H-%M}'.format(datetime.datetime.now())
    outname = ("/home/pi/" + fname + ".jpg")
    print("Running")
    
    try:
        cc = "raspistill -w 3280 -h 2464 -ISO 50 -ss 2000000 -ex off -awb off -awbg 1.41,2.03 -o "
    
        GPIO.output(17,GPIO.HIGH)
        os.system(cc + outname)
        GPIO.output(17,GPIO.LOW)
    except:
        for i in range(0,2):
            GPIO.output(17,GPIO.HIGH)
            sleep(0.2)
            GPIO.output(17,GPIO.LOW)
            sleep(0.2)
        sleep(1)
    try:
        print("Saving")
        session = ftplib.FTP('10.146.126.237','LabPeople','5htrules')
        file = open('/home/pi/' + fname + '.jpg','rb')                  # file to send
        session.storbinary('STOR LabPeople/Russell/Gels/Images/' + fname + '.jpg', file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
    except:
        for i in range(0,2):
            GPIO.output(21,GPIO.HIGH)
            sleep(0.2)
            GPIO.output(21,GPIO.LOW)
            sleep(0.2)
        sleep(1)
        
    for i in range(0,2):
        GPIO.output(21,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(21,GPIO.LOW)
        sleep(0.2)
        print("i")
    call("sudo shutdown -h now", shell=True)


