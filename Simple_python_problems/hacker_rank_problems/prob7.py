if __name__ == "__main__":
    n = int(input().strip())
    phone_book = {}
    for i in range(n):
        contact = input().strip().split()
        phone_book[contact[0]] = contact[1]

    while (True):
        try:
            name = input().strip()
            if name in phone_book:
                print(f"{name}={phone_book[name]}")
            else:
                print("Not found")
        except EOFError:
            break
'''This code appears to be a simple phone book application implemented in Python. It reads a series of inputs to build a phone book dictionary, and then it allows users to query the phone book to find phone numbers associated with names. Here's a breakdown of how the code works:

n = int(input().strip()): This line reads an integer n from the input, which represents the number of entries you want to add to the phone book.

phone_book = {}: It initializes an empty dictionary called phone_book to store the phone book entries, where the keys are names (strings) and the values are phone numbers (also strings).

The code then enters a loop that runs n times:

a. contact = input().strip().split(): Inside the loop, it reads a line of input, strips any leading/trailing whitespace, and splits it into a list called contact. The input line is expected to be in the format "name phone_number," where name is a string and phone_number is also a string.

b. phone_book[contact[0]] = contact[1]: It adds an entry to the phone_book dictionary. contact[0] is the name, and contact[1] is the associated phone number. This line adds the name as the key and the phone number as the value in the dictionary.

After building the phone book, the code enters another loop that continues indefinitely using a while(True) loop. Inside this loop, it attempts to read lines of input using try and except:

a. name = input().strip(): It reads a line of input and strips any leading/trailing whitespace. This line expects the user to input a name they want to search for in the phone book.

b. if name in phone_book:: It checks if the entered name exists as a key in the phone_book dictionary.

If the name exists, it prints the corresponding phone number using a formatted string.
If the name does not exist, it prints "Not found."
c. except EOFError:: This exception is caught when there is no more input to read, typically when the user presses Ctrl+D (EOF in Unix-like systems) to signal the end of input. When this happens, the loop breaks using break, and the program terminates.

In summary, this code builds a phone book from a list of entries and allows users to query the phone book by entering names. If the name exists in the phone book, it prints the associated phone number; otherwise, it prints "Not found." The program continues to accept user input until the user signals the end of input.'''
