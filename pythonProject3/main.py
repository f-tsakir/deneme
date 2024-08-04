def matmul(A,B):
    C=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(B)):
            product=0
            for k in range(len(A[i])):
                product+=A[i][k]+B[k][j]
            row.append(product)
        C.append(row)
    return C

A = eval(input())
B = eval(input())
C = matmul(A, B)
print(C)