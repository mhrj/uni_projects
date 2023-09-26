import math

# compelexity = log2n 
# go to the middle of numbers
# ether if the number is less or is more we guess middle again
# continue the algorithm to compelete binary search
# we must have ordered list

list_of_nums = [1,2,3,4,5,6,7,8,9,10,12,14,16,18,20]
target_num = 14

def binary_search():
    search_time = 0
    low_index = 0
    high_index = int(len(list_of_nums) - 1)
    while(low_index <= high_index):
        mid = int((low_index + high_index) / 2)
        middle_number = list_of_nums[mid]
        if(middle_number == target_num):
            print(f"found it! => {middle_number}")
            print(f"compelexity : log2 {search_time} = {math.log2(search_time)}")
            break
        if(middle_number < target_num):
            low_index = mid + 1
        elif(middle_number > target_num):
            high_index = mid - 1
        search_time += 1 
        
binary_search()
    