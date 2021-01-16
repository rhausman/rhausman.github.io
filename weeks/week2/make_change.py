



def make_change(n):
	
	if n<=0:
		print(n)
		return [[]]
	all = []
	if n>=25:
		all.append( [25] + make_change(n-25))
	if n>=10:
		all.append(  [10] + make_change(n-10))
	if n>=5:
		all.append( [5]+ make_change(n-10))
	all.append( [l+[1] for l in  make_change(n-1)])
	
	return all
	
