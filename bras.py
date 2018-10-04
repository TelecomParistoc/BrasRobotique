from AX12 import AX12
#angles settings in degree
basea0=0
epaulea0=45
coudea0=140#/!\ negativ angles
pinceopen=45
pinceclose=-29

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
