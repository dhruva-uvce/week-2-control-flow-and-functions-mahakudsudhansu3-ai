def add_element(lst, element):
    """Appends element to lst in-place."""
    lst.append(element)

def double_elements(lst):
    """Multiplies every element in lst by 2 in-place."""
    for i in range(len(lst)):
        lst[i] = lst[i] * 2

if __name__ == "__main__":
    # 1. Create a list numbers = [1, 2, 3]
    numbers = [1, 2, 3]
    
    # 2. Call add_element(numbers, 4) and print the list
    add_element(numbers, 4)
    print(numbers)
    
    # 3. Call double_elements(numbers) and print the list
    double_elements(numbers)
    print(numbers)
