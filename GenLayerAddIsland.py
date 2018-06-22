from genLayer import Main
import numpy as np

class GenLayerAddIsland(Main):
    def __init__(self, seed, layer):
        super().__init__(seed)
        self.parent = layer

    def getInts(self, aX, aY, aW, aH):
        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent.getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                k1 = aint[j1 + i1 * k]
                l1 = aint[j1 + 2 + i1 * k]
                i2 = aint[j1 + (i1 + 2) * k]
                j2 = aint[j1 + 2 + (i1 + 2) * k]
                k2 = aint[j1 + 1 + (i1 + 1) * k]
                self.initChunkSeed((j1 + aX, i1 + aY))
                if k2 or ((not k1) and (not l1) and (not i2) and (not j2)):
                    if k2 > 0 and ((not k1) or (not l1) or (not i2) or (not j2)):
                        if not self.nextIntGen(5):
                            if k2 == 4:
                                aint1[j1 + i1 * aW] = 4
                            else:
                                aint1[j1 + i1 * aW] = 0
                        else:
                            aint1[j1 + i1 * aW] = k2
                    else:
                        aint1[j1 + i1 * aW] = k2
                else:
                    i3 = 1
                    if k1 and not self.nextIntGen(1):
                        i3 = k1
                    if l1 and not self.nextIntGen(2):
                        i3 = l1
                    if i2 and not self.nextIntGen(3):
                        i3 = i2
                    if j2 and not self.nextIntGen(4):
                        i3 = j2
                    if not self.nextIntGen(3):
                        aint1[j1 + i1 * aW] = i3
                    elif i3 == 4:
                        aint1[j1 + i1 * aW] = 4
                    else:
                        aint1[j1 + i1 * aW] = 0
        print("addislan",self.countIt(aint1))
        return aint1