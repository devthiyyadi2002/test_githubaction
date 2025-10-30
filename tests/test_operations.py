from src.math_operations import add,sub


def test_add():
    assert add(2,3) == 5 # assert statment checks if the function outputs the value if yes it gives True 
    assert add(-1,1) == 0 

def test_sub():
    assert sub(5,4) == 1
    assert sub(8,4) == 4
    assert sub(7,4) == 3
    assert sub(4,4) == 0