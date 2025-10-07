'''def min_max(nums):
    if len(nums) == 0:
        return ('ValueError')
    else:
        return ((min(nums), max(nums)))

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))


def unique_sorted(nums):
    nums.sort()
    return [*set(nums)]

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))'''

def flatten(mat):
    answer = []
    for arr in mat:
        if type(arr) == str:
            return ('TypeError')
        else:
            for member in arr:
                answer.append(member)
    return answer

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))