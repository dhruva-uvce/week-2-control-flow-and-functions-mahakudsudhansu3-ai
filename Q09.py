def greet(name, greeting="Hello"):
    """Returns a formatted greeting string."""
    return f"{greeting}, {name}!"

def power(base, exp=2):
    """Returns base raised to the power of exp."""
    return base ** exp

if __name__ == "__main__":
    # Demonstrate greet function
    res1 = greet("Alice")
    res2 = greet("Bob", "Hi")
    
    # Demonstrate power function
    res3 = power(5)
    res4 = power(2, 10)
    
    # Print all four results
    print(res1)
    print(res2)
    print(res3)
    print(res4)
