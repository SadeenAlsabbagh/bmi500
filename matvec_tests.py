# generate tests for matrix-vector-product function in matvec_multiply.py

# generate tests for dot-product function in matvec_multiply.py

import unittest

from matvec_multiply import dot_product, matrix_vector_product


class TestDotProduct(unittest.TestCase):

    def test_basic_dot_product(self):
        self.assertEqual(dot_product([1, 2, 3], [4, 5, 6]), 32)

    def test_negative_values(self):
        self.assertEqual(dot_product([-1, 2], [3, -4]), -11)

    def test_float_values(self):
        self.assertAlmostEqual(
            dot_product([1.5, 2.0], [2.0, 3.0]),
            9.0
        )

    def test_different_lengths(self):
        with self.assertRaises(ValueError):
            dot_product([1, 2], [1, 2, 3])

    def test_empty_vectors(self):
        with self.assertRaises(ValueError):
            dot_product([], [])

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            dot_product([1, "a"], [2, 3])


class TestMatrixVectorProduct(unittest.TestCase):

    def test_basic_matrix_vector_product(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        vector = [5, 6]

        self.assertEqual(
            matrix_vector_product(matrix, vector),
            [17, 39]
        )

    def test_identity_matrix(self):
        matrix = [
            [1, 0],
            [0, 1]
        ]
        vector = [7, 8]

        self.assertEqual(
            matrix_vector_product(matrix, vector),
            [7, 8]
        )

    def test_dimension_mismatch(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        vector = [1, 2]

        with self.assertRaises(ValueError):
            matrix_vector_product(matrix, vector)

    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            matrix_vector_product([], [1, 2])

    def test_non_list_matrix(self):
        with self.assertRaises(TypeError):
            matrix_vector_product("not a matrix", [1, 2])

    def test_non_numeric_matrix_value(self):
        matrix = [
            [1, 2],
            [3, "x"]
        ]

        with self.assertRaises(TypeError):
            matrix_vector_product(matrix, [1, 2])


if __name__ == "__main__":
    unittest.main()
