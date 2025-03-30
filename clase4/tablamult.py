print("      0   1   2   3   4   5   6   7   8   9")
print("---------------------------------------------")

for i in range(0, 10):
    print(f"{str(i)+":":<6s}", end="")
    for j in range(0, 10):
        print(f"{i*j:<3d}", end=" ")
    print("\n")
