name = input("What's your name friend?")
print(f"welcome to my trial python {name}")

def game():
  colours = ['brown', 'white', 'blue']
  for colour in colours:
    if colour == 'brown':
      return "Your are a rare gem!"
    else:
      return "You dont have a good taste in colours"

print(input('what color do you choose? '))
print(game())



#     LOOPS 

# ages = [14, 17, 20, 34, 24, 16]

# for age in ages:
#   if age < 21:
#     continue
#   print (age)
    



# FUNCTIONS WITH CONDITIONS
# def large_power(base, exponent):
#   result = base ** exponent
#   if result > 5000:
#     return True
#   else:
#     return False
   
# print(large_power(200, 10))
  


# examples of function

def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False
  
print(divisible_by_ten(500))  





