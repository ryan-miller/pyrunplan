class PyRunPlan:

    def __init__(self):
        self._planLength = 0
        self._plan = list()

    @property
    def plan(self):
        return self._plan

    @property
    def planLength(self):
        return self._planLength
    @planLength.setter
    def planLength(self, value):
        self._planLength = value

    def calculate(self):

        for x in range(self.planLength):
            print(x)
            self.plan.append(list())

        return self.plan