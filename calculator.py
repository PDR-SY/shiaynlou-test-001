#! /usr/bin/env python3

import sys

def insurence(money):
	return money*0.08+money*0.02+money*0.005+money*0.06

def getTax(m):
	money = None
	if m<=1500:
		money = format(m*0.03,".2f")
	elif m>1500 and m<=4500:
		money = format(m*0.1-105,".2f")
	elif m>4500 and m<=9000:
		money =format(m*0.2-555,".2f")
	elif m>9000 and m<=35000:
		money = format(m*0.25-1005,".2f")
	elif m>35000 and m<=55000:
		money = format(m*0.30-2755,".2f")
	elif m>55000 and m<=80000:
		money = format(m*0.35-5505,".2f")
	else:
		money = format(m*0.45-13505,".2f")
	return money
	
#try:
	for person in sys.argv[1:]:
		number = int(person.split(":")[0])
		money = int(person.split(":")[1])
		m = money - insurence(money) -3500
		m = money-getTax(m)
		print('{}:{}'.format(number,m))

#except ValueError:
#	print("Parameter Error")
#except TypeError:
#	print("Parameter Error")

