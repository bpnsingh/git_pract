"""
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return the middle element.
If there are an even number of elements, the function should return the average of the middle two elements.

"""
def middle_element(lst):
    middle_index = len(lst)//2
    if len(lst)%2 ==0 :
        avg = (lst[middle_index-1] + lst[middle_index]) /2
        return avg
    else:
        return lst[middle_index]

print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -4, 4, 5]))