###
### P1
### CHONG GUO
### Can't save and share on EarSketch social website
### github link: https://github.com/ginrain/LMC6310cguo/blob/master/p1.py
###

from earsketch import *
 
init()
setTempo(100)

'''
======== use customized function to read image file and generate a beat pattern ========
'''
def createDrumbeats_garlic(myImage):
 
    drumBeats = []
    for size in range(len(myImage)):
        drumBeats.append("")
 
    for outerCounter in range(len(myImage)):
        for innerCounter in range(len(myImage[0])):
            if (myImage[outerCounter][innerCounter] >100 ):  # if the color is white
                drumBeats[outerCounter] = drumBeats[outerCounter] + "+" # 
            elif (myImage[outerCounter][innerCounter] < 1):
                drumBeats[outerCounter] = drumBeats[outerCounter] + "0" 
    return drumBeats

def createDrumbeats_bean(myImage):
 
    drumBeats = []
    for size in range(len(myImage)):
        drumBeats.append("")
 
    for outerCounter in range(len(myImage)):
        for innerCounter in range(len(myImage[0])):
            if (myImage[outerCounter][innerCounter] >100 ):  # if the color is white
                drumBeats[outerCounter] = drumBeats[outerCounter] + "+" # 
            elif (myImage[outerCounter][innerCounter] < 10):
                drumBeats[outerCounter] = drumBeats[outerCounter] + "0" # rest
    return drumBeats

def createDrumbeats_cat(myImage):
 
    drumBeats = []
    for size in range(len(myImage)):
        drumBeats.append("")
 
    for outerCounter in range(len(myImage)):
        for innerCounter in range(len(myImage[0])):
            if (myImage[outerCounter][innerCounter] >150 ):  # if the color is white
                drumBeats[outerCounter] = drumBeats[outerCounter] + "+" # 
            elif (myImage[outerCounter][innerCounter] < 5):
                drumBeats[outerCounter] = drumBeats[outerCounter] + "0" # rest
    return drumBeats

def createDrumbeats_corn(myImage):
 
    drumBeats = []
    for size in range(len(myImage)):
        drumBeats.append("")
 
    for outerCounter in range(len(myImage)):
        for innerCounter in range(len(myImage[0])):
            if (myImage[outerCounter][innerCounter] >100 ):  # if the color is white
                drumBeats[outerCounter] = drumBeats[outerCounter] + "+" # 
            elif (myImage[outerCounter][innerCounter] < 10):
                drumBeats[outerCounter] = drumBeats[outerCounter] + "0" # rest
    return drumBeats

def createDrumbeats_broccoli(myImage):
 
    drumBeats = []
    for size in range(len(myImage)):
        drumBeats.append("")
 
    for outerCounter in range(len(myImage)):
        for innerCounter in range(len(myImage[0])):
            if (myImage[outerCounter][innerCounter] >200 ):  # if the color is white
                drumBeats[outerCounter] = drumBeats[outerCounter] + "+" # 
            elif (myImage[outerCounter][innerCounter] < 4):
                drumBeats[outerCounter] = drumBeats[outerCounter] + "0" # rest
    return drumBeats

'''
======== use customized function to convert a list of 2D list into a 64-element list ========
'''
def convert3Dto1D(myImage3D):
    new1DList = []
    for outerCounter in range(len(myImage3D)):
        for middleCounter in range(len(myImage3D[0])):
            listSum = sum(myImage3D[outerCounter][middleCounter])
            listLength = len(myImage3D[outerCounter][middleCounter])
            listAverage = listSum / listLength
            #Test Module
            #print ListAverage
            new1DList.append(listAverage)
            #Test Module
            #print new1DList
    return new1DList

