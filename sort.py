animals = [
    "dog", "cat", "lion", "tiger",  # Mammals
    "eagle", "parrot", "sparrow", "owl",  # Birds
    "shark", "dolphin", "whale", "octopus",  # Sea creatures
    "frog", "snake", "lizard", "turtle"  # Reptiles
]

# 1. Bubble Sort (Alphabetical)
def bubble_sort(animals):
    n = len(animals)
    for i in range(n):
        for j in range(0, n - i - 1):
            if animals[j] > animals[j + 1]:
                animals[j], animals[j + 1] = animals[j + 1], animals[j]
    return animals

# 2. Sorting Alphabetically Using Python's Built-in sort()
animals_sorted_alphabetically = animals[:]
animals_sorted_alphabetically.sort()

# 3. Sorting by Length Using sorted() with key=len
animals_sorted_by_length = sorted(animals, key=lambda x: len(x))

# 4. Printing the Results
print("Original List:", animals)
print("Bubble Sorted Alphabetically:", bubble_sort(animals[:]))  # Copy to keep original
print("Alphabetically Sorted Using sort():", animals_sorted_alphabetically)
print("Sorted by Length Using sorted():", animals_sorted_by_length)


# 3

def filter_animals(char,animals):
    filter_list=[]

    for animals in animals:
        if len(animals)>char.len:
            filter.append(animals)
        return filter_list
print (filter_animals)


# 4

# processed_animals=[]

# for animals in animals:
#     if animals not in processed_animals:
#         processed_animals=animals.append(animals)
#         print (processed_animals)


# 5

# def cateh

def filter_animals_by_lenght(animals):
    for x in animals:
        if x.len>5:
            new_animals=print(x)
        else:
            print("no animals found")
    
    return new_animals

#create dictonary
animals_dictonary = {
    "mammals":animals[0:4],
    "birds":animals[4:8],
}
print(animals_dictonary)