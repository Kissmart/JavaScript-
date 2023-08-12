def remove_whitespace(input_str):
    without_whitespace = input_str.replace(" ", "")
    print(without_whitespace)

user_input = input("Enter a string: ")
remove_whitespace(user_input)
