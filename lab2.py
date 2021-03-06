import RPi.GPIO as GPIO
from time import sleep
p1=4
p2=17
p3=27
in1,in2=23,24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT) 
GPIO.setup(in1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
try:
  def myCallback(pin):
    if pin==in1:
      pwm1=GPIO.PWM(p1,100)
      pwm1.start(0)
      for dc in range(101):
        pwm1.ChangeDutyCycle(dc)
        sleep(0.01)
      for dc in range(100,0,-1):
        pwm1.ChangeDutyCycle(dc)
        sleep(0.01)
    if pin==in2:
      pwm2=GPIO.PWM(p2,100)
      pwm2.start(0)
      for dc in range(101):
        pwm2.ChangeDutyCycle(dc)
        sleep(0.01)
      for dc in range(100,0,-1):
        pwm2.ChangeDutyCycle(dc)
        sleep(0.01)
  GPIO.add_event_detect(in1,GPIO.FALLING,callback=myCallback,bouncetime=500)
  GPIO.add_event_detect(in2,GPIO.FALLING,callback=myCallback,bouncetime=500)
  while True:
    GPIO.output(p3, 0)
    sleep(0.5)
    GPIO.output(p3, 1)
    sleep(0.5)
except KeyboardInterrupt:
  print('\nExiting')
GPIO.cleanup()