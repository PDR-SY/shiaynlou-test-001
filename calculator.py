#! /usr/bin/env python3

import sys

def insurence(money):
	m = money*0.08+money*0.02+money*0.005+money*0.06
	return m

def getTax(m):
	
	if m<=1500:
		return m*0.03
	elif m>1500 and m<=4500:
		return m*0.1-105
	elif m>4500 and m<=9000:
		return m*0.2-555
	elif m>9000 and m<=35000:
		return m*0.25-1005
	elif m>35000 and m<=55000:
		return  m*0.30-2755
	elif m>55000 and m<=80000:
		return m*0.35-5505
	else:
		return m*0.45-13505
	
	
try:
	for person in sys.argv[1:]:
		number = int(person.split(":")[0])
		money = int(person.split(":")[1])
		n = insurence(money)
		if money<=3500:
			print('{}:{}'.format(number,format(money-n,".2f")))
		else:
			m = money -n-3500
			k = getTax(m)
			new_money=money-n-k
			print('{}:{}'.format(number,format(new_money,".2f")))

except ValueError:
	print("Parameter Error")
except TypeError:
	print("Parameter Error")

