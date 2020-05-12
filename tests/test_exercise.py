import pytest
from src.exercise import sum_list

def test_exercise(capsys):
    numbers = [1,3,10,-1,5,0]
    assert sum_list(numbers) == 18
