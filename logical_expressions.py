from types_of_variables import varInt, varBig, varStr, varFloat

a = 5
b = 10

# Оператор and
expression1 = (a < varInt) and (b <= varBig)  # True
expression2 = (b >= varInt) and (a > varBig)  # False

# Оператор or
expression3 = (varInt < varBig) or (b < 0)  # True
expression4 = (varBig < len(varStr)) or (a > varFloat)  # False

# Логічні вирази зі змінними строкового типу
str1 = "Hello"
str2 = ""

str_expression1 = str1 and str2  # ""
str_expression2 = str1 or str2  # "Hello"

# Запитання у користувача двох чисел
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(num1 > num2)