'''
======== raw data that got from 8*8 greyscale image ========
'''
myImage_garlic1 = [[10,9,4,4,8,3,8,0],[11,6,5,3,9,6,6,0],[6,8,3,5,2,6,9,0],[5,10,10,135,188,6,8,0],[1,4,184,221,245,66,8,2],[5,8,8,2,4,1,6,7],[6,7,7,7,2,8,9,9],[0,7,11,11,10,9,12,10]]
myImage_garlic2 = [[10,3,12,4,6,15,7,0],[3,8,4,8,9,10,70,0],[9,14,10,2,10,4,6,7],[10,1,10,216,0,11,11,6],[2,9,185,245,243,10,3,5],[6,7,6,5,5,6,2,10],[8,7,9,9,8,8,8,9],[1,7,0,10,10,7,9,0]]
myImage_garlic3 = [[0,2,3,1,0,5,3,1],[8,0,3,0,3,4,5,0],[1,1,2,3,0,5,6,1],[1,7,0,7,135,0,0,0],[0,7,186,216,219,0,5,6],[1,5,0,0,0,0,2,1],[2,8,0,5,4,3,6,0],[3,1,0,1,0,5,2,8]]
myImage_garlic4 = [[2,3,0,2,0,0,1,1],[1,5,0,1,0,4,4,1],[0,1,1,0,0,3,0,0],[1,0,188,136,184,0,3,0],[0,4,64,188,219,135,0,0],[0,0,0,0,1,0,1,0],[0,2,1,0,2,1,0,0],[0,2,0,0,0,2,2,0]]
myImage_garlic5 = [[3,2,1,0,0,0,4,0],[1,1,0,0,0,0,5,0],[2,1,65,70,1,0,0,2],[6,185,135,137,182,179,0,0],[0,243,179,180,137,183,0,0],[1,0,0,1,0,0,0,0],[1,8,0,1,5,2,4,0],[0,0,0,0,4,0,1,0]]
myImage_garlic6 = [[3,2,5,6,0,3,0,1],[5,8,0,0,0,3,7,0],[0,1,0,63,8,3,3,0],[0,64,185,180,136,63,0,0],[1,183,187,136,7,218,0,0],[0,0,0,1,0,0,1,0],[5,2,0,2,1,2,0,0],[1,0,0,9,0,0,0,1]]
myImage_garlic7 = [[1,11,8,10,2,0,8,0],[3,1,7,9,0,9,1,1],[3,6,10,8,2,4,9,1],[7,3,68,185,133,215,0,0],[0,220,186,219,183,243,0,2],[0,0,3,3,0,1,4,2],[7,0,3,1,3,2,0,0],[9,2,3,1,9,6,10,2]]
myImage_garlic8 = [[7,8,3,3,9,11,7,0],[2,11,8,6,11,9,10,0],[2,3,6,8,3,8,7,0],[6,9,10,187,218,0,11,1],[8,7,184,185,244,222,9,4],[12,1,3,0,2,8,7,1],[9,7,4,11,5,10,1,10],[9,7,8,9,3,2,2,0]]
#build a list of 2D lists:
myImage3D_garlic = [myImage_garlic1, myImage_garlic2, myImage_garlic3, myImage_garlic4, myImage_garlic5, myImage_garlic6, myImage_garlic7,myImage_garlic8]

myImage_broccoli1 = [[2,2,2,2,2,2,2,2],[2,2,87,87,2,2,53,16],[2,137,16,53,70,221,35,2],[70,16,35,2,2,2,2,2],[2,2,2,2,109,243,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2]]
myImage_broccoli2 = [[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,35,16,70,35,35,2,2],[2,2,109,197,53,35,2,2],[2,2,53,35,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2]]
myImage_broccoli3 = [[2,2,2,2,2,2,2,2],[2,2,70,53,2,2,2,2],[2,35,2,137,87,2,2,2],[2,16,2,197,197,16,2,2],[2,2,35,221,221,2,35,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2]]
myImage_broccoli4 = [[2,2,2,2,2,2,2,2],[2,87,16,2,109,35,2,87],[53,16,243,87,53,2,137,2],[16,169,2,70,2,2,2,2],[243,2,2,2,2,2,2,2],[2,2,2,2,221,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2]]
myImage_broccoli5 = [[2,70,2,35,35,35,53,16],[87,16,2,2,221,2,197,2],[243,16,2,2,2,2,137,2],[2,16,2,221,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,109,2,2,2],[2,2,2,2,169,2,2,2],[2,2,2,2,2,2,2,2]]
myImage_broccoli6 = [[2,2,70,53,16,70,2,2],[35,35,35,2,53,2,35,2],[2,2,2,197,2,2,2,2],[2,2,109,2,35,2,2,2],[2,2,2,2,243,197,2,2],[2,137,243,221,197,243,2,2],[2,2,221,243,35,2,2,2],[2,197,2,243,35,16,2,2]]
myImage_broccoli7 = [[2,2,87,53,35,2,2,2],[2,70,2,35,109,35,16,2],[53,2,16,221,2,2,2,2],[2,16,2,221,2,2,2,2],[2,2,35,243,109,2,2,2],[2,2,197,221,221,2,2,2],[2,2,2,243,243,87,2,2],[2,2,2,221,221,2,2,2]]
myImage_broccoli8 = [[2,2,35,53,53,70,53,2],[53,169,53,35,2,70,169,2],[2,35,2,197,2,169,2,2],[2,2,2,2,2,2,2,2],[2,2,53,2,2,2,2,2],[2,137,2,53,2,2,2,2],[2,2,2,2,243,2,2,2],[2,2,2,2,169,2,2,2]]
#build a list of 2D lists:
myImage3D_broccoli = [myImage_broccoli1, myImage_broccoli2, myImage_broccoli3, myImage_broccoli4, myImage_broccoli5, myImage_broccoli6, myImage_broccoli7, myImage_broccoli8]

