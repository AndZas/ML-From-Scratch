def random(b: int) -> int:
    a: int = 5
    c: int = 1
    m: int = 16
    return (a * b + c) % m


if __name__ == '__main__':
    state: int = int(input("Enter a first state: "))
    k: int = int(input("Enter number of iterations: "))

    for i in range(k):
        state: int = random(state)
        print(state)
