from genLayer import Main
import numpy as np
class GenLayerFuzzyZoom(Main):
    def __init__(self, seed, layer):
        super().__init__(seed)
        self.parent = layer


    def selectModeOrRandom(self, j, l, k, i):
        return self.selectRandom([j, l, k, i])

    def getInts(self, aX, aY, aW, aH):
        l=self.parent.getInts(aX, aY, aW, aH)
        print("fuzzy",self.countIt(l))
        return l