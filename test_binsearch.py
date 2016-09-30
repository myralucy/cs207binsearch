from pytest import raises
from binsearch import binary_search
import numpy as np

def test_inf():
	assert binary_search([1,2,np.inf], 2) == 1

