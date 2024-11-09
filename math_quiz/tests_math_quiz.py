import unittest
from math_quiz import randNumGenerator, randOperator, arithmeticOp


class TestMathGame(unittest.TestCase):

    def test_randNumGenerator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randNumGenerator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randOperator(self):
        # check if generated operators are addition, subtraction or multiplication 
        for _ in range(1000):
            rand_op = randOperator()
            self.assertTrue(rand_op in ['+','-','*'])

    def test_arithmeticOp(self):
        # run various test cases for the arithmeticOp function
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 5, '-', '3 - 5', -2),
                (4, 6, '+', '4 + 6', 10),
                (9, 1, '-', '9 - 1', 8),
                (4, 9, '*', '4 * 9', 36)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                self.assertTrue(arithmeticOp(num1, num2, operator) == (expected_problem, expected_answer))

if __name__ == "__main__":
    unittest.main()
