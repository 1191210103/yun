from collections import defaultdict
A = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
B = defaultdict(list)
for i,j in A:
    B[i].append(j)
H = sorted(B.items())
H.sort(reverse=True)
print(H)