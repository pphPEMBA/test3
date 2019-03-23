# getting the main GPIO libraly
import RPi.GPIO as GPIO
# getting the time libraly
import time

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings 
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use 
pinList= [18,17,15,14] 

#setting the mode for all pins so all will be switched on 


#for loop where pin = 18 next 17 ,15, 14 
for pin in pinList:
	#setting the GPIO to HIGH or 1 or true
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin,  GPIO.HIGH)

SleepTimeS = 0.1

try:
  while True:

    for pin in pinList:
      GPIO.output(pin, GPIO.LOW)
      time.sleep(SleepTimeS);

    for pin in pinList:
      GPIO.output(pin, GPIO.HIGH)
      time.sleep(SleepTimeS);
      
    pinList.reverse()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

#cleaning all GPIO's 
GPIO.cleanup()
print "Shutdown All relays"