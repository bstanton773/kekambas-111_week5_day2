import unittest
from whiteboard import solution
from unittest import TestCase


class TestSearchInsert(TestCase):

    def test_solution(self):
        nums1, target1 = [1, 3, 5, 6], 5
        nums2, target2 = [1, 3, 5, 6], 2
        nums3, target3 = [1, 3, 5, 6], 7
        nums4, target4 = [1, 3, 5, 6], 0

        self.assertEqual(solution(nums1, target1), 2)
        self.assertEqual(solution(nums2, target2), 1)
        self.assertEqual(solution(nums3, target3), 4)
        self.assertEqual(solution(nums4, target4), 0)

    def test_solution_target_found(self):
        nums, target = [1, 3, 5, 6], 3
        self.assertEqual(solution(nums, target), 1)

    def test_solution_target_not_found(self):
        nums, target = [1, 3, 5, 6], 4
        self.assertEqual(solution(nums, target), 2)

    def test_solution_single_element_array(self):
        nums, target = [5], 5
        self.assertEqual(solution(nums, target), 0)

    def test_solution_single_element_array_target_not_found(self):
        nums, target = [5], 3
        self.assertEqual(solution(nums, target), 0)
