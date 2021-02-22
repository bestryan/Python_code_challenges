# Divisible by Ten
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for x in nums:
    if (x % 10 == 0):
      count = count + 1
  return count
     
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


# Greetings
#Write your function here
def add_greetings(names):
  new_greetings = []
  for i in names:
    new_greetings.append("Hello, " + i)
  return new_greetings

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


# Delete Starting Even Numbers
#Write your function here
def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst.pop(0)
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))



# Odd Indices
#Write your function here
def odd_indices(lst):
  new_list = []
  for index in range(1, len(lst), 2):
    new_list.append(lst[index]) 
  return new_list
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


#Exponents
#Write your function here
def exponents(bases, powers):
  newlist = []
  for a in bases:
    for b in powers:
      newlist.append(a**b)
  return newlist

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


#Larger Sum
#Write your function here
def larger_sum(lst1, lst2):
  num1=0
  num2=0
  for number in lst1:
    num1 = number + num1
  for number in lst2:
    num2 = number + num2
  if num1 >= num2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))


# Over 9000
#Write your function here
def over_nine_thousand(lst):
  sum1=0
  for number in lst:
    sum1 = number + sum1
    if sum1 >= 9000:
      break
  return sum1

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


# Max Num for loop
#Write your function here
def max_num(nums):
  current_max = 0
  for i in nums:
    if i > current_max: 
      current_max = i
  return current_max
  
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20, 90]))



# Same Values
# Write your function here
def same_values(lst1, lst2):
  newlist = []
  for index in range(len(lst1)):
    if lst1[index]==lst2[index]: 
      newlist.append(index)
  return newlist

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# Reversed List
#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))