myImage_bean1 = [[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,94,0,2,2,2,2,2],[2,2,2,2,2,2,2,2],[2,2,2,220,1,2,2,2],[2,2,2,2,2,2,2,2]]
myImage_bean2 = [[2,2,2,2,2,2,2,2],[2,2,2,145,228,2,2,2],[2,10,50,153,2,2,2,2],[2,2,31,113,75,114,2,2],[2,33,160,2,37,166,2,2],[2,2,2,2,2,2,2,2],[2,2,2,94,36,2,2,2],[2,2,2,2,2,2,2,2]]
myImage_bean3 = [[2,2,2,2,2,2,2,2],[2,2,3,43,142,88,2,2],[2,2,188,160,123,20,2,2],[2,2,51,133,42,16,2,2],[2,2,164,54,203,121,2,2],[2,2,243,2,2,73,2,2],[2,2,133,160,214,0,33,2],[2,2,2,2,123,57,2,2]]
myImage_bean4 = [[2,128,4,2,2,133,2,2],[138,151,56,109,2,2,2,2],[54,112,83,99,137,6,101,2],[2,2,170,205,87,2,2,2],[133,2,2,85,54,2,2,2],[2,2,2,59,17,116,2,2],[2,2,14,2,125,122,142,2],[2,2,2,2,2,2,2,2]]
myImage_bean5 = [[2,17,181,2,2,2,2,2],[115,183,115,2,2,182,164,2],[2,2,25,2,2,79,17,2],[188,121,2,101,180,2,104,2],[113,2,2,2,212,13,6,22],[142,125,58,2,78,182,2,2],[2,2,42,31,159,86,2,2],[59,114,2,106,2,201,92,2]]
myImage_bean6 = [[2,8,2,1,0,2,2,2],[164,2,170,2,103,221,1,2],[209,2,186,158,74,2,69,129],[2,2,2,196,167,2,121,2],[2,32,23,148,36,2,2,2],[2,22,140,45,189,134,22,2],[2,206,2,204,2,30,1,2],[59,96,124,93,5,0,18,2]]
myImage_bean7 = [[182,179,120,2,217,2,2,2],[27,2,2,71,70,138,10,2],[121,216,68,122,76,2,141,2],[48,202,2,76,137,2,2,2],[75,2,2,2,2,2,2,2],[2,176,2,46,247,2,210,2],[2,46,153,183,67,163,162,2],[100,210,15,136,51,145,64,2]]
myImage_bean8 = [[91,2,54,83,30,2,2,2],[2,162,2,95,2,118,2,2],[2,6,166,46,139,2,210,2],[54,2,10,45,2,140,2,2],[37,22,2,2,54,40,184,2],[101,2,45,73,2,2,176,2],[2,32,123,151,2,153,2,2],[2,151,85,156,2,2,41,2]]
#build a list of 2D lists:
myImage3D_bean = [myImage_bean1, myImage_bean2, myImage_bean3, myImage_bean4, myImage_bean5, myImage_bean6, myImage_bean7, myImage_bean8]

