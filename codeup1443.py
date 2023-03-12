def select_sort(arr) :
    for i in range(len(arr)-1) :
        j = i+1
        while arr[j-1] > arr[j] and j > 0 :
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

input_cnt = int(input())
sorting_nums = []

for i in range(input_cnt) :
    a = int(input())
    sorting_nums.append(a)

select_sort(sorting_nums)

for i in range(input_cnt) :
    print(sorting_nums[i])