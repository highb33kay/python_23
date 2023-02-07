
def main():
    x = int(input("What is x: "))
    y = int(input("what is y: "))
    added(x, y)


def added(x, y):
    if x > 0:
        print(x)
    if y > 0:
        print(y)

    print(x+y)


main()
