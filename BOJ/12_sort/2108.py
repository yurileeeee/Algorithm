# BOJ 2108 통계학
# https://www.acmicpc.net/problem/2108

import sys 
from collections import Counter

t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))
    
def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2] 
    return mid

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]: # 최빈값이 2개 이상일 때
            mod = modes[1][0] # 두번째로 작은 값
        else : 
            mod = modes[0][0] 
    else : 
        mod = modes[0][0] # 최빈값의 개수가 1개이면 맨 첫번째 수

    return mod
        
def scope(nums):
    return max(nums) - min(nums)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))