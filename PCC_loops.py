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

#