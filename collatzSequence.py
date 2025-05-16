def collatz(number):
    if number % 2 == 0:  # Check if the number is even
        result = number // 2
    else:  # The number is odd
        result = 3 * number + 1
    
    print(result)  # Print the result
    return result  # Return the result

def main():
    while True:
        user_input = input("Enter an integer (or type 'quit' to exit): ")
        if user_input.lower() == 'quit' or user_input.strip() == '':
            print("Goodbye!")
            break

        try:
            number = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        while number != 1:
            number = collatz(number)

if __name__ == "__main__":
    main()
