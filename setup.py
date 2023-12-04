# 1. Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max([a, b, c])

print(max_num(8, 24, 13))


# 2. Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(mult_list([3, 3, 3]))


# 3. Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]

print(rev_string('Kawhi Leonard'))


# 4. Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,1,3))   
print(num_within(10,2,5))   


# 5. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(5)