#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 18:01:36 2021

@author: lilygoodyersait
"""
## range from start to and including 100 in steps of 3
#Write your function here
def every_three_nums(start):
  if start > 100:
    l = []
    return l
  else:
    l=list(range(start,101,3))
    return l

#Uncomment the line below when your function is done
print(every_three_nums(91))

## remve elements between and including indices start:end:
def remove_middle(lst, start, end):
  del lst[start:end+1]
  return lst

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

## return most common item
#Write your function here
def more_frequent_item(lst,item1,item2):
  a=lst.count(item1)
  b=lst.count(item2)
  if a > b:
    return item1
  elif a < b:
    return item2
  else:
    return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

## double number at index position in list

def double_index(lst, index):
    if index > len(lst)-1:
        return lst
    else: 
        lst[index] = lst[index]*2
        return lst
    

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 4))

### return middle index or average of 2 middle index values if list len%2==0

#Write your function here
def middle_element(lst):
  if len(lst)%2 ==0:
    b =lst[int((len(lst)/2)-1)]
    c=lst[int((len(lst)/2))]
    d=(b+c)/2
    return d
  else:
    return lst[int(len(lst)/2)] ## rounds down e.g. half of 7 will equal 3

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5,8]))


