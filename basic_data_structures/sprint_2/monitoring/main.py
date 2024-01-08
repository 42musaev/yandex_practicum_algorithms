length_matrix = int(input())
height_matrix = int(input())


def generate_matrix(length_matrix):
    matrix = []
    for _ in range(length_matrix):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


matrix = generate_matrix(length_matrix)

for row in range(height_matrix):
    for col in range(length_matrix):
        print(matrix[col][row], end=" ")
    print()
