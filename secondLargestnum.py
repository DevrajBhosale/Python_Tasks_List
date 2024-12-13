# Find the second largest number in a list

numbers = input("Enter Numbers: ")
lst = []
lst = numbers.split()
lst.sort(reverse = True)
print(lst[1])