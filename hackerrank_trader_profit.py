#!/bin/python

import sys

def traderProfitRecursive(i,j,m,transactions,k,maxProfit):
	if i >= len(m) or j >= len(m):
		return 
	if sum(transactions) > maxProfit[0]:
		# print transactions
		maxProfit[0] = sum(transactions)
	if len(transactions) == k: 
		return
	for _i in range(j+1,len(m)):
		for _j in range(j+2,len(m)):
			transactions.append(m[_i][_j])
			traderProfitRecursive(_i,_j,m,transactions,k,maxProfit)
			if len(transactions) > 0:
				transactions.pop()

def traderProfit(k, n, A):
	m = [[0 for i in range(len(A))] for i in range(len(A))]
	maxProfit = [0]
	for i in range(len(A)):
		for j in range(i+1,len(A)):
			m[i][j] = A[j] - A[i]
	for i in range(len(A)):
		for j in range(i+1,len(A)):
			traderProfitRecursive(i,j,m,[m[i][j]],k,maxProfit)
	return maxProfit[0]


if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        k = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = traderProfit(k, n, arr)
        print result