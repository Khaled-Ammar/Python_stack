# def down (num):
#     arr=[]
#     for x in range(num,0,-1):
#         arr.append(x) 
#     return arr
# print(down(9))
# ----------------------------
# def print_return(list):
#     print(list[0])
#     return list[1]
# print('return is' , print_return([5,6]))
# --------------------------------
def first_plus_length(array):
    sum = array[0] + len(array)
    return sum
print(first_plus_length([1,2,3]) )
# ----------------------------------
def values_greater_than_second(list1):
    list2=[]
    for x in list1:
        if len(list1)==1:
            return 'false'
            
        if x>list1[1]:
            list2.append(x)
    return list2
    
    
print(values_greater_than_second([5,2,3,2,1,4]));
# --------------------------------------------
def length_and_value(length,val):
    list1=[]
    count=length
    while count>0:
        list1.append(val)
        count-=1
    return list1
    
print(length_and_value(4,7))  
print(length_and_value(6,2))        


