import unittest
from app.calculator import Calculator

class TDDPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_calculator_add_method_returns_correct_value(self):
        result = self.calc.add(2,2)
        self.assertEqual(4,result)
    
    def test_calculator_add_error_message_if_both_args_are_not_numbers(self):
        self.assertRaises(ValueError,self.calc.add, 'one', 'two')
        
    def test_calculator_subtract_method_returns_correct_value(self):
        result = self.calc.subtract(4,2)
        self.assertEqual(2, result)
    
    def test_calculator_subtract_error_message_if_both_args_are_not_numbers(self):
        self.assertRaises(ValueError,self.calc.subtract, 'one', 'two')

if __name__ == '__main__':
    unittest.main()