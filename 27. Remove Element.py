from typing import List


def removeElement(nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


if __name__ == '__main__':
    list_of_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    value_to_remove = 2
    print(removeElement(list_of_nums, value_to_remove))
