inventory = {
    "яблуко": 10,
    "груша": 3,
    "банан": 7
}

def update_inventory(product, amount):
    if product in inventory:
        inventory[product] += amount
    else:
        inventory[product] = amount

update_inventory("яблуко", -2)
update_inventory("апельсин", 4)

print("Склад після оновлення:", inventory)

low_stock = []
for product, amount in inventory.items():
    if amount < 5:
        low_stock.append(product)

print("Продукти, де залишилось менше 5:", low_stock)
