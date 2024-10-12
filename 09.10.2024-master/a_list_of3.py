import random

print ("solution a, CREATE lIAT OF 3 RANDOM BOOL")
list_of_3: list[bool] = [random.choice([True, False])for _ in range(3)]
print(list_of_3 , "\n")

print ("solution B, DID THE LIST CONTAIN ONlY True")
if all(list_of_3):
    print("The list contain only True", "\n")
else:
    print ("The list Not contain only True", "\n")

print ("solution C, DID THE LIST CONTAIN AT LAST 1 True")
if any(list_of_3):
    print("The list contain at last 1 True", "\n")
else:
    print (" The list not contain at last 1 True", "\n")

print ("solution D, DID THE LIST CONTAIN ONlY False")
if not any(list_of_3):
    print("All the list contain False", "\n")
else:
    print ("The list contain at last 1 False", "\n")

print ("solution E, DID THE LIST CONTAIN AT LAST 1 False")
if all(list_of_3):
    print("The list not contain False", "\n")
else:
    print (" The list contain at last 1 False", "\n")

print ("solution F, CREATE lIAT OF 5 RANDOM number between 2 to -2")
list_of_5: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(list_of_5 , "\n")

print ("solution G, DID ALL THE NUMBERS ARE DIFFERENT THEN 0")
if any(list_of_5):
    print("not all the numbers different from  0", "\n")
else:
    print("The list contain only 0", "\n")

print ("solution H, DID THE LIST CONTAIN AT LAST 1 NUMBER DIFFERENT THEN 0")
if any(list_of_5):
    print("AT LAST 1 NUMBER DIFFERENT THEN 0", "\n")
else:
    print("The list contain only 0", "\n")

print ("solution I, DID THE LIST CONTAIN ONLY 0")
if any(list_of_5):
    print("AT LAST 1 NUMBER DIFFERENT THEN 0", "\n")
else:
    print("The list contain only 0", "\n")

print ("solution I, DID THE LIST CONTAIN AT LAST 1 number 0")
if all(list_of_5):
    print("ALL THE NUMBERS ARE DIFFERENT THEN 0", "\n")
else:
    print("AT LAST 1 NUMBER ARE 0 ", "\n")