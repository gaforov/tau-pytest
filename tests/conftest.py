import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

@pytest.fixture
def accum2():
    return Accumulator()