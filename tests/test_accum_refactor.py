import pytest

from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

@pytest.mark.accumulator
def test_accumulator_init(accum): # <-- dependency injection (fixture looks at the function's parameters' list)
    # accum = Accumulator()  # no need for this after using fixture
    assert accum.count == 0

@pytest.mark.accumulator
def test_accumulator_add_one(accum, accum2):  # a test case can have multiple fixture (just make sure each fixture has unique name)
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10