import argparse

def main(number):
    # Write the code to determine whether or not a number is a pallindrome here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    number_string = str(number)

    string_list = list(number_string)
    string_list.reverse()
    string_reversed = ""
    for cur_char in string_list:
        string_reversed += cur_char

    if (string_reversed == number_string):
            print("True")
    else:
            print("False")



    return None

if __name__ == "__main__":
    arg = argparse.ArgumentParser("Pallindrome Checker")
    arg.add_argument("--x", type=int, help="Input a number to determine if it's a pallindrome")
    parsed = arg.parse_args()
    main(parsed.x)