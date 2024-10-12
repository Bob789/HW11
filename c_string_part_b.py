print("Solution A, STRIP")
text1: str = "    fun-day    "
print("    fun-day    ", '**strip:', text1.strip(), "\n")

print("Solution B, ISALPHA")
text: str = "hello"
print(f"did the text is alpha: {text.isalpha()}\n")

print("Solution C, ISDIGIT")
number: str = "584953"
print(f"did the text is digit: {number.isdigit()}\n")

print("Solution D, ISSPACE")
space: str = "      "
print(f"did the text is space: {space.isspace()}\n")

print("Solution E, JOIN")
list_j: list[str] = ['N', "I", "N", "J", "A"]
print(f"list_j: {list_j}")
new_str: str =  "".join(list_j)
print("join ['N', 'I', 'N', 'J', 'A'] :",f"{new_str} \n")

print("Solution F, JOIN *")
print(f"{new_str}")
print("*".join(new_str), "\n")

print("Solution G, CHECK IF LETTER IN STRING")
text = "hELLo".lower()
if "e" in text:
    print("The letter 'e' is in hELLo \n")
else:
    print("The letter 'e' is not in hELLo \n")

print("Solution H, split string to LETTERs then conver to uppercase and ignore digits")
text = "py3thon12"
split_upper_letter = [char.upper() for char in text if not char.isdigit()]
print(split_upper_letter)



