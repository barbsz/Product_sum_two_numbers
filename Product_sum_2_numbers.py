def calculate_product_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Given number 1 
number1 = 20
number2 = 30

result = calculate_product_or_sum(number1, number2)
print("The result is", result)