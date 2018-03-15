#! /usr/bin/env python3

import sys
import csv


class UserData(object):
	def __init__(self,user_file):
		self.user = self._read_user(user_file)
	def _read_user(self,user_file):
		with open(user_file,'r') as file:
			user = {}
			for line in file:
				line = line.strip()
				key = line.split(',')[0].strip()
				value = line.split(',')[1]
				user[key] = value
			return user


class Config(object):
	def __init__(self,config_file):
		self.config = self._read_config(config_file)
	def _read_config(self,config_file):		
		with open(config_file,'r') as file:
			config = {}
			for line in file:
				line = line.strip()
				key = line.split("=")[0].strip()
				value = line.split("=")[1].strip()
				config[key] = value
			return config




def dumptofile(outfile,result):
	with open(outfile,'a') as file:
		
		writer = csv.writer(file)
		writer.writerows(result)

def calculator(config,user,outfile):
	str_out = []
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
		str_out.append(key)
		str_out.append(value)
		str_out.append(insurence_money)
		str_out.append(tax)
		str_out.append(backmoney)
		dumptofile(outfile,str_out)

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
	
args = sys.argv[1:]
index_config = args.index('-c')
index_user = args.index('-d')
index_out = args.index('-o')
config = Config(args[index_config+1]).config
user = UserData(args[index_user+1]).user
result = calculator(config,user,args[index_out+1])


