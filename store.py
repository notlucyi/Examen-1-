class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Cart:
    def __init__(self):
        self.products = []

    def agregar(self, product):
        self.products.append(product)
        print("Producto added.")

    def ver(self):
        if not self.products:
            print("The cart is empty.")
        else:
            print("Products in the cart:")
            total = 0
            for p in self.products:
                print(f"- {p}")
                total += p.price

            print(f"Your total is: ${total:.2f}")

    def vaciar(self):
        self.products.clear()
        print("The cart has been emptied.")