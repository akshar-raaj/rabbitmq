import pytest


def test_dummy():
    assert 1 == 1


class TestDummy(object):

    def test_add(self):
        assert 1 + 2 == 3

    def test_sub(self):
        assert 1 - 2 == -1

    @pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (2, 3, 6)])
    def test_mul(self, a, b, expected):
        assert a * b == expected
