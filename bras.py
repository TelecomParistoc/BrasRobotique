from AX12 import AX12

base = AX12(121)
epaule = AX12(142)
coude = AX12(25)
pince = AX12(145)

try:
    pince.move(0)
except:
    pass