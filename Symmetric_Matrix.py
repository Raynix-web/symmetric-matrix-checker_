def is_symmetric(matrix):
    """
    Function to check if a matrix is symmetric.
    A matrix is symmetric if it is equal to its transpose.

    Args:
    matrix (list of list of int/float): The matrix to check.

    Returns:
    bool: True if the matrix is symmetric, False otherwise.
    """
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])

    # Check if the matrix is square
    if rows != cols:
        return False

    # Check symmetry by comparing elements with their transposed counterparts
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Example usage
matrix = [
    [1, 2, 3],
    [2, 5, 4],
    [3, 4, 6]
]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
