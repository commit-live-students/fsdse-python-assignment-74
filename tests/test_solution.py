from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        res = solution()
        list_res = list(res)
        res3 = list_res[:]
        res3.sort()

        self.assertEqual(res.shape, (10,))
        self.assertEqual(list_res, res3)

