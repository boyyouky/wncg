ddef fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
	
	
	def fact1(n):
	t=1
	s=n
	if s==1:
		return s
	for t in range(n):
		n=n-1
		s=s*n
		if n==1:
			break
	return s