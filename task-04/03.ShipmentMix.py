def find_smallest_not_in_list(lst):
    for i in range(0, 101):
        if i not in lst:
            return i

test_cases = int(input())
results = []

for _ in range(test_cases):
    ship = []
    ship_length = int(input())
    ship = input().strip().split(" ")

    a = []
    b = []
    elements = ship.copy()
    i = 0

    while True:
        if str(i) not in ship:
            for element in elements:
                a.append(int(element))
            break
        elif elements.count(str(i)) == 1:
            a.append(int(i))
            elements.remove(str(i))
        elif elements.count(str(i)) >= 2:
            a.append(int(i))
            elements.remove(str(i))
            while str(i) in elements:
                b.append(int(i))
                elements.remove(str(i))
        else:
            pass

        i += 1

    results.append(find_smallest_not_in_list(a) + find_smallest_not_in_list(b))

for result in results:
    print(result)
