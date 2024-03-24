def gain_max_value(nums: list[int], k: int) -> int:
  n = len(nums) - 1 - k
  i = n
  acc = nums[i]

  while i >= 0:
    nums[i] = nums[i] + nums[i + k]
    acc = max(nums[i],acc)
    i = i - 1

  return acc

print(gain_max_value([2, -3, 4, 6, 1], 2))