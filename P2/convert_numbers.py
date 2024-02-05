"""
The following program is for concerting numbers to decimal and hexadecimal.
"""
import sys
import time

hex_dict = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}
inverted_hex_dict = {
    '0': 15,
    '1': 14,
    '2': 13,
    '3': 12,
    '4': 11,
    '5': 10,
    '6': 9,
    '7': 8,
    '8': 7,
    '9': 6,
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 0,
}

def display_results(results):
    """
    Function to display results.
    """
    for file in results:
        print("Number\tBin\tHex")
        for line in file:
            print(line)
        print("\n")
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as results_file:
        for file in results:
            print("Number\tBin\tHex")
            results_file.write("Number\tBin\tHex\n")
            for line in file:
                print(line)
                results_file.write(f"{line}\n")
            print("\n")
            results_file.write("\n")

def get_negative_representation(base, new_representation):
    """
    Returns negative representation with complement 2 values
    """
    if base == 2:
        n = len(new_representation)
        carry_value = 0
        new_negative_representation = ""
        for j in range(n):
            if j == 0:
                carry_value = 1
            val = int(not int(new_representation[n-j-1]))
            val = val + carry_value
            if val in [0, 1]:
                new_negative_representation = str(val) + new_negative_representation
                carry_value = 0
            else:
                new_negative_representation = "0" + new_negative_representation
                carry_value = 1
    else:
        n = len(new_representation)
        carry_value = 0
        new_negative_representation = ""
        for j in range(n):
            if j == 0:
                carry_value = 1
            val = inverted_hex_dict[new_representation[n-j-1]]
            val = val + carry_value
            if val  > 15:
                new_negative_representation =  "0" + new_negative_representation
                carry_value = 1
            elif val  > 9:
                new_negative_representation = hex_dict[val] + new_negative_representation
                carry_value = 0
            else:
                new_negative_representation = str(val) + new_negative_representation
                carry_value = 0

    return new_negative_representation

def decimal_to_base(num, base):
    """
    Function to change a number from decimal number to another
    """
    if base not in [2,16]:
        raise ValueError("Base not valid")
    negative = False
    if num < 0:
        negative = True
        num = abs(num)

    new_representation = ""
    if num == 0:
        new_representation = "0"
    else:
        while num > 0:
            remainder = num % base
            if remainder > 9:
                new_representation = hex_dict[remainder] + new_representation
            else:
                new_representation = str(remainder) + new_representation
            num //= base
    if negative:
        new_representation = get_negative_representation(base, new_representation)
    return new_representation


def convert_numbers(filename):
    """
    Function to convert numbers.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = [int(line.strip()) for line in file
                if line.strip().replace('.', '', 1).isdigit()
                or (line.strip().startswith('-')
                    and line.strip()[1:].replace('.', '', 1).isdigit())]

    if not data:
        raise ValueError("Error: Empty data set. Unable to convert numbers.")

    all_numbers = []
    for num in data:
        binary = decimal_to_base(num, 2)
        hexadecimal = decimal_to_base(num, 16)
        new_row = f"{num}\t{binary}\t{hexadecimal}"
        all_numbers.append(new_row)

    return all_numbers


if __name__ == "__main__":
    try:
        time_start = time.time()

        if len(sys.argv) < 2:
            raise ValueError("Error: Invalid number of arguments. Please provide a file path.")

        file_results = []
        for i in range(1,len(sys.argv)):
            file_path = sys.argv[i]
            stats = convert_numbers(file_path)
            file_results.append(stats)

        display_results(file_results)

        elapsed_time = time.time() - time_start
        print(f"Time elapsed: {elapsed_time} s")

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(ve)
