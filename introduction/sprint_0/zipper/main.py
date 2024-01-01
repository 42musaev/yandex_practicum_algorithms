from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i])
        new_list.append(b[i])
    return new_list


def read_input() -> Tuple[List[int], List[int]]:
    int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
