def print_grid(size):
    for num in range(size):
        for j in range(size):
            print('#', end="")
        print("")

size = int(input("Size: "))
while size < 1 or size > 8:
    size = int(input("Size: "))

print_grid(size)
