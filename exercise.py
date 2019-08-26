# 003111 # 3 = 1 + 1 + 1
# 813372 # 8 + 1 + 3 = 3 + 7 + 2
# 17935 # 1 + 7 = 3 + 5
# 56328116

def luckCheck(num):
    
    if len(num) % 2 == 0:
        half = len(num)/2
        
        left_half = num[:int(half)]
        right_half = num[int(half):]
        
        left_list = list(left_half)
        right_list = list(right_half)
        
        left_sum = []
        right_sum = []

        for i_left in left_list:
            left_sum.append(int(i_left))
        for i_right in right_list:
            right_sum.append(int(i_right))
        
        if sum(left_sum) == sum(right_sum):
            return "You're very lucky!"
        else:
            return "It's not your lucky day ¯\_(ツ)_/¯ "

    if len(num) % 2 == 1:
        half = len(num)/2
        
        left_half = num[:int(half)]
        right_half = num[int(half):]
        
        left_list = list(left_half)
        right_list = list(right_half)
        right_list[0] = 0

        left_sum = []
        right_sum = []

        for i_left in left_list:
            left_sum.append(int(i_left))
        for i_right in right_list:
            right_sum.append(int(i_right))

        if sum(left_sum) == sum(right_sum):
            return "You're very lucky!"
        else:
            return "It's not your lucky day ¯\_(ツ)_/¯ "
        
            
    
    
    




ex = luckCheck('63263')
print(ex)