myImage_cat1 = [[85,81,226,123,204,84,85,52],[131,208,255,172,248,155,85,85],[89,251,119,179,254,230,96,85],[98,247,84,235,253,255,85,85],[83,207,243,201,239,217,129,87],[119,188,254,138,254,201,85,71],[80,85,176,195,221,81,84,70],[75,82,54,85,55,70,85,39]]
myImage_cat2 = [[85,84,172,249,185,68,58,66],[78,171,253,241,254,239,85,67],[101,128,227,174,231,255,85,83],[81,202,221,239,218,198,96,85],[85,219,238,185,186,235,110,85],[85,170,236,171,195,200,85,85],[72,85,164,202,202,84,56,85],[74,57,84,83,86,88,81,42]]
myImage_cat3 = [[129,85,202,207,199,85,60,55],[85,164,212,144,233,200,86,83],[85,238,200,242,253,222,97,123],[85,232,227,156,253,206,128,110],[85,199,199,233,205,213,123,84],[85,108,191,209,197,209,85,85],[55,74,171,167,124,85,85,82],[55,55,59,77,60,57,84,58]]
myImage_cat4 = [[80,85,169,130,199,79,85,70],[85,250,208,177,211,210,87,81],[99,203,128,238,252,220,129,109],[99,225,114,192,223,254,104,85],[85,181,127,203,254,254,124,85],[70,219,202,247,244,199,85,85],[85,63,160,213,166,83,85,85],[50,55,54,50,57,84,52,42]]
myImage_cat5 = [[85,85,201,171,168,87,58,58],[85,138,222,222,166,253,77,92],[85,242,251,222,85,252,124,123],[118,236,254,241,85,202,79,90],[87,170,253,185,204,181,125,85],[124,184,233,210,174,195,85,85],[85,77,217,194,159,94,86,85],[55,51,55,75,83,84,87,59]]
myImage_cat6 = [[69,84,200,171,173,87,89,89],[85,202,248,168,199,217,79,85],[84,156,85,254,237,237,85,85],[85,203,81,174,170,199,86,85],[85,171,127,169,247,215,123,85],[85,170,152,221,211,169,95,63],[61,73,135,169,178,86,81,80],[55,53,71,55,85,83,62,0]]
myImage_cat7 = [[108,85,184,244,128,65,54,53],[85,192,222,171,128,201,85,85],[90,208,232,255,248,246,110,85],[124,220,253,211,200,189,85,85],[84,200,246,208,231,242,85,85],[85,203,218,130,129,107,85,85],[85,86,181,172,83,85,85,74],[55,59,78,70,85,66,79,2]]
myImage_cat8 = [[82,84,202,91,200,127,85,76],[113,151,225,254,253,169,85,87],[110,253,125,168,253,199,85,85],[91,209,82,203,253,219,104,114],[131,174,183,199,255,223,85,84],[92,172,178,168,248,194,84,78],[85,81,169,128,223,83,63,57],[89,84,71,85,69,80,80,2]]
#build a list of 2D lists:
myImage3D_cat = [myImage_cat1, myImage_cat2, myImage_cat3, myImage_cat4, myImage_cat5, myImage_cat6, myImage_cat7,myImage_cat8]

