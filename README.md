# Collatz Sequence Program

## Overview
The Collatz Sequence Program is a Python application that explores the Collatz conjecture, which posits that for any positive integer, repeatedly applying a specific set of operations will eventually lead to the number 1. This program allows users to input an integer and calculates the next number in the sequence until it reaches 1.

## Functionality
- The program defines a function `collatz(number)` that:
  - Takes an integer as input.
  - Checks if the number is even or odd.
  - If even, it returns half of the number.
  - If odd, it returns `3 * number + 1`.
  - It prints the result of each operation.

- The main function continuously prompts the user for an integer input and:
  - Calls the `collatz()` function until the result is 1.
  - Allows the user to exit the program by typing 'quit' or pressing enter without inputting a number.
  - Handles invalid inputs gracefully by prompting the user to enter a valid integer.

## Requirements
- Python 3.x

## Usage
1. Clone or download the repository containing the code.
2. Open a terminal or command prompt.
3. Navigate to the directory where the code is located.
4. Run the program using the command:
   ```bash
   python collatzSequence.py
