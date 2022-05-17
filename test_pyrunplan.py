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
        assert PyRunPlan.planLength

    def test_canSetPlanLength(self, rp):
        rp.planLength = 4
        assert rp.planLength == 4

    def test_hasPlan(self, rp):
        assert PyRunPlan.plan
    
    def test_lengthOfPlanIsPlanLength(self, rp):
        rp.planLength = 5
        rp.calculate()
        assert len(rp.plan) == 5

    def test_hasStartMinutes(self, rp):
        assert PyRunPlan.startMinutes

    def test_canSetStartMinutes(self, rp):
        rp.startMinutes = 240
        assert rp.startMinutes == 240

    def test_canGetWeekOne(self, rp):
        rp.planLength = 1
        rp.calculate()
        assert rp.week(0) == {'totalMinutes': rp.startMinutes}

    def test_weekZeroTotalMinutesAfterCalculateIsStartMinutes(self, rp):
        rp.startMinutes = 30
        rp.minMinutes = 15
        rp.calculate()
        assert rp.week(0).get("totalMinutes") == rp.startMinutes
    
    def test_weekThreeTotalMinutesAfterCalculateIsStartMinutes(self, rp):
        rp.startMinutes = 30
        rp.minMinutes = 15
        rp.buildFactor = 1.1
        rp.calculate()
        expectedMinutes = int(rp.startMinutes * rp.buildFactor * rp.buildFactor * rp.buildFactor)
        assert rp.week(3).get("totalMinutes") == expectedMinutes

    def test_hasBuildFactor(self, rp):
        assert PyRunPlan.buildFactor
    
    def test_weekOneTotalMinutesAfterCalculateIsOneHundredTwentyPercentOfWeekZero(self, rp):
        rp.startMinutes = 30
        rp.minMinutes = 15
        rp.buildFactor = 1.2
        rp.calculate()
        expectedMinutes = int(rp.startMinutes * rp.buildFactor)
        assert rp.week(1).get("totalMinutes") == expectedMinutes

    def test_hasMinimumMinutes(self, rp):
        assert PyRunPlan.minMinutes

    
    def test_totalMinutesIsNeverLessThanMinMinutes(self, rp):
        rp.minMinutes = 180
        rp.startMinutes = 240
        rp.calculate()
        for x in range(rp.planLength):
            assert rp.week(x).get("totalMinutes") >= rp.minMinutes
    
    def test_whenTotalMinutesIsLessThanMinMinutesTotalMinutesIsSetToMinMinutes(self, rp):
        rp.minMinutes = 300
        rp.startMinutes = 100
        rp.calculate()
        assert rp.week(0).get("totalMinutes") == rp.minMinutes

    def test_hasMaximumMinutes(self, rp):
        assert PyRunPlan.maxMinutes

    def test_totalMinutesIsCappedAtMaxMinutes(self, rp):
        rp.maxMinutes = 800
        rp.startMinutes = 900
        rp.calculate()
        assert rp.week(0).get("totalMinutes") == rp.maxMinutes

    def test_hasBlockSize(self, rp):
        assert PyRunPlan.blockSize
