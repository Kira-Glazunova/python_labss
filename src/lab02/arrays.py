def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return "ValueError"
    else:
        return (min(nums), max(nums))


print(min_max([10, 3, -100, 9, 2]))
print(min_max([10]))
print(min_max([-1, -11, -2]))
print(min_max([]))
print(min_max([1.4, -8.4, 5, 6.66]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums.sort()
    return [*set(nums)]


print(unique_sorted([5, 1, 1, 2, 5]))
print(unique_sorted([]))
print(unique_sorted([-2, 0, -342, -2, 10]))
print(unique_sorted([1.3, 1.2, 0, -4.5]))


def flatten(mat: list[list | tuple]) -> list:
    answer = []
    for arr in mat:
        if type(arr) == str:
            return "TypeError"
        else:
            for member in arr:
                answer.append(member)
    return answer


print(flatten([[10, 2], [1, 5]]))
print(flatten([[10, 24], (11, 1, 5)]))
print(flatten([[], [23], [1, 2]]))
print(flatten(["sfggd", [10, 11, 120]]))
