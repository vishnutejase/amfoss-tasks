def hello(input_string):
    check_string = "hello"
    i = 0
    for c in input_string:
        if c == check_string[i]:
            i += 1
            if i == len(check_string):
                return "YES"
    return "NO"

def main():
    input_string = input().strip()
    output = hello(input_string)
    print(output)

if __name__ == "__main__":
    main()
