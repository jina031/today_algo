import sys
sys.stdin = open('input.txt')

# map int 안하면 아마 기본적으로 char로~
a,b = map(int, input().split())
print(a,b)