myImage_corn1 = [[2,112,232,163,163,55,2,2],[112,201,232,9,163,201,55,2],[232,112,112,163,55,201,201,2],[201,163,112,163,112,163,201,9],[201,201,112,55,55,201,201,3],[55,201,232,112,201,112,55,5],[2,9,163,163,163,112,9,9],[3,9,2,2,3,6,9,3]]
myImage_corn2 = [[9,112,201,163,163,9,2,2],[55,201,112,55,163,201,112,9],[232,112,112,55,55,163,163,2],[232,232,163,163,55,201,201,9],[232,232,55,55,55,163,6,2],[55,163,201,163,163,163,55,9],[9,55,201,112,232,55,3,9],[9,3,2,2,3,2,2,7]]
myImage_corn3 = [[6,55,232,201,201,55,2,5],[55,163,232,55,201,201,55,9],[201,112,112,112,55,163,112,2],[232,112,55,163,55,232,163,55],[232,232,9,55,55,112,201,6],[55,163,163,163,163,201,55,6],[2,55,112,232,232,112,9,3],[9,9,2,2,9,2,3,6]]
myImage_corn4 = [[6,201,163,232,163,55,2,6],[55,201,201,9,163,163,55,3],[232,112,55,112,55,163,232,2],[201,163,112,163,55,201,163,55],[201,232,6,112,55,201,163,2],[55,232,201,232,201,112,55,2],[2,55,232,201,232,55,6,6],[2,9,3,2,3,6,2,2]]
myImage_corn5 = [[2,55,232,232,201,55,2,3],[55,163,232,55,163,201,55,6],[232,232,55,112,55,163,163,2],[232,112,55,163,55,163,163,2],[163,232,9,112,7,232,163,3],[55,201,163,163,163,201,55,9],[2,9,55,163,55,9,6,2],[6,7,9,3,2,2,2,3]]
myImage_corn6 = [[6,163,232,163,232,55,3,5],[55,163,232,55,163,163,9,5],[163,112,55,112,112,163,112,2],[201,201,9,112,112,201,163,2],[112,201,6,163,9,201,112,2],[9,112,201,201,163,232,2,2],[9,55,55,163,9,2,2,5],[2,5,2,9,2,2,2,3]]
myImage_corn7 = [[5,112,201,201,163,55,2,9],[112,163,112,112,232,201,55,5],[232,232,55,112,3,112,201,3],[201,55,112,163,55,163,112,2],[163,163,55,112,55,163,55,5],[55,201,232,112,201,112,55,9],[2,112,232,163,232,55,2,2],[3,3,2,2,3,2,2,2]]
myImage_corn8 = [[6,163,201,163,112,55,2,7],[163,201,201,2,163,163,9,9],[232,112,112,112,55,201,201,2],[201,55,112,112,112,163,112,2],[163,163,112,112,55,163,55,9],[55,232,232,163,201,163,55,9],[2,112,232,232,112,112,9,6],[2,2,2,2,6,2,9,7]]
#build a list of 2D lists:
myImage3D_corn = [myImage_corn1, myImage_corn2, myImage_corn3, myImage_corn4, myImage_corn5, myImage_corn6, myImage_corn7, myImage_corn8]


'''
======== load music from the eyesketch library ========
'''
snare1 = TECHNO_LOOP_PART_026
snare2 = TECHNO_CLUB_ANALOGLEAD_003
snare3 = TECHNO_SYNTHPLUCK_003
snare4 = TECHNO_MAINLOOP_018
snare5 = TECHNO_ACIDBASS_011
#load the customized sound
snare6 = ForkPlateKnife_01


'''
======== calculate the beat pattern ========
'''
drumBeats_garlic1 = createDrumbeats_garlic(myImage_garlic1)
drumBeats_garlic2 = createDrumbeats_garlic(myImage_garlic2)
drumBeats_garlic3 = createDrumbeats_garlic(myImage_garlic3)
drumBeats_garlic4 = createDrumbeats_garlic(myImage_garlic4)
drumBeats_garlic5 = createDrumbeats_garlic(myImage_garlic5)
drumBeats_garlic6 = createDrumbeats_garlic(myImage_garlic6)
drumBeats_garlic7 = createDrumbeats_garlic(myImage_garlic7)
drumBeats_garlic8 = createDrumbeats_garlic(myImage_garlic8)

drumBeats_broccoli1 = createDrumbeats_broccoli(myImage_broccoli1)
drumBeats_broccoli2 = createDrumbeats_broccoli(myImage_broccoli2)
drumBeats_broccoli3 = createDrumbeats_broccoli(myImage_broccoli3)
drumBeats_broccoli4 = createDrumbeats_broccoli(myImage_broccoli4)
drumBeats_broccoli5 = createDrumbeats_broccoli(myImage_broccoli5)
drumBeats_broccoli6 = createDrumbeats_broccoli(myImage_broccoli6)
drumBeats_broccoli7 = createDrumbeats_broccoli(myImage_broccoli7)
drumBeats_broccoli8 = createDrumbeats_broccoli(myImage_broccoli8)

