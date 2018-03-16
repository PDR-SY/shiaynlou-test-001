#! /usr/bin/env python3

import sys
import csv
import multiprocessing import Process,Queue
from datetime import datetime
import getopt

queue1 = Queue()
queue2 = Queue()
queue3 = Queue()
def _read_user(user_file,config_file):
	with open(user_file,'r') as file:
		user = {}
		for line in file:
			line = line.strip()
			key = line.split(',')[0].strip()
			value = line.split(',')[1]
			user[key] = value
		queue1.put(user)
		_read_config(config_file)



def _read_config(config_file):		
	with open(config_file,'r') as file:
		config = {}
		for line in file:
			line = line.strip()
			key = line.split("=")[0].strip()
			value = line.split("=")[1].strip()
			config[key] = value
		queue2.put(config)




def dumptofile(outfile):
	with open(outfile,'a',newline='') as file:
		result = queue3.get()
		file.write(result)
		#writer = csv.writer(file)
		#writer.writerows(result)

def calculator():
	str_out = ""
	config = queue2.get()
	user = queue1.get()
	for key,value in user.items():
		
		insurence_money = 0.00
		backmoney = 0.00
		tax = 0.00
		if(int(value)<=float(config['JiShuL'])):
			insurence_money = insurence(float(config['JiShuL']),config)
		elif(int(value)>=float(config['JiShuH'])):
			insurence_money = insurence(float(config['JiShuH']),config)
		else:
			insurence_money = insurence(int(value),config)
		
		if int(value)<=3500:
			tax = 0.00
		else:
			tax = format(getTax(int(value)-float(insurence_money)-3500),'.2f')
		backmoney = format(int(value)-float(insurence_money)-float(tax),'.2f')
		str_out = str_out+str(key)+','+str(value)+','+str(insurence_money)+','+str(tax)+','+str(backmoney)+'\n'
		queue3.put(str_out)

def insurence(money,config):
	m = money*float(config['YangLao'])+money*float(config['YiLiao'])+money*float(config['ShiYe'])+money*float(config['GongJiJin'])

	return format(m,'.2f')

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
	
opts,args = getopt.getopt()
index_config = args.index('-c')
index_user = args.index('-d')
index_out = args.index('-o')
p1 = Process(target=_read_user,args=(args[index_user+1],args[index_config+1]))
p2 = Process(target=calculator)
p3 = Process(target=dumptofile,args=(args[index_out+1],))
#config = Config(args[index_config+1]).config
#user = UserData(args[index_user+1]).user
#result = calculator(config,user,args[index_out+1])


