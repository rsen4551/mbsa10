# accept numbers till user enters 0 and display the total of all the numbers entered.
def main():
    total = 0
    while True:
        try:
            num = int(input("Enter a number (0 to exit): "))
            if num == 0:
                break
            total += num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Total sum of entered numbers: {total}")

obj=main()