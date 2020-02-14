from numpy import array, round, diag
from numpy.linalg import inv, eigvalsh, eig

#Showing User the Arrays
print("A: [ -1, 2, 1 ], [ 2, 3, 0 ], [ 1, 0, 3 ]")
print("B: [ -1, 1, 3 ], [ 1, 2, 0 ], [ 3, 0, 2 ]")
print("C: [ -3, 2, 2 ], [ 2, 1, 3 ], [ 2, 3, 1 ]")

#Declare each matrix
A = array([[ -1, 2, 1 ], [ 2, 3, 0 ], [ 1, 0, 3 ]], float)
B = array([[ -1, 1, 3 ], [ 1, 2, 0 ], [ 3, 0, 2 ]], float)
C = array([[ -3, 2, 2 ], [ 2, 1, 3 ], [ 2, 3, 1 ]], float)

#Ask for Inputs
input = input("Enter A,B,C to calculate the matrix's Inverse, Eigen Values, Eigen Vector and Diagonalization : ")

if input == "A":
    #Calculate A: inverse of each matrix
    A_inv = inv(A)
    #Calculating A: Eigen Values & V ectors
    A_eigval,A_eigvec = eig(A)
    #Calculate the diagonalization of each matrix
    A_diag = diag(A_eigval)
   #Printing A
    print("\nMatrix A:\n", A)
    print("Inverse Matrix A:\n", round(A_inv, 5))
    print("Eigenvalues of Matrix A:\n", round(A_eigval, 5))
    print("Eigenvectors of Matrix A:\n", round(A_eigvec, 5))
    print("Diagonalization of Matrix A:\n", A_diag)
elif input == "B":
    #Calculate B: inverse of each matrix
        B_inv = inv(B)
        #Calculating A: Eigen Values & Vectors
        B_eigval,B_eigvec = eig(B)
        #Calculate the diagonalization of each matrix
        B_diag = diag(B_eigval)

        #Printing B
        print("\nMatrix B:\n", B)
        print("Inverse Matrix B:\n", round(B_inv, 5))
        print("Eigenvalues of Matrix B:\n", round(B_eigval, 5))
        print("Eigenvectors of Matrix B:\n", round(B_eigvec, 5))
        print("Diagonalization of Matrix B:\n", B_diag)
elif input == "C":
    #Calculate B: inverse of each matrix
    C_inv = inv(C)
    #Calculating A: Eigen Values & Vectors
    C_eigval,C_eigvec = eig(C)
    #Calculate the diagonalization of each matrix
    C_diag = diag(C_eigval)

    #Print C
    print("\nMatrix C:\n", C)
    print("Inverse Matrix C:\n", round(C_inv, 5))
    print("Eigenvalues of Matrix C:\n", round(C_eigval, 5))
    print("Eigenvectors of Matrix C:\n", round(C_eigvec, 5))
    print("Diagonalization of Matrix C:\n", C_diag)