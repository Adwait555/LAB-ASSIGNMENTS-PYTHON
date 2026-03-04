# Practical3
# TASK 1 PATTERNS

print("pattern 1")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print("\n")

print("pattern 2")
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
print("\n")

print("pattern 3")
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
print("\n")

print("pattern 4")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end="")
        else:
            print(0, end="")
    print()
print("\n")

print("pattern 5")
num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
print("\n")

print("pattern 6")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print("\n")

# TASK 2

print("1. Alphabet Pattern")
for i in range(65, 70):  # ASCII A=65
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()
print("\n")

print("2. Symbol Pattern")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("*", end="")
        else:
            print("#", end="")
    print()
print("\n")

print("3. Repeated Letter Pattern")
word = "python"

for i in range(len(word)):
    for j in range(i + 1):
        print(word[i], end="")
    print()
print("\n")

print("4. Python Word Pattern")
word = "Python"

for i in range(1, len(word) + 1):
    print(word[:i])
print("\n")

# ==============================
# TASK – 3 : Print 1 to n (No String Method)
# ==============================

print("\nTASK 3 - Print 1 to n")
n = int(input("Enter value of n: "))
for i in range(1, n + 1):
    print(i, end="")
print()

# ==============================
# TASK – 4 : Reverse Star Pattern
# ==============================

print("\nTASK 4 - Reverse Star Pattern")
rows = 5
for i in range(rows):
    print(" " * i + "* " * (rows - i))

# ==============================
# TASK – 7 : Prime Number Finder
# ==============================

print("\nTASK 7 - Prime Number Finder")

while True:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    if start < end:
        break
    else:
        print("Start number must be less than end number. Try again.")

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

