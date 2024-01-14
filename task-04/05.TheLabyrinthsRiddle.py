def is_elegant(arr):
    n = len(arr)
    if sorted(arr) == arr:
        return True

    idx = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            idx = i
            break

    for i in range(idx + 1, n):
        if arr[i] < arr[i - 1]:
            return False

    return arr[0] >= arr[-1]

def process_test_case():
    d = int(input())
    queries = list(map(int, input().split()))
    result = []
    series = []

    for q in queries:
        series.append(q)
        if is_elegant(series):
            result.append('1')
        else:
            result.append('0')
            series.pop()

    print(''.join(result))

test_cases = int(input())

for k in range(test_cases):
    process_test_case()
