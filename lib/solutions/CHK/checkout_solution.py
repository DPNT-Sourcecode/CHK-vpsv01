

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    def get_values (d):
        for k,t in d.items():
            a, b = t; yield k, a, b

    base_prices = {
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15,
        "E" : 40,
        "F" : 10,
        "G" : 20,
        "H" : 10,
        "I" : 35,
        "J" : 60,
        "K" : 80,
        "L" : 90,
        "M" : 15,
        "N" : 40,
        "O" : 10,
        "P" : 50,
        "Q" : 30,
        "R" : 50,
        "S" : 30,
        "T" : 20,
        "U" : 40,
        "V" : 50,
        "W" : 20,
        "X" : 90,
        "Y" : 10,
        "Z" : 50
    }

    first_discount = {"A" : (5,  50), "B" : (2, 15), "F" : (3, 10),
                      "H" : (10, 20), "K" : (2, 10), "P" : (5, 50),
                      "Q" : (3,  10), "U" : (4, 40), "V" : (3, 20)}
    second_discount = {"A" : (3, 20), "H" : (5, 5), "V" : (2, 10)}
    free_discount = {"E" : (2, "B"), "N" : (3, "M"), "R" : (3, "Q")}

    qty = {item : skus.count(item) for item in base_prices.keys()}
    if sum(qty.values()) != len(skus) : return -1

    for product, n_for_discount, free_item in get_values(free_discount):
        qty[free_item] = max(0, qty[free_item] - qty[product] // n_for_discount)

    checkout = sum(qty[product]*price for product,price in base_prices.items())

    for product, n_for_discount, discount in get_values(first_discount):
        checkout -= (qty[product] // n_for_discount) * discount

    for product, n_for_discount, discount in get_values(second_discount):
        checkout -= ((qty[product]%first_discount[product][0]) // n_for_discount) * discount

    return checkout






