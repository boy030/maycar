from donkeycar.parts.ominibot_car_com import OminibotCar,threading,sys 
import time 

_port = "/dev/ominibot_car"
_baud = 115200 

ominibot = OminibotCar(_port, _baud) 
ominibot.set_system_mode(platform="individual_wheel") 

a=80

#w
ominibot.individual_wheel(V1=a,V3=a,V2=a,V4=a, debug=False) 
time.sleep(2) 

#d
ominibot.individual_wheel(V1=a,V3=a,V2=0,V4=0, debug=False) 
time.sleep(2) 

#a
ominibot.individual_wheel(V1=0,V3=0,V2=a,V4=a, debug=False) 
time.sleep(2) 

#s 
ominibot.individual_wheel(V1=0,V3=0,V2=0,V4=0, debug=False) 
time.sleep(2) 

#ss
ominibot.individual_wheel(V1=-a,V3=-a,V2=-a,V4=-a, debug=False) 
time.sleep(2)