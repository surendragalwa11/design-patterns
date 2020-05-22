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
        try:
            zone = config[self.zone]
        except Exception as e:
            # default zone when we don't have zone config
            zones = list(config.keys())
            zone = config[zones[0]]
        return zone

if __name__ == '__main__':
    zone = ZoneFactory('UK').getZone()
    confidence = zone.getConfidence()
    threshold = zone.getThreshold()
    print(confidence, threshold)


    