# coding=utf-8

# import pytest
import sys
sys.path.append("..")
import calculator.calculator


class TestCalculator:
    def test_pluse_1(self):
        assert 5 == calculator.calculator.plus(1, 4)

    def test_minus(self):
        assert 2 == calculator.calculator.minus(5, 3)

    def test_pluse_2(self):
        assert 3!= calculator.calculator.plus(1, 1)
