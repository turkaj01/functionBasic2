list=[]
x=5
y=0
def countdown(n,x):
    for i in range(n, x-1, -1):
        list.append(i)
    print(list)
countdown(5,0)

x=0
y=0
list=[x,y]
def print_and_return(list):
    print(list[0])
    return list[1]

result=print_and_return([1,2])
print(result)


def first_plus_length(numbers:list):
    shuma=numbers[0] + len(numbers)
    return shuma

x=first_plus_length([5,4,3,2,1])
print(x)


def values_greater_than_second(numbers:list):
    new_list=[]
    for i in range(len(numbers)):
        if numbers[i]>numbers[1]:
            new_list.append(numbers[i])
    if len(new_list)<2:
        return False
    else:
        print(len(new_list))
        return new_list

print(values_greater_than_second([1,2,3,4]))


def length_and_value(x,y):
    return [y]*x

print(length_and_value(4,7))





