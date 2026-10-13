
from simpleint import simple_interest

def test_simple_interest():
    assert simple_interest(1000, 5, 2) == 100

def test_simple_interest2():
    assert simple_interest(2000, 4, 3) == 240
