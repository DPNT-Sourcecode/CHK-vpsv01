

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    c = 0
    for sku in "ABCD":
        c += sku.count("A")
