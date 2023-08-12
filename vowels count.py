def count_vowels(input_str):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_str:
        if char in vowels:
            vowel_count += 1
    print("Number of vowels:", vowel_count)

user_input = input("Enter a string: ")
count_vowels(user_input)
