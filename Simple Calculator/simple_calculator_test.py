import Simple_Calculator_part1 as calculator

def test_add():
    assert calculator.add(0,0) == 0
    assert calculator.add(-1,-1) == -2
    assert calculator.add(4,5) == 9
    assert calculator.add(1,2,3,4) == 10

def test_multiply():
    assert calculator.multiply(1,2) == 2 
    assert calculator.multiply(1,2,3,4) == 24
        