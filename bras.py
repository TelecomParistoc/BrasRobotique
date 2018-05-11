from AX12 import AX12

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
    pince.move(0)
except:
    pass
