def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to GitHub 🚀")


def simple_calculator():
    print("\nSimple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid choice")


def main():
    while True:
        print("\n==== Mini CLI Tool ====")
        print("1. Greet User")
        print("2. Calculator")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == '1':
            greet_user()
        elif option == '2':
            simple_calculator()
        elif option == '3':
            print("Goodbye 👋")
            break
        else:
            print("Invalid option, try again")


if __name__ == "__main__":
    main()
