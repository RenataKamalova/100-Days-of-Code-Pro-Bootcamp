total_sum = 0
for i in range(2, 101, 2):
    if i % 2 == 0:
        print(i)
        total_sum += i

print(total_sum)