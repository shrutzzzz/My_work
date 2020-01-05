vvlist="12abcbacbaba344ab"
def split(vvlist):							#typecasting
	return list(vvlist)
freq=[]

for w in vvlist:
	freq.append(vvlist.count(w))
	
	
print("count is\n:"+str(list(zip(vvlist,freq))))