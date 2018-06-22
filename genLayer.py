"""
public static final WorldType[] WORLD_TYPES = new WorldType[16];

    /** Default world type. */
    public static final WorldType DEFAULT = (new WorldType(0, "default", 1)).setVersioned();

    /** Flat world type. */
    public static final WorldType FLAT = new WorldType(1, "flat");

    /** Large Biome world Type. */
    public static final WorldType LARGE_BIOMES = new WorldType(2, "largeBiomes");

    /** amplified world type */
    public static final WorldType AMPLIFIED = (new WorldType(3, "amplified")).setNotificationData();
    public static final WorldType CUSTOMIZED = new WorldType(4, "customized");
    public static final WorldType DEBUG_WORLD = new WorldType(5, "debug_all_block_states");

    /** Default (1.1) world type. */
    public static final WorldType DEFAULT_1_1 = (new WorldType(8, "default_1_1", 0)).setCanBeCreated(false);


    if we create a customized world we expecty chunk composition to change but not biome so chunkComposition doesnt matter

    if (worldTypeIn == WorldType.CUSTOMIZED && !options.isEmpty())
        {
            this.chunkComposition= ChunkGeneratorSettings.Factory.jsonToFactory(options).build();
        }

"""
import numpy as np
from collections import Counter
class Main:
    def __init__(self, seed=None):
        if seed:
            self.baseSeed = seed
            self.baseSeed *= self.baseSeed * 6364136223846793005 + 1442695040888963407
            self.baseSeed += seed
            self.baseSeed *= self.baseSeed * 6364136223846793005 + 1442695040888963407
            self.baseSeed += seed
            self.baseSeed *= self.baseSeed * 6364136223846793005 + 1442695040888963407
            self.baseSeed += seed

    def initChunkSeed(self, chunk):
        self.chunkSeed = self.worldGenSeed
        self.chunkSeed *= (self.chunkSeed * 6364136223846793005 + 1442695040888963407)
        self.chunkSeed += chunk[0]
        self.chunkSeed *= (self.chunkSeed * 6364136223846793005 + 1442695040888963407)
        self.chunkSeed += chunk[1]
        self.chunkSeed *= (self.chunkSeed * 6364136223846793005 + 1442695040888963407)
        self.chunkSeed += chunk[0]
        self.chunkSeed *= (self.chunkSeed * 6364136223846793005 + 1442695040888963407)
        self.chunkSeed += chunk[1]

    def countIt(self,array):
        dic=Counter(array)
        return [str(el) +" " + str(dic[el]/array.size) for el in dic]

    def initWorldSeed(self, seed):
        self.worldGenSeed = seed
        try:
            self.parent.initWorldSeed(seed)
        except:
            print("parent reached",self)
            pass

        self.worldGenSeed *= self.worldGenSeed * 6364136223846793005 + 1442695040888963407
        self.worldGenSeed += self.baseSeed
        self.worldGenSeed *= self.worldGenSeed * 6364136223846793005 + 1442695040888963407
        self.worldGenSeed += self.baseSeed
        self.worldGenSeed *= self.worldGenSeed * 6364136223846793005 + 1442695040888963407
        self.worldGenSeed += self.baseSeed


    def nextIntGen(self, limit):
        i = (self.chunkSeed >> 24) % limit
        if i < 0:
            i += limit
        self.chunkSeed *= (self.chunkSeed * 6364136223846793005 + 1442695040888963407)
        self.chunkSeed += self.worldGenSeed
        return i

    def selectRandom(self, l):
        return l[self.nextIntGen(len(l))]

    def genlayer(self, seed, customized):
        # customized hold 0 for normal, 1 for large and 2 for fully cuztomized, 4 for default1.1, then it holds biomeSize and river size then chunk composition

        initialLayer = g1.GenLayerIsland(1)
        firstLayer = g2.GenLayerFuzzyZoom(2000, initialLayer)
        secondLayer = g3.GenLayerAddIsland(1, firstLayer)
        thirdLayer = g4.GenLayerZoom(2001, secondLayer)
        genlayeraddisland1 = g3.GenLayerAddIsland(2, thirdLayer)
        genlayeraddisland1 = g3.GenLayerAddIsland(50, genlayeraddisland1)
        genlayeraddisland1 = g3.GenLayerAddIsland(70, genlayeraddisland1)
        genlayerremovetoomuchocean = g5.GenLayerRemoveTooMuchOcean(2, genlayeraddisland1)
        genlayeraddsnow = g6.GenLayerAddSnow(2, genlayerremovetoomuchocean)
        genlayeraddisland2 = g3.GenLayerAddIsland(3, genlayeraddsnow)
        genlayeredge = g7.GenLayerEdge(2, genlayeraddisland2, "COOL_WARM")
        genlayeredge = g7.GenLayerEdge(2, genlayeredge , "HEAT_ICE")
        genlayeredge = g7.GenLayerEdge(3, genlayeredge , "SPECIAL")
        genlayerzoom1 = g4.GenLayerZoom(2002, genlayeredge)
        genlayerzoom1 = g4.GenLayerZoom(2003, genlayerzoom1 )
        genlayeraddisland3 = g3.GenLayerAddIsland(4, genlayerzoom1)
        genlayeraddmushroomisland = g8.GenLayerAddMushroomIsland(5, genlayeraddisland3)
        genlayerdeepocean = g9.GenLayerDeepOcean(4, genlayeraddmushroomisland)
        genlayer4 = g4.GenLayerZoom.magnify(1000, genlayerdeepocean, 0)
        i, j = 4, 4
        if customized[0] == 2:
            i, j = customized[1], customized[2]
        if customized[0] == 1:
            i = 6
        lvt71 = g4.GenLayerZoom.magnify(1000, genlayer4, 0)
        genlayerriverinit = g10.GenLayerRiverInit(100, lvt71)
        lvt81 = g11.GenLayerBiome(200, genlayer4, customized)
        genlayer6 = g4.GenLayerZoom.magnify(1000, lvt81, 2)
        genlayerbiomeedge = g12.GenLayerBiomeEdge(1000, genlayer6)
        lvt91 = g4.GenLayerZoom.magnify(1000, genlayerriverinit, 2)
        genlayerhills = g13.GenLayerHills(1000, genlayerbiomeedge, lvt91)
        genlayer5=g4.GenLayerZoom.magnify(1000,genlayerriverinit,2)
        genlayer5=g4.GenLayerZoom.magnify(1000,genlayer5,j)
        genlayerriver=g14.GenLayerRiver(1,genlayer5)
        genlayersmooth=g15.GenLayerSmooth(1000,genlayerriver)
        genlayerhills=g16.GenLayerRareBiome(1001,genlayerhills)
        for k in range(i):
            genlayerhills=g4.GenLayerZoom(1000+k,genlayerhills)
            if not k:
                genlayerhills=g3.GenLayerAddIsland(3,genlayerhills)
            if k==1 or i==1:
                genlayerhills=g17.GenLayerShore(1000,genlayerhills)
        genlayersmooth1=g15.GenLayerSmooth(1000,genlayerhills)
        genlayerrivermix=g18.GenLayerRiverMix(100,genlayersmooth1,genlayersmooth)
        genlayer3=g19.GenLayerVoronoiZoom(10,genlayerrivermix)
        genlayerrivermix.initWorldSeed(seed)
        genlayer3.initWorldSeed(seed)
        print([genlayerrivermix,genlayer3,genlayerrivermix])
        return [genlayerrivermix,genlayer3,genlayerrivermix][1]

    def matchBiomes(self,l,indice,seed,customized):
        biomeId, px, pz = l[indice]
        genlayerFinal=self.genlayer(seed,customized)
        print(genlayerFinal.getInts(px,pz,1,1))
        #if biomeId==genlayerFinal.getInts(px,pz,1,1)[0]:
            #return True
        return False

    def isBiomeOceanic(self, biomeID):
        return biomeID in [24, 10, 0]

    def isValidId(self, id):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 127, 129, 130, 131, 132, 133, 134, 140, 149, 151, 155, 156,
             157, 158, 160, 161, 162, 163, 164, 165, 166, 167]
        return id in x

    def sameClass(self, biomeA, biomeB):
        flag = False
        biomeClass = {"ocean": [0, 10, 24],
                      "plains": [1, 129],
                      "desert": [2, 17, 27, 28, 29, 130],
                      "hills": [3, 20, 34, 131, 162],
                      "forest": [4, 18, 132, 157],
                      "taiga": [5, 19, 30, 31, 32, 33, 133, 158, 160, 161],
                      "swamp": [6, 134],
                      "river": [7, 11],
                      "hell": [8],
                      "end": [9],
                      "mushroom": [14, 15],
                      "mesa": [37, 38, 39],
                      "savanna": [35, 36],
                      "beach": [16, 26],
                      "stonebeach": [25],
                      "jungle": [21, 22, 23, 149, 151],
                      "savannaMutated": [163, 164],
                      "forestMutated": [155, 156],
                      "snow": [12, 13, 140],
                      "void": [127]}
        for el in biomeClass:
            if biomeB in biomeClass[el] and biomeA in biomeClass[el]:
                flag = True
        return flag

    def getTempCategory(self,biome):
        cold,medium,warm=0,1,2
        if biome in [30,158,12,140,11,26,127,10]:
            return cold #below 0.2
        elif biome in [35,163,2,130,37,165,38,166,36,39,164,167,8,17]:
            return warm #above 1.0
        else:
            return medium
    def biomesEqualOrMesaPlateau(self, biomeA, biomeB):

        if biomeA == biomeB:
            return True
        else:
            if self.isValidId(biomeA) and self.isValidId(biomeB):
                if biomeA != 38 and biomeA != 39:  # mesa rock and clear rock
                    return biomeA == biomeB or self.sameClass(biomeA, biomeB)

                else:
                    return biomeB != 38 or biomeB != 39
            else:
                return False
    def isSnowy(self,id):
        return id in [10,11,12,13,26,30,31,140,158]

    def selectModeOrRandom(self, j, l, k, i):

        if (l == k and k == i):

            return l

        elif (j == l and j == k):

            return j

        elif (j == l and j == i):

            return j
        elif (j == k and j == i):

            return j

        elif (j == l and k != i):

            return j

        elif (j == k and l != i):

            return j

        elif (j == i and l != k):

            return j

        elif (l == k and j != i):

            return l

        elif (l == i and j != k):

            return l

        else:

            return k if k == i and j != l else self.selectRandom([j, l, k, i])


import GenLayerIsland as g1
import GenLayerFuzzyZoom as g2
import GenLayerAddIsland as g3
import GenLayerZoom as g4
import GenLayerRemoveTooMuchOcean as g5
import GenLayerAddSnow as g6
import GenLayerEdge as g7
import GenLayerAddMushroomIsland as g8
import GenLayerDeepOcean as g9
import GenLayerRiverInit as g10
import GenLayerBiome as g11
import GenLayerBiomeEdge as g12
import GenLayerHills as g13
import GenLayerRiver as g14
import GenLayerSmooth as g15
import GenLayerRareBiome as g16
import GenLayerShore as g17
import GenLayerRiverMix as g18
import GenLayerVoronoiZoom as g19
if __name__ == "__main__":
    m=Main()
    customized = [0, "", "", [""]]
    seed=181201211981019340
    l=[(24,0,0)] #deep ocean
    print(m.matchBiomes(l,0,seed,customized))
