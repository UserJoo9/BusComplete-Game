class BusComplete:
    totalScore = 0
    def __init__(self):
        self.__MasterLitter = ''
        self.__boyNAme = ''
        self.__girlName = ''
        self.__plantName = ''
        self.__inanimate = ''
        self.__animalName = ''
        self.__country = ''
        self.__score = 0


    def setMasterLitter(self, newMAsterLitter):
        self.__MasterLitter = newMAsterLitter

    def getMasterLitter(self):
        return self.__MasterLitter

    def setBoyName(self, newBoyName):
        self.__boyNAme = newBoyName

    def getBoyName(self):
        return self.__boyNAme

    def setGirlName(self, newGirlName):
        self.__girlName = newGirlName

    def getGirlName(self):
        return self.__girlName

    def setPlaneName(self, newPlant):
        self.__plantName = newPlant

    def getPlant(self):
        return self.__plantName

    def setInanimate(self, newInanimate):
        self.__inanimate = newInanimate

    def getInanimate(self):
        return self.__inanimate

    def setAnimal(self, newAnimal):
        self.__animalName = newAnimal

    def getAnimal(self):
        return self.__animalName

    def setCountry(self, newCountry):
        self.__country = newCountry

    def getCountry(self):
        return self.__country

    def setScore(self, newScore):
        self.__score = newScore

    def getScore(self):
        return self.__score

    def setTotalScore(self, newTotalScore):
        self.totalScore = newTotalScore

    def getTotalScore(self):
        return self.totalScore

    def Revision(self):
        sum = 0

        if self.getBoyName().startswith(self.getMasterLitter()):
            sum += 10
        if self.getGirlName().startswith(self.getMasterLitter()):
            sum += 10
        if self.getPlant().startswith(self.getMasterLitter()):
            sum += 10
        if self.getInanimate().startswith(self.getMasterLitter()):
            sum += 10
        if self.getAnimal().startswith(self.getMasterLitter()):
            sum += 10
        if self.getCountry().startswith(self.getMasterLitter()):
            sum += 10

        self.setScore(sum)


    # def describe(self):
    #     print("Boy:          ",self.getBoyName())
    #     print("Girl:         ",self.getGirlName())
    #     print("PLant:        ",self.getPlant())
    #     print("Inanimate:    ",self.getInanimate())
    #     print("Animal:       ",self.getAnimal())
    #     print("Country:      ",self.getCountry())

    def sumTotal(self, lastScore):
        ts = self.getTotalScore() + lastScore
        self.setTotalScore(ts)

    def ModifyTotalScoreMinus(self):
        self.totalScore = self.totalScore - 5

    def ModifyTotalScorePlus(self):
        self.totalScore = self.totalScore + 5

    def modifyScoreMinus(self):
        self.setScore(self.getScore()-5)

    def modifyScorePlus(self):
        self.setScore(self.getScore()+5)


