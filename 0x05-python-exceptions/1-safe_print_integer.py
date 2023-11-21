#!/usr/bin/python3
def safe_print_integer(value):
	isPrinted = False
	try:
		print("{:d}".format(value))
		isPrinted = True
	except ValueError:
		return(isPrinted)
	return (isPrinted)
