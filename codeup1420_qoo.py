input_cnt = int(input())
sort_member = []

if input_cnt > 2 and input_cnt < 51 :
    for i in range(0, input_cnt) :
        input_list = list(map(str,input().split()))
        input_list[1] = int(input_list[1])
        sort_member.append(input_list)


for i in range(1, input_cnt) :
    for j in range(i, 0, -1) :
        if sort_member[j][1] < sort_member[j-1][1] :
            temp = sort_member[j-1]
            sort_member[j-1] = sort_member[j]
            sort_member[j] = temp
        else : break

print(sort_member[input_cnt-3][0])