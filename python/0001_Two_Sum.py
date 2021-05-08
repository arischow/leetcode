from typing import List

import pytest


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x_index = 0
        for x in nums:
            y_index = x_index + 1
            for y in nums[y_index:]:
                if x + y == target:
                    return [x_index, y_index]
                y_index += 1
            x_index += 1


@pytest.mark.parametrize('solution', [Solution1])
@pytest.mark.parametrize('test_input, expected', [
    [dict(nums=[2, 7, 9, 11], target=9), [0, 1]],
    [dict(nums=[3, 2, 4], target=6), [1, 2]],
    [dict(nums=[3, 2, 3], target=6), [0, 2]],
])
def test(solution, test_input, expected):
    assert solution().twoSum(**test_input) == expected
