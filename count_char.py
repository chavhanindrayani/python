def count_char_in_string(text, char):
    return text.count(char)

string = "banana"
character = "a"
result = count_char_in_string(string, character)
print(f"the character '{character}' appears {result} time(s) in '{string}'")