

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
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

    quantities = {item : skus.count(item) for item in base_prices.keys()}
    if sum(quantities.values()) != len(skus) : return -1

    for product,t in free_discount.items():
        n_for_discount, free_item = t
        quantities[free_item] = max(0, quantities[free_item] - quantities[product] // n_for_discount)

    checkout = sum(quantities[product]*price for product,price in base_prices.items())

    for product,t in first_discount.items():
        n_for_discount, discount = t
        checkout -= (quantities[product] // n_for_discount) * discount

    checkout -= quantities["A"] // 5 * 50
    checkout -= (quantities["A"]%5) // 3 * 20
    checkout -= quantities["B"] // 2 * 15
    checkout -= quantities["F"] // 3 * 10

    return checkout

