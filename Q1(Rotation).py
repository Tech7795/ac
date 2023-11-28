#@title Q1 Matrices: 270° = 90°
def rotate_90_clockwise(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    rotated_matrix = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            rotated_matrix[j][num_rows - i - 1] = matrix[i][j]

    return rotated_matrix

def rotate_90_counterclockwise(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    rotated_matrix = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            rotated_matrix[num_cols - j - 1][i] = matrix[i][j]

    return rotated_matrix

# Test the rotations with a 2x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7,8,9],
    [10,11,12]
]

m1=matrix
print("Enter the degress:")
c1=int(input())
n =int(c1/90)
while n!=0:
   m1= rotate_90_clockwise(m1)
   n=n-1
rotated_90 = rotate_90_counterclockwise(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nMatrix Rotated 270 degrees clockwise:")
for row in m1:
    print(row)

print("\nMatrix Rotated 90 degrees counterclockwise:")
for row in rotated_90:
    print(row)
# Check if the rotated matrices are equal
if m1 == rotated_90:
    print("\nBoth rotations are equivalent.")
    print("Success")
else:
    print("\nBoth rotations are not equivalent.")
