import pytest
from vasim import instrument

who22 = instrument.get_who2022()


# run function tests
def test_get_who2022():
    assert len(who22) == 2

# check each is a data frame

# check col names of survey

# check col names of choices
