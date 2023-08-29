def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # Prints True
