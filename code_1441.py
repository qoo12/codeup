input_cnt = int(input())
sorting_nums = []

for i in range(input_cnt) :
    a = int(input())
    sorting_nums.append(a)

for i in range(1, input_cnt) :
    for j in range(0, input_cnt-i) :
        if sorting_nums[j] > sorting_nums[j+1] :
            temp = sorting_nums[j]
            sorting_nums[j] = sorting_nums[j+1]
            sorting_nums[j+1] = temp

for i in range(input_cnt) :
    print(sorting_nums[i])