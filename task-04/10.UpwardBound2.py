def calculate_steps_to_reach_zero(num_list):
    if len(num_list) == 1:
        return 0

    steps_to_zero = 0
    previous = num_list[-1]

    for current in num_list[-2::-1]:
        while current >= previous:
            current //= 2
            steps_to_zero += 1

            if current == 0 and previous == 0:
                return -1

        previous = current

    return steps_to_zero

def main():
    num_iterations = int(input())

    for _ in range(num_iterations):
        _ = input()
        numbers = list(map(int, input().split()))

        result = calculate_steps_to_reach_zero(numbers)
        print(result)

if __name__ == "__main__":
    main()
