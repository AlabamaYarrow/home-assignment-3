# -*- coding: utf-8 -*-

import unittest
import calc


class CalculatorAddTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, calc.add(1, 2))

    def test_add_float(self):
        self.assertEqual(2.6, calc.add(1.5, 1.1))

    def test_add_negative(self):
        self.assertEqual(0, calc.add(1, -1))

    def test_add_commutative(self):
        self.assertEqual(calc.add(2, 1), calc.add(1, 2))

    def test_add_associative(self):
        self.assertEqual(calc.add(2, calc.add(3, 4)), calc.add(calc.add(2, 3), 4))

    def test_add_string(self):
        self.assertEqual('Invalid input', calc.add(1, '1'))

    def test_add_string_2(self):
        self.assertEqual('Invalid input', calc.add('1', 1))

    def test_add2(self):
        self.assertEqual(0.3, calc.add(0.1, 0.2))


class CalculatorSubTestCase(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(1, calc.sub(3, 2))

    def test_sub_float(self):
        self.assertEqual(1.1, calc.sub(3.2, 2.1))

    def test_sub_zero(self):  # Subzero!
        self.assertEqual(1, calc.sub(1, 0))

    def test_sub_negative(self):
        self.assertEqual(5, calc.sub(3, -2))

    def test_sub_string(self):
        self.assertEqual('Invalid input', calc.sub(1, '1'))

    def test_sub_string_2(self):
        self.assertEqual('Invalid input', calc.sub('1', 1))

    def test_sub2(self):
        self.assertEqual(0.2, calc.sub(0.3, 0.1))


class CalculatorMulTestCase(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(12, calc.mult(3, 4))

    def test_mul_float(self):
        self.assertEqual(6.25, calc.mult(2.5, 2.5))

    def test_mul_commutative(self):
        self.assertEqual(calc.mult(2, 1), calc.mult(1, 2))

    def test_mul_associative(self):
        self.assertEqual(calc.mult(2, calc.mult(3, 4)), calc.mult(calc.mult(2, 3), 4))

    def test_mul_negative(self):
        self.assertEqual(-1, calc.mult(1, -1))

    def test_mul_double_negative(self):
        self.assertEqual(1, calc.mult(-1, -1))

    def test_mul_string(self):
        self.assertEqual('Invalid input', calc.mult(1, '1'))

    def test_mul_string_2(self):
        self.assertEqual('Invalid input', calc.mult('1', 1))

    def test_mul2(self):
        self.assertEqual(1.2, calc.mult(12, 0.1))


class CalculatorDivideTestCase(unittest.TestCase):
    def test_div(self):
        self.assertEqual(3, calc.divide(6, 2))

    def test_div_float(self):
        self.assertEqual(1.5, calc.divide(2.25, 1.5))

    def test_div_negative(self):
        self.assertEqual(-1, calc.divide(-1, 1))

    def test_div_double_negative(self):
        self.assertEqual(1, calc.mult(-1, -1))

    def test_div_zero(self):
        self.assertEqual('Invalid input', calc.divide(1, 0))

    def test_div_string(self):
        self.assertEqual('Invalid input', calc.divide(1, '1'))

    def test_div_string_2(self):
        self.assertEqual('Invalid input', calc.divide('1', 1))

    def test_div2(self):
        self.assertEqual(3, calc.divide(0.3, 0.1))

    def test_div3(self):
        self.assertNotEqual(4, calc.divide(53, 12))


class CalculatorRootTestCase(unittest.TestCase):
    def test_root(self):
        self.assertEqual(3, calc.root(27, 3))

    def test_root_negative(self):
        self.assertEqual(-3, calc.root(-27, 3))

    def test_root_negative_even(self):
        self.assertEqual('Invalid input', calc.root(-27, 2))

    def test_root_float_y(self):
        self.assertEqual('Invalid input', calc.root(27, 3.5))

    def test_root_zero_y(self):
        self.assertEqual('Invalid input', calc.root(1, 0))

    def test_root_zero_x(self):
        self.assertEqual(0, calc.root(0, 1))

    def test_float_root_exact(self):
        self.assertEquals(2.5, calc.root(6.25, 2))

    def test_float_root_almost(self):
        self.assertAlmostEquals(2.2360679775, calc.root(5, 2), places=5)

    def test_root_string(self):
        self.assertEqual('Invalid input', calc.root(1, '1'))

    def test_root_string_2(self):
        self.assertEqual('Invalid input', calc.root('1', 1))