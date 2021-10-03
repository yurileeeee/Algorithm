# BOJ 10818 최소, 최대
# https://www.acmicpc.net/problem/10818

num = int(input())
num_list = list(map(int, input().split()))

print('{} {}'.format(min(num_list), max(num_list)))