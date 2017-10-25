x = input()
y = input()

i = (x,y)
l1 = []
l2 = []

div = 1
for z in i: 
	while( div >= z ):
		if( z % div == 0 ):
			l1.append(div)
			div = div + 1
			
for a in l1:
	if a not in l2:
		l2.append(a)
		
print(l2)