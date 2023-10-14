# Read a string as input
input_str = input()

try:
    # Try to convert the input to an integer
    int_value = int(input_str)

    # Check if it's an integer
    print("Integer")

except ValueError:
    try:
        # Try to convert the input to a float
        float_value = float(input_str)

        # Check if it's a float
        print("Float")

    except ValueError:
        # If neither conversion works, it's not an integer or a float
        print("None")
