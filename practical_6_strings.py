"""
PRACTICAL NO: 6
STRING OPERATIONS

Lab Assignment - 1
Lab Assignment - 2
"""

# ==========================================
# LAB ASSIGNMENT - 1
# ==========================================

print("LAB ASSIGNMENT - 1")

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
space_count = 0
lowercase_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
    if char == " ":
        space_count += 1
    if char.islower():
        lowercase_count += 1

print("\nString Statistics:")
print("Number of Vowels:", vowel_count)
print("Number of Consonants:", consonant_count)
print("Number of Spaces:", space_count)
print("Number of Lowercase Letters:", lowercase_count)


# ==========================================
# LAB ASSIGNMENT - 2
# ==========================================

print("\nLAB ASSIGNMENT - 2")

def capitalize_lines():
    print("Enter multiple lines (Type 'END' to stop):")
    
    lines = []
    while True:
        line = input()
        if line.upper() == "END":
            break
        lines.append(line)
    
    print("\nCapitalized Output:")
    for line in lines:
        print(line.upper())

capitalize_lines()
