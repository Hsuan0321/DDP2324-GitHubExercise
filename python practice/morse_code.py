"""
Morse Code Translator Function

Objective:
Write a function named 'morse_translator' that translates a given string into Morse code.

Function Parameter:
text (string): The string to be translated into Morse code.

Instructions:
- Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
- The Morse code for each character should be separated by a space.
- Each word in the string should be separated by a forward slash (/).
- The function should handle both uppercase and lowercase alphabetic characters.
- The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
- Non-alphabetic characters (like numbers or symbols) should not be translated.
- https://en.wikipedia.org/wiki/Morse_code

Example Test Cases:
1. morse_translator("HELLO WORLD") should return the Morse code for the given string.
2. morse_translator("Python") should return the Morse code for the given string.
3. morse_translator("Morse Code") should return the Morse code for the given string.
"""


def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    text= text.upper() #convert all text into upperletter text
    
    morse_code_list= [morse_code_dict[char] for char in text if char in morse_code_dict]
    #for char in text: 这是一个迭代，它遍历输入文本 text 中的每一个字符，将当前字符赋值给变量 char。
    #if char in morse_code_dict: 使用条件语句判断当前字符 char 是否在摩尔斯密码字典 morse_code_dict 中。
    #[morse_code_dict[char] for char in text if char in morse_code_dict]: 这是列表推导式的语法，它会生成一个新的列表。
    #对于输入文本中的每个字符，如果该字符在摩尔斯密码字典中存在，则取出相应的摩尔斯密码并添加到新列表中。  
    #morse_code_dict[char]：表示取摩尔斯密码字典中当前字符 char 对应的摩尔斯密码。
    #整个列表推导式生成了一个包含输入文本中每个存在于摩尔斯密码字典中字符的摩尔斯密码的列表。
    translation= " ".join(morse_code_list) #add space into the result of morse_code_list
    print(f"{translation}")
    # Your code goes here
    # Remember to consider both upper and lower case letters, and spaces
    # The function should return the translated Morse code string


# Test cases
print(
    morse_translator("HELLO WORLD")
)  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(
    morse_translator("Morse Code")
)  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
