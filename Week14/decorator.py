


def main():
    print(add(3,4))
    print(multiply(5,6))

def log_decorator(func):
     def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)   
        print(f"{func.__name__} returned {result}")        
        return result    
     return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def multiply(c, d):
    return c*d


if __name__ == "__main__":
    main()