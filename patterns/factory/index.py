from AsiaZone import AsiaZone
from UKZone import UKZone
from USZone import USZone

class ZoneFactory:
    def __init__(self, zone):
        self.zone = zone

    def getZone(self):
        if self.zone == 'ASIA':
            return AsiaZone()
        elif self.zone == 'US':
            return USZone()
        else:
            return UKZone()

if __name__ == '__main__':
    zone = ZoneFactory('ASIA').getZone()
    confidence = zone.getConfidence()
    threshold = zone.getThreshold()
    print(confidence, threshold)


    