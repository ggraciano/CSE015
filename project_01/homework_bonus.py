# 1.1 AND(p and q)
def AND(p, q):
	if p == True and q == True:
		return True
	elif p == True and q == False:
		return False
	elif p == False and q == True:
		return False
	else:
		return False

# 1.2 OR(p or q)
def OR(p, q):
	if p == True and q == True:
		return True
	elif p == True and q == False:
		return True
	elif p == False and q == True:
		return True
	else:
		return False

# 1.3 IF(p -> q)
def IF(p, q):
	if p == True and q == True:
		return True
	elif p == True and q == False:
		return False
	elif P == False and q == True:
		return True
	else:
		return True

# 1.4 NOT(-p)
def NOT(p):
	if p == True:
		return False
	else:
		return True

# 1.5 IFF(p <-> q)
def IFF(p, q):
	if p == True and q == True:
		return True
	elif p == True and q == False:
		return False
	elif p == False and q == True:
		return False
	else:
		return True

# 1.6
def evaluate(formula):
	if formula[0] == 'AND':
		return AND(formula[1], formula[2])
	elif formula[0] == 'OR':
		return OR(formula[1], formula[2])
	elif formula[0] == 'IF':
		return IF(formula[1], formula[2])
	elif formula[0] == 'NOT':
		return NOT(formula[1])
	else:
		return IFF(formula[1], formula[2])

print("Simple Evaluation Function Test\n")

p = True
q = False

print("p = ", p)
print("q = ", q,"\n")
print("(p or q): \t", evaluate(('OR', p, q)))
print("(p and q): \t", evaluate(('AND', p, q)))
print("(p -> q): \t", evaluate(('IF', p, q)))
print("(p <-> q): \t", evaluate(('IFF', p, q)))
print("-p: \t\t", evaluate(('NOT', p)))

# 2
def cartesianProduct(x, y):
	xlen = len(x)
	ylen = len(y)
	z = [[0 for c in range(ylen)] for r in range(xlen)]
	for i in range(xlen):
		for j in range(ylen):
			z[i][j] = x[i] * y[j]
	return z

x = ['a','e']
y = [1,3,7,9]

z = cartesianProduct(x, y)

# 3
def merge(list1, list2):
	llen1 = len(list1)
	llen2 = len(list2)
	
	rlen = llen1 + llen2
	result = [0] * rlen
	
	i = 0
	j = 0
	k = 0
	
	while i < llen1 and j < llen2:
		if list1[i] < list2[j]:
			result[k] = list1[i]
			print(result[k], list1[i])
			i += 1
			k += 1
		else:
			result[k] = list2[j]
			print(result[k], list2[j])
			j += 1
			k += 1
	if i < llen1:
		while k < rlen:
			result[k] = list1[i]
			i += 1
			k += 1
	else:
		while k < rlen:
			result[k] = list2[j]
			j += 1
			k += 1
	return result

print("merge([1,3,5,7], [2,4,6,8]):\t", merge([1,3,5,7], [2,4,6,8]))

# 4
def gcd(a, b):
	if a == 0:
		return b
	else:
		return gcd(b%a, a)

print(gcd(128, 60))
