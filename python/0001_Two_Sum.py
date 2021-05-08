from typing import List

import pytest


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x_index, x_value in enumerate(nums):
            for y_index, y_value in enumerate(nums[x_index + 1:], start=x_index + 1):
                if x_value + y_value == target:
                    return [x_index, y_index]


@pytest.mark.parametrize('solution', [Solution1])
@pytest.mark.parametrize('test_input, expected', [
    [dict(nums=[2, 7, 9, 11], target=9), [0, 1]],
])
def test(solution, test_input, expected):
    assert solution().twoSum(**test_input) == expected
