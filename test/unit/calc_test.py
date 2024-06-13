import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    #Methods return correct results
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(-4, self.calc.add(-2, -2))
        self.assertEqual(1, self.calc.add(1, 0))
        
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.substract(2, 1))
        self.assertEqual(-1, self.calc.substract(1, 2))
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(0, self.calc.substract(-2, -2))
        self.assertEqual(1, self.calc.substract(1, 0))
        
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(-1.5, self.calc.divide(-3, 2))
        self.assertEqual(-1.5, self.calc.divide(3, -2))
        self.assertEqual(1.5, self.calc.divide(-3, -2))
        self.assertEqual(0, self.calc.divide(0, 2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(0, self.calc.power(0, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(-8, self.calc.power(-2, 3))
        self.assertEqual(0.125, self.calc.power(2, -3))
        self.assertEqual(-0.125, self.calc.power(-2, -3))


    def test_square_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.square(0))
        self.assertEqual(5, self.calc.square(25))

    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.logarithm(1))
        self.assertEqual(1, self.calc.logarithm(10))
    
    #Methods fail with nan par
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
        
    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())
        
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())
        
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
    
    def test_square_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.square, "25")
        self.assertRaises(TypeError, self.calc.square, None)
        self.assertRaises(TypeError, self.calc.square, object())
    
    def test_logarithm_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.logarithm, "10")
        self.assertRaises(TypeError, self.calc.logarithm, None)
        self.assertRaises(TypeError, self.calc.logarithm, object())


    #Methods fail with more par
    def test_add_method_fails_with_more_pars(self):
        self.assertRaises(TypeError, self.calc.add, 2, 2, 1)
    
    def test_substract_method_fails_with_more_pars(self):
        self.assertRaises(TypeError, self.calc.substract, 2, 2, 1)
    
    def test_multiply_method_fails_with_more_pars(self):
        self.assertRaises(TypeError, self.calc.multiply, 2, 2, 1)
    
    def test_divide_method_fails_with_more_pars(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 2, 1)
    
    def test_power_method_fails_with_more_pars(self):
        self.assertRaises(TypeError, self.calc.power, 2, 2, 1)
    
    def test_square_method_fails_with_more_pars(self):
        self.assertRaises(TypeError, self.calc.square, 2, 2,)
        
    def test_logarithm_method_fails_with_more_pars(self):
        self.assertRaises(TypeError, self.calc.logarithm, 2, 2,)
        

    #Methods fail with zero par
    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)
    
    def test_logarithm_method_fails_with_zero(self):
        self.assertRaises(TypeError, self.calc.logarithm, 0)
        self.assertRaises(TypeError, self.calc.logarithm, -0)
        self.assertRaises(TypeError, self.calc.logarithm, "0")
        
    #Methods fail with negative par
    def test_square_method_fails_with_negative(self):
        self.assertRaises(TypeError, self.calc.square, -1)
        self.assertRaises(TypeError, self.calc.square, "-1")
    
    
    def test_logarithm_method_fails_with_negative(self):
        self.assertRaises(TypeError, self.calc.logarithm, -1)
        self.assertRaises(TypeError, self.calc.logarithm, "-1")
    


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
