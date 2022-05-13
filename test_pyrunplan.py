import pytest
from .pyrunplan import PyRunPlan

class Test:

    @pytest.fixture()
    def rp(self):
        rp = PyRunPlan()
        yield rp

    def test_canCallPyRunPlan(self, rp):
        assert type(rp) is PyRunPlan

    def test_hasPlanLength(self, rp):
        assert rp.planLength != None

    def test_canSetPlanLength(self, rp):
        rp.planLength = 4
        assert rp.planLength == 4

    def test_hasPlan(self, rp):
        assert rp.plan != None
    
    def test_lengthOfPlanIsPlanLength(self, rp):
        rp.planLength = 5
        rp.calculate()
        assert len(rp.plan) == 5

    def test_hasStartMinutes(self, rp):
        assert rp.startMinutes != None

    def test_canSetStartMinutes(self, rp):
        rp.startMinutes = 240
        assert rp.startMinutes == 240

    def test_canGetWeekOne(self, rp):
        rp.planLength = 1
        rp.calculate()
        assert rp.week(0) == {'totalMinutes': 0}

    def test_weekZeroTotalMinutesAfterCalculateIsStartMinutes(self, rp):
        rp.startMinutes = 30
        rp.calculate()
        assert rp.week(0).get("totalMinutes") == 30
    
    def test_weekThreeTotalMinutesAfterCalculateIsStartMinutes(self, rp):
        rp.startMinutes = 30
        rp.calculate()
        assert rp.week(3).get("totalMinutes") == 30

    def test_hasBuildFactor(self, rp):
        assert rp.buildFactor != None
    
    def test_weekOneTotalMinutesAfterCalculateIsOneHundredTwentyPercentOfWeekZero(self, rp):
        rp.startMinutes = 30
        rp.buildFactor = 1.2
        rp.calculate()
        assert rp.week(1).get("totalMinutes") == 36
