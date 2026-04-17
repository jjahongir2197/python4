class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, "-", self.price)


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_cart(self):
        for item in self.items:
            item.display()
        print("Total:", self.total_price())


def main():
    p1 = Product("Phone", 500)
    p2 = Product("Laptop", 1000)

    cart = Cart()

    cart.add_product(p1)
    cart.add_product(p2)

    cart.show_cart()


main()
