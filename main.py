def max_elements(x):
    arr = []
    for i in range(x):
        print("Enter number", i + 1, ":")
        arr.append(int(input()))
    print("Your array is: ", arr)

    max1 = arr[0]
    max2 = arr[1]
    for j in range(2, n):
        if max1 < max2:
            max1 = max1 + max2
            max2 = max1 - max2
            max1 = max1 - max2
        if arr[j] > max2:
            max2 = arr[j]
    print("Your two max elements are:", max1, max2)
n = int(input("Enter amount of aray: "))

if n <= 2:
    print("Your array must be bigger than ",n)
else:
    max_elements(n)
