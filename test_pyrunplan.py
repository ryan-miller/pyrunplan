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
