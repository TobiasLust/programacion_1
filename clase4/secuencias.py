def main():
    for i in range(10):
        print(i, end=" ")

    print("\n")

    for i in range(0, 10, 2):
        print(i, end=" ")

    print("\n")

    data = [4, 9, 1, 25, 16, 100, 49]

    print(min(data))
    print(max(data))
    print(sum(data))

    for i, num in enumerate(data):
        print(i, num)

        


main()
