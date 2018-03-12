import sys


f='contact_list.txt'
def readfiletodict():
	global dictfile
	dictfile={}
	with open(f,'r') as rf:
		rf.flush()
		num=1
		for line in rf:
			a=line.split()[0]
			b=line.split()[1]
			c=line.split()[2]
			dictfile[num]=[a,b,c]
			
			num=num+1
	rf.close()

def printdict():
	print('Staff list：')
	print('-----------------')
	for k,v in dictfile.items():
		print('NUM.:',k)
		if type(v) is list:
			num=0
			for i in v:
				if num==0:
					print('\tName:',i)
				elif num==1:
					print('\tSex:',i)
				elif num==2:
					print('\tDep.:',i)
				num=num+1

def menu():
	print('------------------------------------------')
	print('1 list 2 insert 3 del 4 alter 5 save 6 quit')

def insert():
	while True:
		while True:
			try:
				a=int(input('NUM. :'))
				if a not in dictfile.keys():
					break
				else:
					print('The NUM. you input is existed!')
			except ValueError:
				print('ERROR:you must input a NUM.!!')
		while True:
			b=input('NAME:').strip()#name非空
			if len(b)>0:
				break
		c=input('SEX:')
		d=input('DEP.:')
		dictfile[a]=[b,c,d]
		print('\nYou will insert a staff:  ',a,dictfile[a])
		break

def delete():
	while True:
		a=input('Please input you want delete or quit:').strip()
		if a=='quit' or a=='':
			break
		else:
			while True:
				print('delete :')
				key=[]
				for k,v in dictfile.items():
					if a==str(k):
						print(k,dictfile[k])
						key.append(k)
					else:
						for i in v:
							if a==i:
								print(k,v)
								key.append(k)
				if len(key)>0:
					break
				else:
					print('NO items!!')
			affirm=input('Affirm to delete?(y/n):').strip()
			if affirm=='y':
				print('Deleted the ',key,'th value.')
				for m in key:
					del dictfile[m]
				break
		
def alter():
	num=0#输入无效字符的计数器
	while True:
		try:
			a=int(input('Please input the NUM. of staff you want to alter:'))
			if a in dictfile.keys():
				num=0
				print('well done!!!!')
				print(a,dictfile[a])
				while True:
					alteritem=input('Please input the itme(NAME,SEX,DEP) or quit:').strip()
					if alteritem=='quit':
						break
					elif alteritem=='NAME':
						name=input('NAME:')
						dictfile[a][0]=name
						print('Alter to :',a,dictfile[a])
					elif alteritem=='SEX':
						sex=input('SEX:')
						dictfile[a][1]=sex
						print('Alter to :',a,dictfile[a])
					elif alteritem=='DEP':
						dep=input('DEP.:')
						dictfile[a][2]=dep
						print('Alter to :',a,dictfile[a])
			else:
				num=num+1
				print('The NUM. is not existed.')
				print('num=',num)
		except ValueError:
			print('The input value is not a int.')
			num=num+1
			print('num=',num)
		if num>2:
			break
	print('连续3次输入无效内容，系统跳出。')

def save():
	with open(f,'w+') as sf:
		for k in dictfile.keys():
			sf.write(dictfile[k][0])
			sf.write('\t')
			sf.write(dictfile[k][1])
			sf.write('\t')
			sf.write(dictfile[k][2])
			sf.write('\n')
	sf.close()
	print('Save completed!')

def main():
	readfiletodict()
	while True:
		menu()
		while True:
			try:
				num=int(input('Please input the num which you want:'))
				break
			except ValueError:
				print('Please input a NUM.')
		
		
		if num==1:
			printdict()
		elif num==2:
			insert()
		elif num==3:
			delete()
		elif num==4:
			alter()
		elif num==5:
			save()
		elif num==6:
			sys.exit()

main()