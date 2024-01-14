def find(n, t):
    minimum_time = min(t)
    if t.count(minimum_time) == 1:
        return t.index(minimum_time) + 1
    else:
        return "Still Aetheria"

def main():
    n = int(input())
    t = list(map(int, input().split()))
    result = find(n, t)
    print(result)

if __name__ == "__main__":
    main()
