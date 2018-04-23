

class Space():
    def __init__(self, num):
        self.value = num
        self.north = False
        self.south = False
        self.west = False
        self.east = False
        self.object = "null"
        self.printValue = "U"
        self.key = False
        self.damage = 0
        self.health = 0

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health

    def getDMG(self):
        return self.damage

    def setDMG(self, dmg):
        self.damage = dmg

    def getKey(self):
        return self.key

    def setKey(self):
        self.key = True

    def setPrintValue(self, value):
        self.printValue = value

    def getPrintValue(self):
        return self.printValue

    def getNum(self):
        return self.value

    def setPaths(self, paths):
        if paths[0] == "N":
            self.north = True
        if paths[1] == "S":
            self.south = True
        if paths[2] == "W":
            self.west = True
        if paths[3] == "E":
            self.east = True

    def getDir(self):
        directions = [False, False, False, False]
        if self.north == True:
            directions[0] = True
        if self.south == True:
            directions[1] = True
        if self.west == True:
            directions[2] = True
        if self.east == True:
            directions[3] = True
        return directions

    def getPaths(self):
        andFlag = False
        string = "I see paths to the"
        if self.north == True:
            string += " North,"
        if self.south == True:
            string += " South,"
        if self.west == True:
            string += " West,"
        if self.east == True:
            string += " East"
        string += "."
        return string

    def setObject(self, object):
        self.object = object

    def getObject(self):
        return self.object

def __main__():
    print("Main Space Here")


__main__()
