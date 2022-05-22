from donkeycar.parts.controller import LocalWebController, JoystickController, WebFpv,JoyStickPub 
from donkeycar.parts.ominibot_car_com import OminibotCar,threading,sys 
import os 
import time 
import numpy 

_port = "/dev/ominibot_car"
_baud = 115200 

ominibot = OminibotCar(_port, _baud) 
ominibot.set_system_mode(platform="individual_wheel") 

a=80

joystick_message = JoyStickPub() 
while True: 
  time_data = int(time.time()) 
  message_data=joystick_message.run() 
  print("message_data=",message_data)
  print(message_data[3])
  if  message_data[2]=="left_stick_vert" and message_data[3]>0 :
      ominibot.individual_wheel(V1=a,V3=a,V2=a,V4=a, debug=False) 
      time.sleep(1)
  elif message_data[2]=="left_stick_vert" and message_data[3]<0 :
      ominibot.individual_wheel(V1=-a,V3=-a,V2=-a,V4=-a, debug=False) 
      time.sleep(1)
      
  elif message_data[2]=="left_stick_horz" and message_data[3]<0 :
        ominibot.individual_wheel(V1=0,V3=0,V2=a,V4=a, debug=False) 
        time.sleep(1) 
        
  elif message_data[2]=="left_stick_horz" and message_data[3]>0 :
        ominibot.individual_wheel(V1=a,V3=a,V2=0,V4=0, debug=False) 
        time.sleep(1) 