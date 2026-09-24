
# Demonstration of lambda functions and their equivalent regular functions in Python
square = lambda x: x**2
print(square(5))  # 25
print(square)


# Equivalent regular function for the lambda function above
def square_function(x):
    return x**2
print(square_function(5))  # 25
print(square_function)

# Difference between lambda and regular function
print(square(5))  # 25
print(square_function(5))  # 25
print(square)  # <function <lambda> at ...>
print(square_function)  # <function square_function at ...>

# Note: Lambda functions are anonymous and typically used for short, simple operations, whereas regular functions are named and can contain more complex logic.