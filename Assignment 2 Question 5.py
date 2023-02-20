#COMPLETED
#TESTED

"""
You are given a list of coordinates (each as a x,y tuple) representing a 2D shape. 
If the shape has N coordinate, create a Nx3 matrix with the first column having the x values, 
2nd column having the y values, and the third column being 1 for all. 
This represents the matrix for the shape.

You have to scale this 2D shape. For scaling, take as input cx and cy (scaling parameters) 
from the user, and form a matrix of the type:

                        cx 0 0
                        0 cy 0
                        0  0 1

For scaling the shape, multiply the matrix of the shape with this matrix. 
Finally, return the new shape in the form of a list of coordinates - which will be the first two 
columns of the resultant matrix.

Suggestion. While you can easily find matrix multiplication on the net, 
try to first write your own function for this - use online help only if needed.
"""

matrix = []

while(True):
    coords = list(map(int,input("Coordinates: ").split()))

    if bool(coords)==0:
        break

    else:
        matrix.append(coords + [1])


cx = int(input("c_x: "))
cy = int(input("c_y: "))

scaling_matrix = [[cx,0,0],[0,cy,0],[0,0,1]]

def matrix_mult(l1,l2):
    output = [[0 for i in range(len(l2))] for i in range(len(l1))]
    
    for i in range(len(l1)):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                output[i][j] += l1[i][k] * l2[k][j]

    return output

matrix = matrix_mult(matrix,scaling_matrix)

print("Coordinates of the scaled up shape are: ")
for i in matrix:
    print(tuple(i[:2]))