#----------------------------------------------1

def biggiesize(list1):
    for i in range(len(list1)):
        if list1[i] > 0:
            list1[i]='big'
    return list1
print(biggiesize([-1, 3, 5, -5]))


#-----------------------------------------------2

def count_positive(list1):
    count=0
    for i in range(len(list1)):
        if list1[i]>0:
            count+=1
            
        list1[len(list1)-1]=count
    return list1
print(count_positive([-1,1,1,1]))
print(count_positive([1,6,-4,-2,-7,-2]))

#---------------------------------------------3

def total(list1):
    sum=0
    for i in range(len(list1)):
        sum+=list1[i]
    return sum
print(total([1,2,3,4]))
print(total([6,3,-2]))

#-----------------------------------------4

def Average (list1):
    sum=0
    for i in range(len(list1)):
        sum+=list1[i]
    return sum/len(list1)
print(Average([1,2,3,4]))
print(Average([6,3,-2]))

#-------------------------------------------5

def length(list1):
    return len(list1)
print(length([1,2,3,4]))
print(length([]))

#--------------------------------------------6

def minimum(list1):
    min=list1[0]
    for i in range(len(list1)):
        if min > list1[i]:
            min=list1[i]
    return min
print(minimum([37,2,-10,-9]))

#-----------------------------------------------7

def max(list1):
    max1=list1[0]
    for i in range(len(list1)):
        if max1 < list1[i]:
            max1=list1[i]
    return max1
print(max([37,2,-10,99]))

#----------------------------------------------------8

def ultimate_analysis(list1):
    dictionary={}
    sum=0
    avg=0
    minimum=list1[0]
    maximum=list1[0]
    for i in range(len(list1)):
        sum+=list1[i]
        avg=sum/len(list1)
        if minimum > list1[i]:
            minimum=list1[i]
        if maximum < list1[i]:
            maximum=list1[i]
        length=len(list1)
    dictionary['sumTotal']=sum
    dictionary['average']=avg
    dictionary['minimum']=minimum
    dictionary['maximum']=maximum
    dictionary['length']=length
    return dictionary
print(ultimate_analysis([37,2,1,-9]))  
        
#---------------------------------------------------9

def reverse_list(list1):
    list1.reverse()
    return list1
print(reverse_list([37,2,1,-9]))



