def main() -> None:
    double = lambda x,y: x * y
    print(double(5, 10))

    a = int(input('Enter a: '))
    b = int(input('Enter b: '))

    max_number = lambda x,y: x if x>y else y
    print(f"Max number is: {max_number(a, b)}")


if __name__ == '__main__':
    main()

