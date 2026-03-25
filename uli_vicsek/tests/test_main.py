from vicsek.vicsek_bad import VicsekModel
import pytest
import numpy as np


def test_main():
  assert(True)




@pytest.mark.parametrize("lst", [0,3])
def test_search_neighbours(lst):
  vicsek_model=VicsekModel(n=200,d=0.001,v=0.01,dt=1,eta=0.1)
  vicsek_model.search_neighbours(lst)
  assert 0 <= vicsek_model.neighbours < vicsek_model.n

  assert isinstance(vicsek_model.sum_sin, float)
  assert isinstance(vicsek_model.sum_cos, float)
  assert abs(vicsek_model.sum_sin) <= vicsek_model.neighbours
  assert abs(vicsek_model.sum_cos) <= vicsek_model.neighbours