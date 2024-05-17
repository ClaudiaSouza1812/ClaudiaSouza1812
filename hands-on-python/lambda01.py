# Write a lambda function that you can use as the key argument in the sorted() function to sort the list of tuples based on
# the ages in ascending (from low to high) order. After sorting, print the sorted list.

def main():

    people = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("David", 35)]
    people.sort(key=lambda tuple: tuple[1])
    print(people)

main()