drumBeats_corn1 = createDrumbeats_corn(myImage_corn1)
drumBeats_corn2 = createDrumbeats_corn(myImage_corn2)
drumBeats_corn3 = createDrumbeats_corn(myImage_corn3)
drumBeats_corn4 = createDrumbeats_corn(myImage_corn4)
drumBeats_corn5 = createDrumbeats_corn(myImage_corn5)
drumBeats_corn6 = createDrumbeats_corn(myImage_corn6)
drumBeats_corn7 = createDrumbeats_corn(myImage_corn7)
drumBeats_corn8 = createDrumbeats_corn(myImage_corn8)

drumBeats_cat1 = createDrumbeats_cat(myImage_cat1)
drumBeats_cat2 = createDrumbeats_cat(myImage_cat2)
drumBeats_cat3 = createDrumbeats_cat(myImage_cat3)
drumBeats_cat4 = createDrumbeats_cat(myImage_cat4)
drumBeats_cat5 = createDrumbeats_cat(myImage_cat5)
drumBeats_cat6 = createDrumbeats_cat(myImage_cat6)
drumBeats_cat7 = createDrumbeats_cat(myImage_cat7)
drumBeats_cat8 = createDrumbeats_cat(myImage_cat8)

drumBeats_bean1 = createDrumbeats_bean(myImage_bean1)
drumBeats_bean2 = createDrumbeats_bean(myImage_bean2)
drumBeats_bean3 = createDrumbeats_bean(myImage_bean3)
drumBeats_bean4 = createDrumbeats_bean(myImage_bean4)
drumBeats_bean5 = createDrumbeats_bean(myImage_bean5)
drumBeats_bean6 = createDrumbeats_bean(myImage_bean6)
drumBeats_bean7 = createDrumbeats_bean(myImage_bean7)
drumBeats_bean8 = createDrumbeats_bean(myImage_bean8)


'''
======== convert raw data into a list of numbers ========
'''
numberWave_bean = convert3Dto1D(myImage3D_bean)
numberWave_cat = convert3Dto1D(myImage3D_cat)
numberWave_corn = convert3Dto1D(myImage3D_corn)
numberWave_broccoli = convert3Dto1D(myImage3D_broccoli)
numberWave_garlic = convert3Dto1D(myImage3D_garlic)

'''
print numberWave_garlic
print numberWave_broccoli
print numberWave_corn
print numberWave_bean
print numberWave_cat
print drumBeats_b1
print drumBeats_b2
print drumBeats_b3
print drumBeats_b4
print drumBeats_b5
print drumBeats_b6
print drumBeats_b7
print drumBeats_b8
'''


'''
======== put everything on the track ========
'''
for counter in range(len(drumBeats_garlic1)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter, drumBeats_garlic1[counter])

