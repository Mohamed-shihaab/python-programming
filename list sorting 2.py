numbers = []

n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print("Original List:", numbers)

ascending = sorted(numbers)
print("Ascending Order:", ascending)

descending = sorted(numbers, reverse=True)
print("Descending Order:", descending)
