from AsiaZone import AsiaZone
from UKZone import UKZone
from USZone import USZone

class ZoneFactory:
    def __init__(self, zone):
        self.zone = zone

    def getFactoryConfig(self):
        return {
            'ASIA': AsiaZone(),
            'US': USZone(),
            'UK': UKZone()
        }

    def getZone(self):
        config = self.getFactoryConfig()
        zone = config[self.zone]
        return zone

if __name__ == '__main__':
    zone = ZoneFactory('ASI').getZone()
    confidence = zone.getConfidence()
    threshold = zone.getThreshold()
    print(confidence, threshold)


    