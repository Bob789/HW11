print("Solution A, Create Base STR")
str_detiels: str = "Yossi Levi Nale"
print(str_detiels, f"Length : {len(str_detiels)} \n")

print("Solution B, CONVERT STRING TO UPPERCASE")
print(f" {str_detiels.upper()} \n")

print("Solution C, CONVERT STRING TO LOWER")
print(f" {str_detiels.lower()} \n")

print("Solution D, Check if the string starts with your first name: startswith")
print(str_detiels, 'str_detiels.startswith("Yossi") ?', str_detiels.startswith("Yossi"), "\n")

print("Solution E, Check if the string ends with your city of residence: endswith")
print(str_detiels, 'str_detiels.endswith("Nale") ?', str_detiels.endswith("Nale"), "\n")

print("Solution F , split string")
details_list: [str] = str_detiels.split()
print(details_list, "\n")

print("Solution G , split string")
print(str_detiels.replace(" ", "*"))
print(str_detiels.replace("*", " "))
details_list: [str] = str_detiels.split()
print(details_list, "\n")

print("Solution H, Print the string in the center of 50 characters, wrapped in the = character: center")
center_str: str = "WoW"
print(center_str.center(50, '='), "\n")

print("Solution I, Print the string from 4 char to end ")
from_char4: str = "gravitation"
print("gravitation :"f"{from_char4[4:]}\n")

print("Solution J, Print the string from beginning to char 4 include")
txt4: str = "gravitation"
print("gravitation :"f"{txt4[:4]}", "\n")

print("Solution K, Print the  even char")
txt_even: str = "gravitation"
print("gravitation :"f"{txt_even[1::2]}", "\n")

print("Solution L, PRINT EACH WORD IN THE STRING WITH UPPERCASE")
txt: str = "gravitation, also known as gravitational attraction"
print(f" {txt.title()} \n")




