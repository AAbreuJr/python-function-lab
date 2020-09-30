#-----------------------
# FUNCTION LAB
# Anderson Abreu Jr.
#-----------------------

# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest
  
def largest(nums):
  nums.sort()
  return nums[-1]



# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside 

def occurances(string, substr):
  stripped_string = string.replace(substr, '')
  return (len(string) - len(stripped_string)) // len(substr)
  
def occurances(string, substr):
  return string.count(substr)




# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product