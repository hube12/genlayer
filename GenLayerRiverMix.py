from genLayer import Main
import numpy as np

class GenLayerRiverMix(Main):
    def __init__(self, seed, biomePattern, riverPattern):
        super().__init__(seed)
        self.biomePatternGeneratorChain = biomePattern
        self.riverPatternGeneratorChain = riverPattern

    def initWorldSeed(self, seed):  # check needed
        self.biomePatternGeneratorChain.initWorldSeed(seed)
        self.riverPatternGeneratorChain.initWorldSeed(seed)
        super().initWorldSeed(seed)

    def getInts(self, aX, aY, aW, aH):
        aint = self.biomePatternGeneratorChain.getInts(aX - 1, aY - 1, aW + 2, aH + 2)
        aint1 = self.riverPatternGeneratorChain.getInts(aX - 1, aY - 1, aW + 2, aH + 2)
        aint2 = np.empty(aW*aH,dtype=int)
        for i in range(aH * aW):
            if aint[i] != 0 and aint[i] != 24:  # not ocean
                if aint1[i] == 7:  # river
                    if aint[i] == 12:  # ice plains
                        aint2[i] = 11  # frozen river
                    elif aint[i] != 14 and aint[i] != 15:  # not mushroom
                        aint2[i] = aint1[i] & 255
                    else:
                        aint2[i] = 15  # mushroom shore
                else:
                    aint2[i] = aint[i]
            else:
                aint2[i] = aint[i]
        return aint2