for counter in range(len(drumBeats_garlic2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter+8, drumBeats_garlic2[counter])

for counter in range(len(drumBeats_garlic2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter+16, drumBeats_garlic3[counter])
    
for counter in range(len(drumBeats_garlic2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter+24, drumBeats_garlic4[counter])
    
for counter in range(len(drumBeats_garlic2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter+32, drumBeats_garlic5[counter])
    
for counter in range(len(drumBeats_garlic2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter+40, drumBeats_garlic6[counter])

for counter in range(len(drumBeats_garlic2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter+48, drumBeats_garlic7[counter])

for counter in range(len(drumBeats_garlic2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare1, 1, counter+56, drumBeats_garlic8[counter])


for counter in range(len(drumBeats_broccoli1)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter, drumBeats_broccoli1[counter])
    
for counter in range(len(drumBeats_broccoli2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter+8, drumBeats_broccoli2[counter])

for counter in range(len(drumBeats_broccoli3)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter+16, drumBeats_broccoli3[counter])

for counter in range(len(drumBeats_broccoli4)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter+24, drumBeats_broccoli4[counter])
    
for counter in range(len(drumBeats_broccoli5)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter+32, drumBeats_broccoli5[counter])

for counter in range(len(drumBeats_broccoli6)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter+40, drumBeats_broccoli6[counter])

for counter in range(len(drumBeats_broccoli7)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter+48, drumBeats_broccoli7[counter])

for counter in range(len(drumBeats_broccoli8)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare3, 3, counter+56, drumBeats_broccoli8[counter])
# =========================================================
for counter in range(len(drumBeats_corn1)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter, drumBeats_corn1[counter])
    
for counter in range(len(drumBeats_corn2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter+8, drumBeats_corn2[counter])

for counter in range(len(drumBeats_corn3)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter+16, drumBeats_corn3[counter])

for counter in range(len(drumBeats_corn4)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter+24, drumBeats_corn4[counter])
    
for counter in range(len(drumBeats_corn5)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter+32, drumBeats_corn5[counter])

for counter in range(len(drumBeats_corn6)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter+40, drumBeats_corn6[counter])

for counter in range(len(drumBeats_corn7)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter+48, drumBeats_corn7[counter])

for counter in range(len(drumBeats_corn8)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare2, 2, counter+56, drumBeats_corn8[counter])

# =========================================================
for counter in range(len(drumBeats_cat1)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter, counter+8)
    
for counter in range(len(drumBeats_cat2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter+8, counter+16)

for counter in range(len(drumBeats_cat3)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter+16, counter+24)

for counter in range(len(drumBeats_cat4)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter+24, counter+32)
    
for counter in range(len(drumBeats_cat5)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter+32, counter+40)

for counter in range(len(drumBeats_cat6)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter+40, counter+48)

for counter in range(len(drumBeats_cat7)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter+48, counter+56)

for counter in range(len(drumBeats_cat8)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    fitMedia(snare4, 4, counter+56, counter+64)

# =========================================================
for counter in range(len(drumBeats_bean1)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter, drumBeats_bean1[counter])
    
for counter in range(len(drumBeats_bean2)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter+8, drumBeats_bean2[counter])

for counter in range(len(drumBeats_bean3)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter+16, drumBeats_bean3[counter])

for counter in range(len(drumBeats_bean4)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter+24, drumBeats_bean4[counter])
    
for counter in range(len(drumBeats_bean5)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter+32, drumBeats_bean5[counter])

for counter in range(len(drumBeats_bean6)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter+40, drumBeats_bean6[counter])

for counter in range(len(drumBeats_bean7)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter+48, drumBeats_bean7[counter])

for counter in range(len(drumBeats_bean8)): #use the first row to demonstrate making a beat using the first list in the myImage variable
    makeBeat(snare5, 5, counter+56, drumBeats_bean8[counter])

# set fade in and fade out for the whole music
setEffect(0, VOLUME, GAIN, -60, 1, 0, 8)   # fade in
setEffect(0, VOLUME, GAIN, 0, 9, 12, 56)  # crescendo
setEffect(0, VOLUME, GAIN, 12, 57, 0, 60)  # begin fade out
setEffect(0, VOLUME, GAIN, 0, 60, -60, 65) # end of fade out

#set effect
for measure in range(len(numberWave_garlic)):
    rate = (numberWave_garlic[measure]*(12.0)/(255.0))
    if (measure == 63):
        rate_next = 0
    elif(measure%5 == 0):
        rate_next = (numberWave_garlic[measure+1]*(12.0)/(255.0))*(-1.0)
    else:
        rate_next = (numberWave_garlic[measure+1]*(12.0)/(255.0))
    setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, rate, measure, rate_next, measure+1)
    #setEffect(1, CHORUS, CHORUS_RATE, (numberWave_garlic[measure]*16/255))
 
#set effect
for measure in range(len(numberWave_cat)):
    rate = (numberWave_cat[measure]*(12.0)/(255.0))
    if (measure == 63):
        rate_next = 0
    elif(measure%4 == 0):
        rate_next = (numberWave_cat[measure+1]*(12.0)/(255.0))*(-1.0) - 4.0
    else:
        rate_next = (numberWave_cat[measure+1]*(12.0)/(255.0)) - 4.0
    setEffect(4, VOLUME, GAIN, rate, measure, rate_next, measure+1)
    
#use the record music
fitMedia( snare6, 6, 1, 64)
for measure in range(len(numberWave_cat)):
    rate = (numberWave_cat[measure]*(16.0)/(255.0))
    if (measure == 63):
        rate_next = 0
    elif(measure%5 == 0):
        rate_next = (numberWave_cat[measure+1]*(16.0)/(255.0))*(-1.0)
    else:
        rate_next = (numberWave_cat[measure+1]*(16.0)/(255.0))
    setEffect(6, CHORUS, CHORUS_RATE, rate, measure, rate_next, measure+1)
    
finish()