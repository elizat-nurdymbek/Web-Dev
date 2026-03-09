N = int(input())
count = 0

for _ in range(N):
    x = int(input())
    if x == 0:
        count += 1

print(count)