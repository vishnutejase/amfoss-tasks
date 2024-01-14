def count_index(input_string):
    check_string = "amfoss"
    c = 0
    for i in range(6):
        if input_string[i] != check_string[i]:
            c += 1
    return c

def main():
    s_len = int(input())
    for j in range(s_len):
        input_string = str(input())
        output = count_index(input_string)
        print(output)

if __name__ == "__main__":
    main()
