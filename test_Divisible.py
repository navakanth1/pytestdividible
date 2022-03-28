import Divisible
import pytest
@pytest.fixture()
def input():
    x = 15
    return x

def testdivisibleby5(input):

    result = Divisible.divisibleby5(input)
    assert result == True


def testdivisibleby7(input):

    result = Divisible.divisibleby7(input)
    assert result == False


def testdivisibleby9(input):

    result = Divisible.divisibleby9(input)
    assert result == False

def testdivisibleby10(input):

    result = Divisible.divisibleby10(input)
    assert result == False
