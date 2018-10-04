from AX12 import AX12
import math

def stop(ax12):
    stopped = False
    while not stopped:
       try:
          ax12.turn(0)
          stopped = True
       except:
          pass

base = AX12(121)
stop(base)
epaule = AX12(142)
stop(epaule)
coude = AX12(25)
stop(coude)
pince = AX12(145)
stop(pince)

try:
    pince.move(-45)
except:
    pass

def deplacerBras(x, y)

    q2 = acos((x*x+y*y-(l1*l1+l2*l2))/(2*l1*l2));
	q1 = atan((y*(l1+l2*cos(q2))-x*l2*sin(q2))/(x*(l1+l2*cos(q2))+y*l2*sin(q2)));
    q2 *= (180/PI);
    q1 *= (180/PI)+45;
