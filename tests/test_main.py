import pytest
from vicsek.vicsek_bad import VicsekModel
from pathlib import Path



def test_main():
  assert(True)



@pytest.mark.parametrize("figname", ['test'])
def test_run(figname):
  vicsek_model = VicsekModel(n=200, d=0.01, v=0.01, dt=1, eta=0.1)
  vicsek_model.run(figname)
  file = Path(figname+".png")
  assert(file.exists)
  file_size = file.stat().st_size
  assert(file_size > 0)


