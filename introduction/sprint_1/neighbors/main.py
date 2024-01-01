length_matrix = int(input())
_height_matrix = int(input())


def generate_matrix(length_matrix):
    matrix = []
    for _ in range(length_matrix):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def get_neighbors(matrix, row_idx, col_idx):
    neighbors = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if row_idx > 0:
        neighbors.append(matrix[row_idx - 1][col_idx])

    if row_idx < num_rows - 1:
        neighbors.append(matrix[row_idx + 1][col_idx])

    if col_idx > 0:
        neighbors.append(matrix[row_idx][col_idx - 1])

    if col_idx < num_cols - 1:
        neighbors.append(matrix[row_idx][col_idx + 1])
    neighbors.sort()
    return neighbors




matrix = generate_matrix(length_matrix)

row_idx = int(input())
col_idx = int(input())

print(*get_neighbors(matrix, row_idx, col_idx))
