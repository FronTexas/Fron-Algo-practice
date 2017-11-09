# Complete the function below.
def isValidIndex(i,j,m):
    return 0 <= i and i < len(m) and 0 <= j and j < len(m[i])

def findCluster(i,matrix,boolean_matrix):
    edited = False
    for j in range(0,len(matrix[i])):
        if matrix[i][j] == 1 and not boolean_matrix[i][j]:
            edited = True
            boolean_matrix[i][j] = True 
            boolean_matrix[j][i] = True 
            if i == j: continue
            findCluster(j,matrix,boolean_matrix)
    return edited

def getNumberOfClusters(m):
    cluster_counter = 0
    boolean_matrix = [[False for i in range(len(m[0]))] for j in range(len(m))]
    
    for i in range(len(m)):
        if findCluster(i,m,boolean_matrix):
            cluster_counter += 1
    return cluster_counter
    
def print2d(m):
    for i in range(len(m)):
        print m[i]

def zombieCluster(zombies):
    m = []
    for row in zombies:
        row = [int(e) for e in row]
        m.append(list(row))
    print2d(m)
    return getNumberOfClusters(m)

print zombieCluster(['1100','1110','0110','0001'])
print zombieCluster(['10000','01000','00100','00010','00001'])


