class PyRunPlan:

    def __init__(self):
        self._planLength = 4
        self._plan = list()
        self._startMinutes = 0
        self._buildFactor = 1.1
        self._minMinutes = 60
        self._maxMinutes = 600

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

    def calculate(self):

        if self.startMinutes < self.minMinutes:
            minutes = self.minMinutes
        else:
            minutes = self.startMinutes

        for x in range(self.planLength):

            if x > 0:
                minutes = minutes * self.buildFactor
                
            if minutes > self.maxMinutes:
                minutes = self.maxMinutes
                
            weekDetails = dict()
            weekDetails["totalMinutes"] = int(minutes)
            self.plan.append(weekDetails)

        return self.plan

    def week(self, value):

        return self.plan[value]
