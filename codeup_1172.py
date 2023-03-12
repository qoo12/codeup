input_nums = list(map(int, input().split()))

for i in range(2, -1 , -1) :
    j = 0
    while j < i :
        if input_nums[j] > input_nums[j+1] :
            temp = input_nums[j+1]
            input_nums[j+1] = input_nums[j]
            input_nums[j] = temp
        j += 1

print(*input_nums, sep=' ')