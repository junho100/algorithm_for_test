po = [0]*(10000001)
ne = [0]*(10000001)

N = int(input())
cards = list(map(int, input().split()))

for i in range(N):
    if cards[i] < 0:
        ne[-cards[i]] += 1
    else:
        po[cards[i]] += 1

M = int(input())
nums = list(map(int, input().split()))

for i in range(M):
    if nums[i] < 0:
        print(ne[-nums[i]], end = " ")
    else:
        print(po[nums[i]], end = " ")