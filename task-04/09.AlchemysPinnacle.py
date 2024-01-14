def calculate_difference(l, r):
    if l == r:
        return 0

    l = "0" * (len(r) - len(l)) + l
    diff = 0

    common_prefix_length = 0
    for j in range(len(r)):
        if l[j] != r[j]:
            break
        common_prefix_length += 1

    for j in range(common_prefix_length + 1):
        if j == len(r):
            break
        diff += max(int(l[j]), int(r[j])) - min(int(l[j]), int(r[j]))

    remaining_digits = len(r) - common_prefix_length - 1
    return remaining_digits * 9 + diff

def main():
    n = int(input())
    for _ in range(n):
        l, r = input().strip().split(' ')
        result = calculate_difference(l, r)
        print(result)

if __name__ == "__main__":
    main()
