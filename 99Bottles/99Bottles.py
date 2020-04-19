def spell(str):
	if i==1:
		x="bottle"
	else:
		x="bottles"
	return x

i=99
x=""
while(i>0):
	n=str(i)
	x=spell(x)
	print(n,x,"of beer on the wall,",n,x,"of beer.")
	i-=1;
	n=str(i)
	x=spell(x)
	if i==0:
		n="no more"
	print("Take one down and pass it around,",n,x,"of beer on the wall.\n")
print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")