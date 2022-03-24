

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    base_prices = {"A" : 50, "B" : 30, "C" : 20, "D" : 15, "E" : 40}

    quantities = {item : skus.count(item) for item in base_prices.keys()}
    if sum(quantities.values()) != len(skus) : return -1

    quantities["B"] = max(0, quantities["B"] - quantities["E"] // 2)

    checkout = sum(quantities[product]*price for product,price in base_prices.items())
    checkout -= quantities["A"] // 5 * 50
    checkout -= (quantities["A"]%5) // 3 * 20
    checkout -= quantities["B"] // 2 * 15

    return checkout


