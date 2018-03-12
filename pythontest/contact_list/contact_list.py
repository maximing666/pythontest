# -*- coding:utf-8 -*-
import shutil
import os
#from tabulate import tabulate
from prettytable import PrettyTable

str='contact_list.txt'
strtemp='contact_list_temp.txt'
f=file(str)
#c=f.readlines()
#print c



def menu():
	print '\n===================================================='
	menu='1 add���� 2 deleteɾ�� 3 alter�޸� 4 select��ѯ 5 list�б� 6 quit�˳�'
	print menu

def tb_init():#��ʼ��������
	global tb;
	tb=PrettyTable(['No.','Name','Sex','Dev'])
	tb.align='l'#���ȫ�������(��l��������룩����c�������У�����r���Ҷ���)
	tb.sortby='No.'#��NO.������
	

def add():
	print '-----------now list-------------'
	list()
	while True:
		input1=raw_input('Add continue?(Y/N):').strip()
		with open(str,'a+') as yy: 					
				if len(input1)>0:					
					if input1=='N' or input1=='n':						
						yy.close;
						break;
					elif input1=='Y' or input1=='y':
						
						flag=True
						while flag:
							input_add2=raw_input('Name:').strip()
							if len(input_add2)>0:
								flag=False

						flag=True
						while flag:
							input_add3=raw_input('Sex:').strip()
							if len(input_add3)>0:
								flag=False
						flag=True
						while flag:
							input_add4=raw_input('Dep:').strip()
							if len(input_add4)>0:
								flag=False						
												
						yy.writelines('\n'+input_add2+'\t'+input_add3+'\t'+input_add4);
						yy.flush
		print '-----------after add list-------------'						
		list()
					

def delete():
	while True:
		print '--------------------------------'
		input2=raw_input('please write into str you want to delete(or quit):').strip()
		tb_init()
		with open(str,'r') as yy: 
			with open(strtemp,'w+') as dd: 

				if len(input2)>0:
					num=0
					listnum=1
					for line in yy:
						if input2 not in line:					
							dd.write(line)
						if input2 in line:					
							#print 'NO.++',listnum,':',line,
							list_d=[`listnum`]+line.strip().split('\t')
							tb.add_row(list_d)
							num=num+1
						listnum=listnum+1
					if listnum>1 and num>0:
						print(tb)
						while True:
							real=raw_input('\nȷ��ɾ����Y/N:').strip()
							if real=='Y' or real=='y':
								dd.close() #�˴���ر�dd,���򸲸��ļ�ʱ���ᱨwindows32��������Ϊ���ļ��Ѿ����ˡ�
								shutil.move(strtemp,str)
								yy.flush
								break
							if real=='N' or real=='n':
								break
					else:
						print 'No result!'
					if input2=='quit':
						yy.close
						dd.close
						break

def alter():
	flag_alter=True
	while flag_alter:
		print '--------------------------------'

		flag=True
		while flag:
			input3=raw_input('Old string(or quit):').strip()
			if input3=='quit':
				flag=False
				flag_alter=False
				break
			elif len(input3)>0:
				flag=False


				flag=True
				while flag:
					input3_new=raw_input('New string(or quit):').strip()
					if input3_new=='quit':
						flag=False
						flag_alter=False
						break
					elif len(input3_new)>0:
						flag=False
			
					flag=True

					while flag:
						input3_mode=raw_input('Replace mode:G(ȫ��)/L(����):').strip()
						if input3_mode=='quit':
							flag=False
							flag_alter=False
							break
						
						if input3_mode=='G' or input3_mode=='g':
							flag=False
						if input3_mode=='L' or input3_mode=='l':
							flag=False
							flag_line=True
							while flag_line:
								input3_lineNo=raw_input('Please write into which NO. you want replace:').strip()
								if input3_lineNo.isdigit():
									flag_line=False

						tb_init()
						tb2=PrettyTable(['No.','Name','Sex','Dev'])
						tb2.align='l'#���ȫ�������left,center,right
						tb2.sortby='No.'#��NO.������
						with open(str,'r') as yy: 
							with open(strtemp,'w+') as dd: 

								if len(input3)>0:
									num=0#��ѯ�����¼��
									listnum=1#���������
									for line in yy:
										if input3 not in line:					
											dd.write(line)
										if input3 in line:							
											list_ab=[`listnum`]+line.strip().split('\t')							
											tb.add_row(list_ab)
											if input3_mode=='G' or input3_mode=='g':								
												line=line.replace(input3,input3_new)
												dd.write(line)
											elif input3_mode=='L' or input3_mode=='l':								
												if  listnum==int(input3_lineNo):
													line=line.replace(input3,input3_new)
													dd.write(line)
												else:
													dd.write(line)
											list_af=[`listnum`]+line.strip().split('\t')							
											tb2.add_row(list_af)							
											num=num+1							
										listnum=listnum+1						
									print 'Before replace:'
									print(tb)
									if listnum>1 and num>0:
										print 'After replace:'
										print(tb2)
										while True:
											real=raw_input('\nȷ���滻��(Y/N):').strip()
											if real=='Y' or real=='y':
												dd.close() #�˴���ر�dd,���򸲸��ļ�ʱ���ᱨwindows32��������Ϊ���ļ��Ѿ����ˡ�
												shutil.move(strtemp,str)
												yy.flush								
												break
												
											if real=='N' or real=='n':
												break
									else:
										print 'No search result.'

						

def search():	
	while True:
		print '--------------------------------'
		input4=raw_input('please write into str you want to search(or quit):').strip()
		tb_init()
		with open(str,'r') as yy: 
			yy.flush
			if len(input4)>0:
				if input4=='quit':
					break
				num=0
				listnum=1
				for line in yy:
					if input4 in line:						
						list_s= [`listnum`]+line.strip().split('\t')
						tb.add_row(list_s)
						num=num+1
					listnum=listnum+1				
				if num==0:
					print "No search result."
				else:
					print(tb)

def list():
	  tb_init()
	  with open(str,'r') as yy:
			yy.flush
			listnum=1
			for line in yy:
				list_l= [`listnum`]+line.strip().split('\t')
				tb.add_row(list_l)				
				listnum=listnum+1
	  print(tb)
	  yy.close

def main():
	while True:
		menu()
		input=raw_input('Please write the number: ')
		

		if input=='1' or input=='add':
			add()
			
		elif input=='2' or input=='delete':
			delete()
		elif input=='3' or input=='alter':
			alter()
		elif input=='4' or input=='search':
			search()
		elif input=='5' or input=='list':
			list()
		elif input=='6' or input=='quit':
			break

main()