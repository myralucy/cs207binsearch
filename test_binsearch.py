from pytest import raises
from binsearch import binary_search
import numpy as np

def test_inf():
    assert binary_search([1,2,np.inf], 2) == 1

def test_inf_2():
    assert binary_search([1,2,np.inf], np.inf) == 2

def test_no_exit_1():
    assert binary_search([5], 4) == -1

def test_no_exit_2():
    assert binary_search([range(10)], -1) == -1

def test_no_exit_3():
    assert binary_search([range(10)], 3.5) == -1

def test_no_exit_4():
    assert binary_search([range(10)], 5, 6, 9) == -1

def test_no_exit_5():
    assert binary_search([range(10)], 1, 2, 8) == -1

def test_multiple():
    assert binary_search([1, 2, 2, 3, 3], 2) == 1

def test_multiple_2():
    assert binary_search([1, 1, 2, 3, 3], 1) == 0

def test_border_1():
    assert binary_search([0, 1, 2, 3, 3], 0) == 0

def test_border_2():
    assert binary_search([0, 1, 2, 3, 8], 8) == 4
