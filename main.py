from Store import Store
from Product import Product
def main():
    # create a new store
    store = Store("localhost", "root", "", "py_store")

    # prompt the user to choose an action
    while True:
        print("Choose an action:")
        print("1. List products")
        print("2. Store a new product")
        print("3. Search for a product")
        print("4. Show a product")
        print("5. Delete a product")
        print("6. Exit")

        choice = input("> ")

        if choice == "1":
            # display the products in the store
            store.display_products()
        elif choice == "2":
            # prompt the user to enter the product details
            name = input("Enter the product name: ")
            while True:
                try:
                    price = float(input("Enter the product price: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            while True:
                try:
                    quantity = int(input("Enter the product quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # create a new product and add it to the store
            product = Product(name, price, quantity)
            store.add_product(product)
            print("Product stored successfully!")
        elif choice == "3":
            # prompt the user to enter the product name to search for
            name = input("Enter the product name: ")

            # search for the product and display the result
            product = store.search_product(name)
            if product:
                print(product)
            else:
                print("Product not found.")
        elif choice == "4":
            # prompt the user to enter the product ID to display
            id = int(input("Enter the product ID: "))

            # display the product with the given ID
            product = store.get_product(id)
            if product:
                print(product)
            else:
                print("Product not found.")
        elif choice == "5":
            # prompt the user to enter the product ID to delete
            id = int(input("Enter the product ID: "))

            # remove the product with the given ID from the store
            product = store.get_product(id)
            if product:
                store.remove_product(product)
                print("Product deleted successfully!")
            else:
                print("Product not found.")
        elif choice == "6":
            # exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()