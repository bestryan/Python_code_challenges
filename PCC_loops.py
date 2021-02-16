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

