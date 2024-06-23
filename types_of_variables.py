# 1. Змінній varInt надається значення 10, varFloat - значення 8.4, var_str - 'No'.
varInt = 10
varFloat = 8.4
varStr = "No"

# 2. Значення, що зберігається в змінній varInt, збільшено в 3.5 рази та зв'язано зі змінною varBig.
varBig = varInt * 3.5

# 3. Значення, збережене в змінній varFloat, зменшено на одиницю та зв'язано з тією ж змінною.
varFloat -= 1

# 4. varInt розділено на varFloat і varBig на varFloat без прив'язки до жодної зі змінних
varInt / varFloat
varBig / varFloat

# 5. Значення, збережене в змінній varStr, змінено на "NoNoYesYesYes"
# *з використанням операції конкатенації (+) і повторення рядка (*)
varStr = "No" * 2 + "Yes" * 3

# Вивід значень всіх змінних
print(f"varInt: {varInt}")
print(f"varFloat: {varFloat}")
print(f"varBig: {varBig}")
print(f"varStr: {varStr}")
