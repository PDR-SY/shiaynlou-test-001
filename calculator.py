#! /usr/bin/env python3

import sys
try:
	m = int(sys.argv[1])
	m = m-3500

	if m<=1500:
		print(format(m*0.03,".2f"))
	elif m>1500 and m<=4500:
		print(format(m*0.1-105,".2f"))
	elif m>4500 and m<=9000:
		print(format(m*0.2-555,".2f"))
	elif m>9000 and m<=35000:
		print(format(m*0.25-1005,".2f"))
	elif m>35000 and m<=55000:
		print(format(m*0.30-2755,".2f"))
	elif m>55000 and m<=80000:
		print(format(m*0.35-5505,".2f"))
	else:
		print(format(m*0.45-13505,".2f"))
except ValueError:
	print("Parameter Error")
except TypeError:
	print("Parameter Error")

