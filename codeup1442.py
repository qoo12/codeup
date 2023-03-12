def select_sort(arr) :
    for i in range(len(arr)-1) :
        min_idx = i
        for j in range(i+1, len(arr)) :
            if arr[min_idx] > arr[j] :
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

input_cnt = int(input())
sorting_nums = []

for i in range(input_cnt) :
    a = int(input())
    sorting_nums.append(a)

select_sort(sorting_nums)

for i in range(input_cnt) :
    print(sorting_nums[i])