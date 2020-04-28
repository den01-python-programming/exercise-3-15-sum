import pytest
from src.exercise import sum

def test_exercise(capsys):
    numbers = [1,3,10,-1,5,0]
    sum(numbers)
    out, err = capsys.readouterr()
    assert out == 18
