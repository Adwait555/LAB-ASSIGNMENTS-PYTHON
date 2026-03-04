"""
PRACTICAL NO: 5
TUPLE OPERATIONS

Lab Assignment - 1
Lab Assignment - 2
"""

# ==========================================
# LAB ASSIGNMENT - 1
# ==========================================

print("LAB ASSIGNMENT - 1")

# Take input from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

print("\nTuple:", numbers)

# a) Total number of items
print("\nTotal number of items in tuple:", len(numbers))

# b) Last item in tuple
print("Last item in tuple:", numbers[-1])

# c) Tuple elements in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if 5 is present
if 5 in numbers:
    print("Yes, tuple contains integer 5")
else:
    print("No, tuple does not contain integer 5")

# e) Remove first and last items, sort remaining items
if len(numbers) > 2:
    new_tuple = tuple(sorted(numbers[1:-1]))
    print("Tuple after removing first and last items and sorting:", new_tuple)
else:
    print("Not enough elements to remove first and last items")


# ==========================================
# LAB ASSIGNMENT - 2
# ==========================================

print("\nLAB ASSIGNMENT - 2")

# Take input for prices
prices = tuple(map(float, input("Enter prices of sold items separated by space: ").split()))

print("\nPrices Tuple:", prices)

# a) Total number of items sold
print("\nTotal number of items sold:", len(prices))

# b) Cheapest item price
print("Cheapest item price:", min(prices))

# c) Costliest item price
print("Costliest item price:", max(prices))

# d) Price list in ascending order
ascending_prices = tuple(sorted(prices))
print("Prices in ascending order:", ascending_prices)

# e) Number of costliest items sold
costliest_price = max(prices)
count_costliest = prices.count(costliest_price)
print("Number of costliest items sold:", count_costliest)
