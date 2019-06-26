class GearProfile:
    def __init__(self, dogTeeth, hexTeeth, pinionTeeth, pHexTeeth, lowGearBool):
        self.dogTeeth = dogTeeth
        self.hexTeeth = hexTeeth
        self.pinionTeeth = pinionTeeth
        self.pHexTeeth = pHexTeeth
        self.lowGearBool = lowGearBool
        self.ratio1 = round((dogTeeth / hexTeeth)*(pHexTeeth / pinionTeeth),3)
        self.separationDiameter = dogGears[dogTeeth]+hexGears[hexTeeth]
        self.dog2Teeth = []
        self.hex2Teeth = []
    def otherRatios(self):
        otherGears = []
        for dogTeeth0,dogDiameter in dogGears.items():
           for hexTeeth0, hexDiameter in hexGears.items():
               if dogTeeth0 != self.dogTeeth and dogDiameter + hexDiameter == self.separationDiameter:
                   ratio2 = round((dogTeeth0 / hexTeeth0)*(self.pHexTeeth / self.pinionTeeth),3)
                   greaterThanBool = ratio2 > self.ratio1
                   if (self.lowGearBool != greaterThanBool):
                       self.dog2Teeth.append(dogTeeth0)
                       self.hex2Teeth.append(hexTeeth0)
                       otherGears.append(ratio2)
        return otherGears

#Gear Dictionaries {Teeth:Pitch-Diameter}
pinions = {9:0.5, 10:0.6, 11:0.6, 12:0.6, 13:0.7, 14:0.7}
dogGears = {40:2.0, 44:2.2, 50:2.5, 60:3.0}
hexGears = {14:0.7, 16:0.8, 18:0.9, 20:1.0, 22:1.1, 24:1.2, 26:1.3, 28:1.4, 30:1.5, 32:1.6, 34:1.7, 36:1.8, 38:1.9, 40:2.0, 42:2.1, 44:2.2, 46:2.3, 50:2.5, 52:2.6}

targetRatio = float(input("Target Ratio: "))
maximumVariance = float(input("Maximum Variance: "))
lowGearQuestion = 'y' == input("Low Gear? (y/n)")

Gearbox = []

for dogTeeth,dogDiameter in dogGears.items():
    for hexTeeth, hexDiameter in hexGears.items():
        for pinionTeeth,pinionDiameter in pinions.items():
            for pHexTeeth,pHexDiameter in hexGears.items():
                if pHexDiameter > hexDiameter and pHexDiameter > 2.52-pinionDiameter and pHexDiameter + 1.125 < dogDiameter + hexDiameter:
                    profileObject = GearProfile(dogTeeth, hexTeeth, pinionTeeth, pHexTeeth, lowGearQuestion)
                    if profileObject.ratio1 < targetRatio + maximumVariance and profileObject.ratio1 > targetRatio - maximumVariance:
                        Gearbox.append(profileObject)



for x in Gearbox:
    others = x.otherRatios()
    if others != []:
        print('[',x.ratio1,']', others,'[',x.pHexTeeth,':',x.pinionTeeth,']','[',x.dogTeeth,':',x.hexTeeth,']','[', x.dog2Teeth,':', x.hex2Teeth,']')