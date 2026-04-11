def main():
    data = {'a':1, 'b':2}
    func(**data)

def func(**kwargs):
    print(kwargs)

if __name__ == "__main__":
    main()