scenario = int(input("Choose the following RHR scenario that applies to you. (Type either 1, 2, or 3 in response)\n1. You have both v and B, but no F.\n2. You have both v and F, but no B.\n3. You have both B and F, but no v.\n"))
while (scenario != 1) and (scenario != 2) and (scenario != 3):
    print("Please try again. Valid inputs only - 1, 2, or 3. Thank you.\n")
    scenario = int(input("Choose the following RHR scenario that applies to you. (Type either 1, 2, or 3 in response)\n1. You have both v and B, but no F.\n2. You have both v and F, but no B.\n3. You have both B and F, but no v.\n"))
print("Thank you for choosing a RHR scenario.\n")

ionType = int(input("Next, choose what type of ion is undergoing magnetic force. (Type either 1 or 2 in response)\n1. A positive one (+)\n2. A negative one (-)\n"))

while (ionType != 1) and (ionType != 2):
    print("Please try again. Valid inputs only - 1 or 2. Thank you.\n")
    ionType = int(input("Next, choose what type of ion is undergoing magnetic force. (Type either 1 or 2 in response)\n1. A positive proton (+)\n2. A negative electron (-)\n"))
print("Thank you for choosing an ion type.\n")


dirToCoords = {
    "up": (0,1,0),
    "down":(0,-1,0),
    "right":(1,0,0),
    "left": (-1,0,0),
    "in": (0,0,-1),
    "out": (0,0,1)
}

coordsToDir = {
    (0,1,0): "up",
    (0,-1,0): "down",
    (1,0,0): "right",
    (-1,0,0): "left",
    (0,0,-1): "in",
    (0,0,1): "out"
}

dirPoss = ["up","down","right","left","in","out"]

#RHR - v = fingers, B = palm, F = thumb
print("\nNOTE:\nUp represents positive y direction.\nDown represents negative y direction.\nRight represents positive x direction.\nLeft represents negative x direction.\nIn represents negative z direction.\nOut represents positive z direction.\n")
if(scenario == 1):
    print("\nYou chose Scenario 1.\nYou have both v and B, but no F.\n")
    v = float(input("Type in the magnitude of v.\n"))
    vDir = (input("Type in the direction of v.\nType either (up, down, right,left,in,out) in carefully.\n")).lower()
    while vDir not in dirPoss:  
        vDir = (input("Type in the direction of v.\nType either (up, down, right,left,in,out) in carefully.\n")).lower()
    
    B = float(input("Type in the magnitude of B\n"))
    bDir = (input("Type in the direction of B.\nType it in carefully.\n")).lower()
    while bDir not in dirPoss:  
        bDir = (input("Type in the direction of B.\nType either (up, down, right,left,in,out) in carefully.\n")).lower()

    print("\nThe direction of the missing F must be: ")
    vDirConverted = dirToCoords[vDir]
    bDirConverted = dirToCoords[bDir]

    fX = (vDirConverted[1]*bDirConverted[2]) - (vDirConverted[2]*bDirConverted[1])
    fY = (vDirConverted[2]*bDirConverted[0]) - (vDirConverted[0]*bDirConverted[2])
    fZ = (vDirConverted[0]*bDirConverted[1]) - (vDirConverted[1]*bDirConverted[0])
    
    if(ionType == 1):
        print(coordsToDir[(fX, fY, fZ)])
    else:
        print(coordsToDir[(-1 * fX, -1 * fY, -1 * fZ)])
    
    print("\nThe magnitude of the missing F must be: ")
    #F = q * v * B *sin(theta)
    #theta is perpendicular so sin(90) = 1 so disregard that part
    q = 1.6*(10**(-19))
    # print(q, v, B)
    
    print("\nThe magnitude of F is:\n")
    print(abs(q * v * B))

elif scenario == 2:
    print("\nYou chose Scenario 2.\nYou have both v and F, but no B.\n")
    
    v = float(input("Type in the magnitude of v.\nType it in carefully.\n"))
    vDir = input("Type in the direction of v.\nType it in carefully.\n")
    while vDir not in dirPoss:  
        vDir = (input("Type in the direction of v.\nType either (up, down, right,left,in,out) in carefully.\n")).lower()

    F = float(input("Type in the magnitude of F.\nType it in carefully.\n"))
    fDir = input("Type in the direction of F.\nType it in carefully.\n")
    while fDir not in dirPoss:  
        fDir = (input("Type in the direction of F.\nType either (up, down, right,left,in,out) in carefully.\n")).lower()

    print("\nThe direction of the missing B must be: ")
    vDirConverted = dirToCoords[vDir]
    fDirConverted = dirToCoords[fDir]

    bX = (vDirConverted[1]*fDirConverted[2]) - (vDirConverted[2]*fDirConverted[1])
    bY = (vDirConverted[2]*fDirConverted[0]) - (vDirConverted[0]*fDirConverted[2])
    bZ = (vDirConverted[0]*fDirConverted[1]) - (vDirConverted[1]*fDirConverted[0])

    if(ionType == 2):
        print(coordsToDir[(bX, bY, bZ)])
    else:
        print(coordsToDir[(-1 * bX, -1 * bY, -1 * bZ)])

    q = 1.6*(10**(-19))
    # print(F, q, v)
    print("\nThe magnitude of B is:\n")
    print(abs(F / (q * v)))

elif scenario == 3:
    print("\nYou chose Scenario 3.\nYou have both B and F, but no v.\n")
    
    B = float(input("Type in the magnitude of B.\nType it in carefully.\n"))
    bDir = input("Type in the direction of B.\nType it in carefully.\n")
    while bDir not in dirPoss:  
        bDir = (input("Type in the direction of B.\nType either (up, down, right,left,in,out) in carefully.\n")).lower()

    F = float(input("Type in the magnitude of F.\nType it in carefully.\n"))
    fDir = input("Type in the direction of F.\nType it in carefully.\n")
    while fDir not in dirPoss:  
        fDir = (input("Type in the direction of F.\nType either (up, down, right,left,in,out) in carefully.\n")).lower()

    print("\nThe direction of the missing v must be: ")
    bDirConverted = dirToCoords[bDir]
    fDirConverted = dirToCoords[fDir]

    vX = (bDirConverted[1]*fDirConverted[2]) - (bDirConverted[2]*fDirConverted[1])
    vY = (bDirConverted[2]*fDirConverted[0]) - (bDirConverted[0]*fDirConverted[2])
    vZ = (bDirConverted[0]*fDirConverted[1]) - (bDirConverted[1]*fDirConverted[0])

    if(ionType == 1):
        print(coordsToDir[(vX, vY, vZ)])
    else:
        print(coordsToDir[(-1 * vX, -1 * vY, -1 * vZ)])

    q = 1.6*(10**(-19))
    # print(F, q, v)
    print("\nThe magnitude of v is:\n")
    print(abs(F / (q * B)))

else:
    #shouldn't be able to access this but just in case
    print("\nCongrats, you shouldn't be able to access this, but somehow you did!\n")