import unittest
from exptree import *

class TestExpressionTree(unittest.TestCase):
    def test_init(self):
        expTree = ExpressionTree("(a/(b-3))")

    def test_evaluate(self):
        expTree = ExpressionTree("(a/(b-3))")
        vars = {'a' : 9, 'b' : 12}
        self.assertEqual(expTree.evaluate(vars), 1.0)

    def test_computeOp(self):
        self.assertEqual(computeOp(1, "+", 1), 2)

    def test_str(self):
        expTree = ExpressionTree("(a/(b-3))")
        print(expTree)


if __name__ == '__main__':
    unittest.main()
