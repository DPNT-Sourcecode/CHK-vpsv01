

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    base_prices = {"A" : 50, "B" : 30, "C" : 20, "D" : 15 }
    discounts = {"A" : (3,20), "B" : (2,15)}  # if there are 3 A, discount is 20 gbp

    skus = skus.upper()
    quantities = {item : skus.count(item) for item in base_prices.keys()}
    if sum(quantities.values()) != len(skus) : return -1

    checkout = sum(quantities[product]*price for product,price in base_prices.items())
    for product,t in discounts.items():
        n_for_discount, discount = t
        checkout -= (quantities[product] // n_for_discount) * discount

    return checkout


