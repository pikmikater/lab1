sales = [
    {"продукт": "яблуко", "кількість": 20, "ціна": 30},
    {"продукт": "груша", "кількість": 15, "ціна": 40},
    {"продукт": "яблуко", "кількість": 10, "ціна": 30},
    {"продукт": "банан", "кількість": 5, "ціна": 50}
]

def calculate_income(sales):
    income = {}
    for sale in sales:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        if product in income:
            income[product] += total
        else:
            income[product] = total
    return income

result = calculate_income(sales)
print("Загальний дохід по продуктах:", result)

profitable = []
for product, money in result.items():
    if money > 1000:
        profitable.append(product)

print("Продукти з доходом більше 1000:", profitable)
