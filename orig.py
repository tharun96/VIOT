#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import call
from datetime import datetime
import httplib, urllib, base64
import json
import time
import RPi.GPIO as GPIO
import cognitive_face as cf
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '8e705a5e508c4d998651bcd28f7b4755',
}
KEY = '8e705a5e508c4d998651bcd28f7b4755'  # Replace with a valid subscription key (keeping the quotes in place).
cf.Key.set(KEY)
x=0
y=0
def ptouch():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        print "ptouch"
        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to search the finger and calculate hash
    try:
        print('Waiting for finger...')

    ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

    ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

    ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]
        print accuracyScore

        if accuracyScore >= 50:
            return 1
        
        else:
            print "else"
            return 0
    except:
        print "hello"
def remo(key):
    xfile = open('/home/pi/x.txt')
    lines=xfile.readlines()
    xfile.close()
    print 'opening f.txt'
    f=open('/home/pi/f.txt',"w")
    for line in lines:
        if line!=key:
            f.write(line)
    f.close()
    print 'after close'
    import shutil
    shutil.move('/home/pi/f.txt', '/home/pi/x.txt')
    print "key", key

    
def touch():
    lines=open('/home/pi/x.txt',"r").readlines()
    def capture():
    
     call(["fswebcam", "-d","/dev/video0", "-r", "640x480", "--no-banner", "-S 10","image10.jpg" ])
    capture()

    #x=lines.pop(0)
    img_url = '/home/pi/Desktop/image10.jpg'
    result=cf.face.detect(img_url)
    x=(result[0]['faceId'])
    print x

    print "start"
    for y in lines:
        print y
        print "verify"
        
        params = urllib.urlencode({
        })
        body={
        "faceId1":str(x),
        "faceId2":str(y.strip('\n')),
        }
        jsondata=json.dumps(body)

        try:
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/verify?%s" % params,str(body), headers)
            response = conn.getresponse()
            data = response.read()
            final_data=json.loads(data)
            isidentical=final_data["isIdentical"]
            print isidentical
          
            if isidentical:
                remo(y)
                return isidentical;
            conn.close()
        except Exception as e:
            print e
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
            
    h=ptouch()
    if(h):
        return 1
    else:
        return 0
    

#button pressing
while True:
  if(GPIO.input(23) ==1):
    print "Button 1 pressed"
    z=touch()
    print z
    if z:
     x=x+1
     print "x=%i" %x
     xfile=open("/var/www/x.txt","w")
     xfile.write("%i" %x)
     xfile.close()
     time.sleep(0.25)
    else:
     print "z=%i" %z
  elif(GPIO.input(24) ==1):
    #
    
    if touch():
     y=y+1
     print "y=%i" %y
     yfile=open("/var/www/y.txt","w")
     yfile.write("%i" %y)
     yfile.close()
     time.sleep(0.25)

