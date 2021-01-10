import pytest
from math import sqrt

def isprime(n):

    if n <= 1:
        return False

    for i in range(2, int(sqrt(n))):
        if n%i == 0:
            return False
    return True

#Lo siguiente da otorga valores a test y los prueba en isprime

@pytest.mark.parametrize("test", [3,5,7,13,17,51,131,251])
def test_isprime(test):
    assert isprime(test) == True
