def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(greet("World"))
    
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    assert greet("Alice") == "Hello, Alice!"
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    
    print("All tests passed!")