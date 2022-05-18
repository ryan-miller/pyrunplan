class PyRunPlan:

    def __init__(self):
        self._planLength = 4
        self._plan = list()
        self._startMinutes = 240
        self._buildFactor = 1.2
        self._minMinutes = 240
        self._maxMinutes = 600
        self._blockSize = 4
        self._recoveryFactor = 0.85

    @property
    def plan(self):
        return self._plan

    @property
    def planLength(self):
        return self._planLength
    @planLength.setter
    def planLength(self, value):
        self._planLength = value

    @property
    def startMinutes(self):
        return self._startMinutes
    @startMinutes.setter
    def startMinutes(self, value):
        self._startMinutes = value

    @property
    def buildFactor(self):
        return self._buildFactor
    @buildFactor.setter
    def buildFactor(self, value):
        self._buildFactor = value

    @property
    def minMinutes(self):
        return self._minMinutes
    @minMinutes.setter
    def minMinutes(self, value):
        self._minMinutes = value

    @property
    def maxMinutes(self):
        return self._maxMinutes
    @maxMinutes.setter
    def maxMinutes(self, value):
        self._maxMinutes = value
    
    @property
    def blockSize(self):
        return self._blockSize
    @blockSize.setter
    def blockSize(self, value):
        self._blockSize = value

    @property
    def recoveryFactor(self):
        return self._recoveryFactor
    @recoveryFactor.setter
    def recoveryFactor(self, value):
        self._recoveryFactor = value

    def calculate(self):

        if self.startMinutes < self.minMinutes:
            minutes = self.minMinutes
        elif self.startMinutes > self.maxMinutes:
            minutes = self.maxMinutes
        else:
            minutes = self.startMinutes

        for x in range(self.planLength):

            if x > 0:
                if x % self.blockSize == (self.blockSize - 1):
                    minutes = minutes * self.recoveryFactor
                    if minutes < self.minMinutes:
                        minutes = self.minMinutes
                else:
                    minutes = minutes * self.buildFactor
                    if minutes > self.maxMinutes:
                        minutes = self.maxMinutes

            weekDetails = dict()
            weekDetails["totalMinutes"] = int(minutes)
            self.plan.append(weekDetails)
            print(weekDetails)
        return self.plan

    def week(self, value):

        return self.plan[value]
