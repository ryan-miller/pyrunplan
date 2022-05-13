class PyRunPlan:

    def __init__(self):
        self._planLength = 4
        self._plan = list()
        self._startMinutes = 0

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

    def calculate(self):

        for x in range(self.planLength):
            temp = dict()
            temp["totalMinutes"] = self.startMinutes
            self.plan.append(temp)

        return self.plan

    def week(self, value):

        return self.plan[value]
