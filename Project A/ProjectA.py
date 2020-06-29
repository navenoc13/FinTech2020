def numEdges(a,b,c,d,e,f,g):
	return (a+b+c+d+f+g) + (a*e) + (b*e) + (c*e) + (c*f) + (d*f) + (e*g)

def numPaths(a,b,c,d,e,f,g):
	return g*(a*e + b*e + c*e) + c*f + d*f

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())


numEdge = numEdges(a,b,c,d,e,f,g)
numPath = numPaths(a,b,c,d,e,f,g)

print (numEdge)
print (numPath)

