import sys
import os
import datetime



def main():
	readaccount()
	login()
	#os.system('cls')#windows清屏命令
	while True:
		menu()
		readstatement()
		while True:
			try:
				num=int(input('Please input the num which you want:'))
				break
			except ValueError:
				print('Please input a NUM.')
		if num==1:
			credit_line()
		elif num==2:
			withdraw_cash()
		elif num==3:
			bill()
		elif num==4:
			alter()
		elif num==5:
			save()
		elif num==6:
			print('ByeBye!')
			sys.exit()

def readaccount():
	accfile='account.txt'
	global accountdict
	accountdict={}
	global account
	global shouxin
	global tixian
	with open(accfile,'r') as af:
		af.flush()
		for line in af:
			account=line.split()[0]
			b=line.split()[1]
			shouxin=line.split()[2]
			tixian=line.split()[3]
			accountdict[account]=[b,shouxin,tixian]
		print(accountdict)
	af.close()

def login():
	print('Welcome use the credit_cart system!')
	num=0
	global creditnum
	while True:
		try:
			creditnum=int(input('Please input the credit_cart NUM.:').strip())
			if str(creditnum) in accountdict.keys():
				passwd=int(input('Please input the password:').strip())
				if str(passwd)==accountdict[str(creditnum)][0]:
					print('-----------------------------------------')
					print('Hello ',creditnum,' !')
					print('Login datetime: ',datetime.datetime.now())
					fs='statement-'+str(creditnum)+'.txt'
					fsfile=open(fs,'w')
					fsfile.close()
					fb='bill-'+str(creditnum)+'.txt'
					fbfile=open(fb,'w')
					fbfile.close()
					break
				else:
					print('Warning:Wrong password!')
					num=num+1
			else:
				print('There is no the account NUM.')
				num=num+1
		except ValueError:
			print('Please input a number ')
			num=num+1
		
		print('Wrong:',num)
		if num>2:
			print('EXIT!!!')
			sys.exit()
			
def menu():
	print('******************************************')
	print('1 额度 2 提现 3 账单 4 还款 6 退出')

	


def readstatement():
	f='statement-'+str(creditnum)+'.txt'
	global statement
	statement=[]
	global isstatementnull
	isstatementnull=True
	try:
		with open(f,'r' ) as fbr:
			fbr.flush()
			if os.path.getsize(f)>0:
				rownum=0
				for line in fbr:
					dt=line.split()[0]
					num=line.split()[1]
					description=line.split()[2]
					money=line.split()[3]
					charge=line.split()[4]
					
					rowlist=[]
					rowlist.append(str(dt))
					rowlist.append(str(num))
					rowlist.append(str(description))
					rowlist.append(str(money))
					rowlist.append(str(charge))
					statement.append(rowlist)
					print('statement:',statement)
			else:
				isstatementnull=False
				#print('账号流水为空。')
		fbr.close()
	except IOError:
		print('没有流水单。')
		
	
	global moneytotal
	moneytotal=0
	global tixiantotal
	tixiantotal=0
	global chargetotal
	chargetotal=0
	global xiaofeitotal
	xiaofeitotal=0
	if len(statement)>0:
		numstatement=0
		while numstatement<len(statement):
			moneytotal=moneytotal+int(statement[numstatement][3])
			chargetotal=chargetotal+float(statement[numstatement][4])
			if statement[numstatement][2]=='提现':
				tixiantotal=tixiantotal+int(statement[numstatement][3])
			numstatement=numstatement+1
		xiaofeitotal=moneytotal-tixiantotal
		#print('moneytotal:',moneytotal)
		#print('tixiantotal:',tixiantotal)
		#print('xiaofeitotal:',xiaofeitotal)
		#print('chargetotal:',tixiantotal)
		
def credit_line():
	print('授信额度为：',shouxin,'元，剩余：',int(shouxin)-float(xiaofeitotal),'元')
	print('提现额度为：',tixian,'元，剩余：',int(tixian)-float(tixiantotal),'元')
	
	
def writestatement(neirong,jine,charge):
	f='statement-'+str(creditnum)+'.txt'
	with open(f,'a+') as fba:
		fba.write(str(datetime.datetime.now().strftime('%Y-%m-%d(%H:%M:%S)'))+'\t'+str(creditnum)+'\t'+neirong+'\t'+str(jine)+'\t'+str(charge)+'\n')
		fba.flush()
	fba.close()
	
def withdraw_cash():#提现
	try:
		while True:
			withdrawnum=int(input('提取金额(元)：').strip())
			if withdrawnum<(int(tixian)-float(tixiantotal)):
				if withdrawnum>0:
					writestatement('提现',withdrawnum,withdrawnum*0.05)
				break
			else:
				print('超出提现额度，请重新输入。')
	except ValueError:
		print('Please input a number.')

def bill():
	print()

main()


