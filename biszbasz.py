for x in range(1,100):
	s = ''
	if (x % 3) == 0:
		s += 'Bisz'
	if (x % 5) == 0:
		s += 'Basz'
	if s == '':
		s = str(x)
	print s
