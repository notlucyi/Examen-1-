from store import Product, Cart

cart = Cart()

added_products = [
    Product("Rice", 1.50),
    Product("Milk", 1.25),
    Product("Bread", 0.75),
    Product("Eggs", 2.80)
]

def menu_tienda():
    while True:
        print("Store menu ")
        print("1. View product list")
        print("2. Add product to cart")
        print("3. View cart")
        print("4. Clear cart")
        print("5. Logout")

        option = input("Choose an option: ")

        if option == "1":
            print("Products available: ")
            for i, p in enumerate(added_products, start=1):
                print(f"{i}. {p}")

        elif option == "2":
            nombre = input("Name of the product: ")
            precio = float(input("Price of the product: "))
            cantidad = int(input("Quantity: "))

            product = Product(nombre, precio)

            for _ in range(cantidad):
                cart.agregar(product)

        elif option == "3":
            cart.ver()

        elif option == "4":
            cart.vaciar()

        elif option == "5":
            print("Login out...")
            break

        else:
            print("Invalid option, try again.")