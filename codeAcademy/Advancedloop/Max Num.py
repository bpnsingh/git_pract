"""Create a function named max_num() that takes a list of numbers named nums as a parameter.
The function should return the largest number in nums"""
#Write your function here
def max_num(lst):
    max = lst[0]
    for num in lst:
        if num < max:
            continue
        else:
            max=num

    return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))