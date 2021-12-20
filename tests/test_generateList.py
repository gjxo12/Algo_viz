import pytest
from Algoviz.Algo import GenerateList


@pytest.mark.parametrize("input1, input2,input3", [
    (50, 0, 100),
])
def test_generatelist(input1, input2, input3):
    # assert GenerateList(10,1,100) is type(list)
    assert GenerateList(input1, input2, input3) is 10
