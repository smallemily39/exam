# 齿轮
# def SearchTool(tools, start_index, target):
#     target_index = [i for i, x in enumerate(tools) if x == target]
#     print(target_index)
#     steps = []
#     for i in target_index:
#         a = abs(start_index - i)
#         b = len(tools) - a
#         print(a, b)
#         if a > b:
#             steps.append(b)
#         else:
#             steps.append(a)
#     step = min(steps)
#     print(step)
#     return step
#
#
# Tools = ['saw', 'hammer', 'mallet',
#          'file', 'saw', 'ladder', 'scissor']
#
# target = "ladder"
# start_index = 2
#
# SearchTool(Tools, start_index, target)


# 解压
# while True:
#     try:
#         n = int(input())
#         num_list = list(map(int, input().split()))
#         bol = int(input())
#         if bol == 0:
#             print(' '.join(map(str, sorted(num_list))))
#         elif bol == 1:
#             print(' '.join(map(str, sorted(num_list, reverse=True))))
#     except:
#         break

# str_list = list(input())
# n = int(input())
# print(''.join(map(str, str_list[:n])))

from typing import List

# 3sum 找出三个相加为零的list
# class Solution(object):
#     def threeSum(self, nums):
#         ans = []
#         nums.sort()
#
#         for i in range(len(nums)):
#             if nums[i] > 0: break  # after sorting, if the min > 0, we couldn't find such three values
#             if i > 0 and nums[i] == nums[i - 1]:  # ensure that nums[i] is not duplicated
#                 continue
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 if nums[l] + nums[r] > -nums[i]:
#                     r -= 1
#                 elif nums[l] + nums[r] < -nums[i]:
#                     l += 1
#                 else:
#                     ans.append([nums[i], nums[l], nums[r]])
#                     # update l to get a different sum
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#         return ans

# set matrix zeros
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m, n, r_0 = len(matrix), len(matrix[0]), 1
#         if m == 0: return


# groupAnagrams 找出相同letter组成的单词
from collections import defaultdict
import pyart

def groupAnagrams(words: List[str]) -> List[List[str]]:
    anags = defaultdict(list)

    for word in words:
        # 1. list()  - split to indvidual letters:
        # 2. sorted() & join the letters to ONE word as key

        key = "".join(sorted(list(word)))
        print(key)
        anags[key].append(word)

    return list(anags.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))