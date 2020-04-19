a=["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
b=["A", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
c=["Partridge in a Pear Tree.","Turtle Doves, and","French Hens,","Calling Birds,","Gold Rings,","Geese-a-Laying,","Swans-a-Swimming,","Maids-a-Milking,","Ladies Dancing,","Lords-a-Leaping,","Pipers Piping,","Drummers Drumming,"]
for j in range(0,12):
	print("On the",a[j],"day of Christmas\nMy true love sent to me")
	for i in range(j,-1,-1):
		print(b[i],c[i])
	print("")