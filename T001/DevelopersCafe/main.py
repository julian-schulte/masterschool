def print_header(name):
    print(name)
    print("---------------")

def calc_espresso_price(espresso_quantity):
    return espresso_quantity * 1.5

def calc_cappuccino_price(cappuccino_quantity):
    return cappuccino_quantity * 2.75

def calc_latte_price(latte_quantity):
    return latte_quantity * 3.25

def print_body(espresso_quantity, cappuccino_quantity, latte_quantity, calc_espresso_price, calc_cappuccino_price, calc_latte_price):
    print(f"{espresso_quantity}x Espresso($1.5) --- ${calc_espresso_price}")
    print(f"{cappuccino_quantity}x Cappuccino($2.75) --- ${calc_cappuccino_price}")
    print(f"{latte_quantity}x Latte($3.25) --- ${calc_latte_price}")

def print_footer(calc_espresso_price, calc_cappuccino_price, calc_latte_price):
    print("---------------")
    print(f"Total --- ${calc_espresso_price + calc_cappuccino_price + calc_latte_price}")

def print_receipt(espresso_quantity, cappuccino_quantity, latte_quantity, name):
    print_header(name)
    espresso_price = calc_espresso_price(espresso_quantity)
    cappuccino_price =calc_cappuccino_price(cappuccino_quantity)
    latte_price = calc_latte_price(latte_quantity)
    print_body(espresso_quantity, cappuccino_quantity, latte_quantity, espresso_price, cappuccino_price, latte_price)
    print_footer(espresso_price, cappuccino_price, latte_price)


print_receipt(2,5,7, "RYZONE")