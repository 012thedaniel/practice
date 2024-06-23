# Програма, яка запитує у користувача чотири числа -> окремо вираховує суму перших двох та
# двох інших -> розділяє першу суму на другу -> виводить результат на екран таким чином, що
# відповідь містить дві цифри після коми.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

sum1 = num1 + num2
sum2 = num3 + num4

result = sum1 / sum2
print(f"The result is: {result:.2f}")
