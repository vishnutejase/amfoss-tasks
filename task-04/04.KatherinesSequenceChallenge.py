def find_max_occurrence(lst):
    max_count = 0
    max_element = None
    for item in set(lst):
        if lst.count(item) == len(lst) - 1:
            max_count = lst.count(item)
            max_element = item
    return max_element

def process_permutations():
    ans = []
    num_tests = int(input())

    for _ in range(num_tests):
        permutations = []
        final_elements = []
        elements = []

        num_elements = int(input())
        for _ in range(num_elements):
            permutations.append(input().strip().split())

        for i in range(len(permutations)):
            elements.append(permutations[i][0])
        final_elements.append(find_max_occurrence(elements))

        elements = []

        for i in range(len(permutations)):
            elements.append(permutations[i][-1])
        final_elements.append(find_max_occurrence(elements))

        elements = []
        ele = final_elements[0]

        while len(final_elements) < len(permutations):
            for perm in permutations:
                if ele in perm:
                    elements.append(perm[perm.index(ele) + 1])
            final_elements.insert(final_elements.index(ele) + 1, find_max_occurrence(elements))
            elements = []
            ele = final_elements[final_elements.index(ele) + 1]

        ans.append(final_elements)

        if num_elements == 3:
            ans.remove(final_elements)
            final_elements.pop(1)
            for perm in permutations:
                for elem in perm:
                    if elem not in final_elements:
                        final_elements.insert(1, elem)
                        ans.append(final_elements)
                        break

    for result in ans:
        for element in result:
            print(element, end=" ")
        print()

process_permutations()
