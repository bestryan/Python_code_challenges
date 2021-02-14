# 1. Every Three Numbers
#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

# 2. Remove Middle
#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 3. More Frequent Item
#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    print(item1)
  else:
    print(item2)

#Uncomment the line below when your function is done
#print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# 4. Double Index
#Write your function here
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
   new_list = lst[0:index]
   new_list.append(lst[index]*2)
   full_list = new_list + lst[index+1:]
   return full_list

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))