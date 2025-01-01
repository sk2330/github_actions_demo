from src.math_ops import add,sub

def test_add():
    assert add(1,2) == 3
    assert add(5,6) == 11
    assert add(2, 3) == 5

def test_sub():
    assert sub(1, 2) == -1
    assert sub(5, 6) == -1
    assert sub(6, 5) == 1
    assert sub(5, 5) == 0