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