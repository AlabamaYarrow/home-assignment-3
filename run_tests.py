# -*- coding: utf-8 -*-

import unittest
import sys

from tests import test_calculator

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(test_calculator.CalculatorAddTestCase),
        unittest.makeSuite(test_calculator.CalculatorMulTestCase),
        unittest.makeSuite(test_calculator.CalculatorSubTestCase),
        unittest.makeSuite(test_calculator.CalculatorDivideTestCase),
        unittest.makeSuite(test_calculator.CalculatorRootTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
