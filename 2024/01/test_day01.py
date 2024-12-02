import pytest
from functions import sortList

unsortedList = list(([5, 2, 0, 1, 3, 4]))
sortedList = list(([0, 1, 2, 3, 4, 5]))

@pytest.mark.parametrize(
  "input, output",
  [
    (unsortedList, sortedList)
  ]
)
def test_sortList(input, output):
  assert sortList(input) == output