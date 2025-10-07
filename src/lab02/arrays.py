def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return ('ValueError')
    else:
        return ((min(nums), max(nums)))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums.sort()
    return [*set(nums)]


def flatten(mat: list[list | tuple]) -> list:
    answer = []
    for arr in mat:
        if type(arr) == str:
            return ('TypeError')
        else:
            for member in arr:
                answer.append(member)
    return answer